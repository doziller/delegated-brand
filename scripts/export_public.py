#!/usr/bin/env python3
"""Export the public part of a brand bundle.

A convenience tool, not a security boundary. It leaves out what is marked
non-public; it cannot find internal information written into public text.
Read the export before you share it.

What it does:
  - leaves out every concept whose visibility is internal or restricted
    (x-brand-visibility, or x-brand-visibility-default in index.md)
  - leaves out every log.md, which may describe internal decisions
  - leaves out tokens marked non-public in the token file, using
    "$extensions": {"x-brand-visibility": "internal"} on a token or group
  - removes links to left-out concepts: a list line whose only links point
    to left-out concepts is removed; elsewhere the link text stays and the
    link goes, so table rows and sentences keep their public content

Usage:
    export_public.py BUNDLE_ROOT OUT_DIR
"""

from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from brandlib import split  # noqa: E402
except ImportError:
    print("export_public.py needs PyYAML: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
LIST_ITEM_RE = re.compile(r"^\s*[*-]\s")


def is_local(target: str) -> bool:
    return not target.startswith(("http:", "https:", "#", "mailto:"))


def filter_tokens(node: dict) -> tuple[dict, int]:
    """Drop tokens and groups whose $extensions mark them non-public."""
    removed = 0
    out = {}
    for key, value in node.items():
        if isinstance(value, dict) and not key.startswith("$"):
            vis = (value.get("$extensions") or {}).get("x-brand-visibility", "public")
            if vis != "public":
                removed += 1 if "$value" in value else max(1, sum(1 for _ in _iter_tokens(value)))
                continue
            if "$value" in value:
                out[key] = value
            else:
                child, n = filter_tokens(value)
                removed += n
                out[key] = child
        else:
            out[key] = value
    return out, removed


def _iter_tokens(node: dict):
    for key, value in node.items():
        if isinstance(value, dict) and not key.startswith("$"):
            if "$value" in value:
                yield value
            else:
                yield from _iter_tokens(value)


def export(root: Path, out: Path) -> tuple[list[Path], int]:
    meta, _ = split(root / "index.md")
    default = (meta or {}).get("x-brand-visibility-default", "public")

    hidden: set[Path] = set()
    for md in root.rglob("*.md"):
        if md.name in {"index.md", "log.md"}:
            continue
        fm, _ = split(md)
        if fm and fm.get("type") and fm.get("x-brand-visibility", default) != "public":
            hidden.add(md.resolve())

    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(root, out, ignore=shutil.ignore_patterns(".*", "log.md"))
    for path in hidden:
        (out / path.relative_to(root)).unlink()

    def points_to_hidden(md_out: Path, target: str) -> bool:
        if not is_local(target):
            return False
        resolved = (md_out.parent / target.split("#")[0]).resolve()
        return out in resolved.parents and (root / resolved.relative_to(out)).resolve() in hidden

    for md in out.rglob("*.md"):
        lines = md.read_text(encoding="utf-8").splitlines(keepends=True)
        kept = []
        for line in lines:
            links = LINK_RE.findall(line)
            hidden_links = [t for _, t in links if points_to_hidden(md, t)]
            if hidden_links and LIST_ITEM_RE.match(line) and len(hidden_links) == len(links):
                continue
            if hidden_links:
                line = LINK_RE.sub(lambda m: m.group(1) if points_to_hidden(md, m.group(2)) else m.group(0), line)
            kept.append(line)
        md.write_text("".join(kept), encoding="utf-8")

    removed_tokens = 0
    token_ref = (meta or {}).get("x-brand-tokens")
    if token_ref and (out / str(token_ref)).exists():
        token_file = out / str(token_ref)
        data, removed_tokens = filter_tokens(json.loads(token_file.read_text(encoding="utf-8")))
        token_file.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    return sorted(hidden), removed_tokens


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    root, out = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    if out == root or root in out.parents:
        print("error: OUT_DIR must be outside the bundle", file=sys.stderr)
        return 2
    hidden, removed_tokens = export(root, out)
    for path in hidden:
        print(f"left out  {path.relative_to(root)}")
    print(f"left out  log.md files, {removed_tokens} non-public token(s)")
    print(f"public bundle written to {out}. Read it before you share it.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
