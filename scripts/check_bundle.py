#!/usr/bin/env python3
"""Check that a brand bundle, its rules and its token file agree.

Errors (exit 1):
  - an x-brand-token that does not resolve in the token file
  - an x-brand-token that points at a primitive instead of a semantic token
  - a token alias ({path}) inside the token file that does not resolve
  - an x-brand-rule-type, x-brand-knowledge or x-brand-visibility value
    outside its vocabulary
  - derived knowledge (x-brand-knowledge: derived) that carries a rule type:
    information about the brand is never a rule that applies to it

Warnings (exit 0, or 1 with --strict):
  - a semantic token that no brand term points at
  - a stable rule without a current human review (OKF v0.3, section 5.3);
    limits may instead be confirmed by a process

Usage:
    check_bundle.py BUNDLE_ROOT [--strict]

The token file is read from x-brand-tokens in the bundle-root index.md
(a path relative to the bundle root). Tokens use the W3C Design Tokens
format: a token is an object with "$value"; groups nest; aliases look
like "{group.token}". Top-level groups named in PRIMITIVE_GROUPS are
primitives; every other group is semantic.

The rule types follow the Brand Infrastructure Report 2026, Table 9:
limit, default, principle, preference.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
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
RESERVED = {"index.md", "log.md"}


def read_frontmatter(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    data = yaml.safe_load(text[4:end])
    return data if isinstance(data, dict) else None


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


def current_reviewers(meta: dict) -> set[str]:
    """Actor schemes of verification events that are current (OKF 5.3)."""
    generated = meta.get("generated") or {}
    gen_at = parse_time(generated.get("at")) if isinstance(generated, dict) else None
    events = meta.get("verified") or []
    if isinstance(events, dict):
        events = [events]
    schemes: set[str] = set()
    for event in events:
        if not isinstance(event, dict):
            continue
        by, at = str(event.get("by", "")), parse_time(event.get("at"))
        if by and at and (gen_at is None or at >= gen_at):
            schemes.add(by.split(":", 1)[0] if ":" in by else "agent")
    return schemes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("bundle", type=Path)
    parser.add_argument("--strict", action="store_true", help="exit 1 on warnings")
    args = parser.parse_args()

    root = args.bundle.resolve()
    index = root / "index.md"
    meta = read_frontmatter(index) if index.exists() else None
    token_ref = (meta or {}).get("x-brand-tokens")
    if not token_ref:
        print(f"error: {index} has no x-brand-tokens key", file=sys.stderr)
        return 2
    token_path = (root / str(token_ref)).resolve()
    if root not in token_path.parents:
        print(f"error: x-brand-tokens points outside the bundle: {token_ref}", file=sys.stderr)
        return 2
    tokens = flatten(json.loads(token_path.read_text(encoding="utf-8")))

    errors: list[str] = []
    warnings: list[str] = []

    for path, token in tokens.items():
        value = token.get("$value")
        match = ALIAS_RE.match(value) if isinstance(value, str) else None
        if match and match.group(1) not in tokens:
            errors.append(f"{token_path.name}: {path} points at missing token {{{match.group(1)}}}")

    default_vis = (meta or {}).get("x-brand-visibility-default")
    if default_vis is not None and default_vis not in VOCAB["x-brand-visibility"]:
        errors.append(f"index.md: x-brand-visibility-default {default_vis!r} is not public, internal or restricted")

    referenced: set[str] = set()
    for md in sorted(root.rglob("*.md")):
        if md.name in RESERVED or any(part.startswith(".") for part in md.relative_to(root).parts):
            continue
        fm = read_frontmatter(md)
        if not fm or not fm.get("type"):
            continue
        rel = md.relative_to(root)
        status = fm.get("status") or "stable"

        for key, allowed in VOCAB.items():
            value = fm.get(key)
            if value is not None and value not in allowed:
                errors.append(f"{rel}: {key} {value!r} is not one of {', '.join(sorted(allowed))}")

        rule_type = fm.get("x-brand-rule-type")
        if fm.get("x-brand-knowledge") == "derived" and rule_type:
            errors.append(f"{rel}: derived knowledge must not carry x-brand-rule-type; it is not a rule")

        ref = fm.get("x-brand-token")
        if ref:
            ref = str(ref)
            if ref not in tokens:
                errors.append(f"{rel}: x-brand-token {ref!r} does not exist in {token_path.name}")
            elif ref.split(".")[0] in PRIMITIVE_GROUPS:
                errors.append(f"{rel}: x-brand-token {ref!r} is a primitive; point at a semantic token")
            elif status != "deprecated":
                referenced.add(ref)

        if status == "stable" and rule_type:
            reviewers = current_reviewers(fm)
            confirmed = "human" in reviewers or (rule_type == "limit" and "process" in reviewers)
            if not confirmed:
                warnings.append(f"{rel}: stable {rule_type} without a current review by a person"
                                + (" or process" if rule_type == "limit" else ""))

    for path in sorted(tokens):
        if path.split(".")[0] not in PRIMITIVE_GROUPS and path not in referenced:
            warnings.append(f"{token_path.name}: semantic token {path} has no brand term")

    for line in errors:
        print(f"ERROR   {line}")
    for line in warnings:
        print(f"WARNING {line}")
    print(f"{len(errors)} error(s), {len(warnings)} warning(s)")
    if errors or (args.strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
