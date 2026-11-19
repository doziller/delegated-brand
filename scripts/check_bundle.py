#!/usr/bin/env python3
"""Check that a brand bundle, its rules and its token file agree.

Errors (exit 1):
  - an approved rule whose content no longer matches the hash stored in its
    latest approval (x-brand-hash in verified): the text or fields changed
    after approval. The last approved version in Git applies until someone
    approves again with scripts/approve.py.
  - an approved rule whose generated date is newer than its latest approval
  - an x-brand-token that does not resolve, or points at a primitive
  - a token alias ({path}) inside the token file that does not resolve
  - an x-brand-rule-type, x-brand-knowledge or x-brand-visibility value
    outside its vocabulary
  - derived knowledge (x-brand-knowledge: derived) that carries a rule type
  - an x-brand-owner that is not a human: or team: actor

Warnings (exit 0, or 1 with --strict):
  - an approval without x-brand-hash: it is not bound to the content, so a
    later change cannot be detected
  - a stable rule that was never approved
  - a public semantic token that no brand term points at

What this check cannot know: who actually ran approve.py. Anyone who can
edit the files can also re-approve them. Restrict that with CODEOWNERS and
branch protection.

Usage:
    check_bundle.py BUNDLE_ROOT [--strict]

The rule types follow the Brand Infrastructure Report 2026, Table 9.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from brandlib import content_hash, split  # noqa: E402
except ImportError:
    print("check_bundle.py needs PyYAML: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

PRIMITIVE_GROUPS = {"primitive"}
VOCAB = {
    "x-brand-rule-type": {"limit", "default", "principle", "preference"},
    "x-brand-knowledge": {"strategic", "implementation", "derived"},
    "x-brand-visibility": {"public", "internal", "restricted"},
}
ALIAS_RE = re.compile(r"^\{([^{}]+)\}$")
OWNER_RE = re.compile(r"^(human|team):\S+$")
RESERVED = {"index.md", "log.md"}


def flatten(node: dict, prefix: str = "") -> dict[str, dict]:
    """Return {dotted.path: token} for every object that has $value."""
    out: dict[str, dict] = {}
    for key, value in node.items():
        if key.startswith("$") or not isinstance(value, dict):
            continue
        path = f"{prefix}.{key}" if prefix else key
        if "$value" in value:
            out[path] = value
        else:
            out.update(flatten(value, path))
    return out


def parse_time(value) -> datetime | None:
    if value is None:
        return None
    if isinstance(value, datetime):
        return value if value.tzinfo else value.replace(tzinfo=timezone.utc)
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None


def events(meta: dict) -> list[dict]:
    raw = meta.get("verified") or []
    if isinstance(raw, dict):
        raw = [raw]
    return [e for e in raw if isinstance(e, dict) and e.get("by") and parse_time(e.get("at"))]


def check(root: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    meta, _ = split(root / "index.md") if (root / "index.md").exists() else (None, "")
    token_ref = (meta or {}).get("x-brand-tokens")
    if not token_ref:
        return [f"index.md has no x-brand-tokens key"], []
    token_path = (root / str(token_ref)).resolve()
    if root not in token_path.parents:
        return [f"x-brand-tokens points outside the bundle: {token_ref}"], []
    tokens = flatten(json.loads(token_path.read_text(encoding="utf-8")))

    for path, token in tokens.items():
        value = token.get("$value")
        match = ALIAS_RE.match(value) if isinstance(value, str) else None
        if match and match.group(1) not in tokens:
            errors.append(f"{token_path.name}: {path} points at missing token {{{match.group(1)}}}")

    bundle_owner = (meta or {}).get("x-brand-owner")
    if bundle_owner is not None and not OWNER_RE.match(str(bundle_owner)):
        errors.append(f"index.md: x-brand-owner {bundle_owner!r} must be a human: or team: actor")
    default_vis = (meta or {}).get("x-brand-visibility-default")
    if default_vis is not None and default_vis not in VOCAB["x-brand-visibility"]:
        errors.append(f"index.md: x-brand-visibility-default {default_vis!r} is not public, internal or restricted")

    referenced: set[str] = set()
    for md in sorted(root.rglob("*.md")):
        rel = md.relative_to(root)
        if md.name in RESERVED or any(part.startswith(".") for part in rel.parts):
            continue
        fm, _ = split(md)
        if not fm or not fm.get("type"):
            continue
        status = fm.get("status") or "stable"
        rule_type = fm.get("x-brand-rule-type")

        for key, allowed in VOCAB.items():
            value = fm.get(key)
            if value is not None and value not in allowed:
                errors.append(f"{rel}: {key} {value!r} is not one of {', '.join(sorted(allowed))}")
        if fm.get("x-brand-knowledge") == "derived" and rule_type:
            errors.append(f"{rel}: derived knowledge must not carry x-brand-rule-type; it is not a rule")
        owner = fm.get("x-brand-owner")
        if owner is not None and not OWNER_RE.match(str(owner)):
            errors.append(f"{rel}: x-brand-owner {owner!r} must be a human: or team: actor")

        ref = fm.get("x-brand-token")
        if ref:
            ref = str(ref)
            if ref not in tokens:
                errors.append(f"{rel}: x-brand-token {ref!r} does not exist in {token_path.name}")
            elif ref.split(".")[0] in PRIMITIVE_GROUPS:
                errors.append(f"{rel}: x-brand-token {ref!r} is a primitive; point at a semantic token")
            elif status != "deprecated":
                referenced.add(ref)

        if status != "stable" or not rule_type:
            continue

        allowed_schemes = {"human"} | ({"process"} if rule_type == "limit" else set())
        approvals = [e for e in events(fm) if str(e["by"]).split(":", 1)[0] in allowed_schemes]
        if not approvals:
            warnings.append(f"{rel}: stable {rule_type} that was never approved")
            continue
        latest = max(approvals, key=lambda e: parse_time(e["at"]))
        generated = fm.get("generated") or {}
        gen_at = parse_time(generated.get("at")) if isinstance(generated, dict) else None
        if gen_at and parse_time(latest["at"]) < gen_at:
            errors.append(f"{rel}: approved {rule_type} was regenerated after its latest approval; "
                          "the last approved version in Git applies until it is approved again")
            continue
        stored = latest.get("x-brand-hash")
        if not stored:
            warnings.append(f"{rel}: approval is not bound to the content (no x-brand-hash); "
                            "re-approve with scripts/approve.py")
        elif stored != content_hash(md):
            errors.append(f"{rel}: approved {rule_type} changed after approval (content hash differs); "
                          "the last approved version in Git applies until it is approved again")

    for path in sorted(tokens):
        public = (tokens[path].get("$extensions") or {}).get("x-brand-visibility", "public") == "public"
        if public and path.split(".")[0] not in PRIMITIVE_GROUPS and path not in referenced:
            warnings.append(f"{token_path.name}: semantic token {path} has no brand term")
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("bundle", type=Path)
    parser.add_argument("--strict", action="store_true", help="exit 1 on warnings")
    args = parser.parse_args()

    errors, warnings = check(args.bundle.resolve())
    for line in errors:
        print(f"ERROR   {line}")
    for line in warnings:
        print(f"WARNING {line}")
    print(f"{len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors or (args.strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
