#!/usr/bin/env python3
"""Export the public part of a brand bundle.

Copies BUNDLE_ROOT to OUT_DIR and leaves out every concept whose visibility
is internal or restricted (x-brand-visibility, or x-brand-visibility-default
in the bundle-root index.md). Lines in index.md files that link to a left-out
concept are removed. In other files the link text stays and the link goes,
so the public bundle has no dangling links.

Use it to hand the bundle to partners, agencies or public agents.

Usage:
    export_public.py BUNDLE_ROOT OUT_DIR
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("export_public.py needs PyYAML: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

LINK_RE = re.compile(r"\]\(([^)\s]+)\)")


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    data = yaml.safe_load(text[4:end]) if end != -1 else None
    return data if isinstance(data, dict) else {}


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    root, out = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    if out == root or root in out.parents:
        print("error: OUT_DIR must be outside the bundle", file=sys.stderr)
        return 2
    default = frontmatter(root / "index.md").get("x-brand-visibility-default", "public")

    hidden: set[Path] = set()
    for md in root.rglob("*.md"):
        if md.name in {"index.md", "log.md"}:
            continue
        fm = frontmatter(md)
        if fm.get("type") and fm.get("x-brand-visibility", default) != "public":
            hidden.add(md)

    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(root, out, ignore=shutil.ignore_patterns(".*"))
    for path in hidden:
        (out / path.relative_to(root)).unlink()

    for index in out.rglob("index.md"):
        kept = []
        for line in index.read_text(encoding="utf-8").splitlines(keepends=True):
            targets = [(index.parent / t.split("#")[0]).resolve() for t in LINK_RE.findall(line)
                       if not t.startswith(("http", "#", "mailto"))]
            source_targets = {root / t.relative_to(out) for t in targets if out in t.parents}
            if not source_targets & hidden:
                kept.append(line)
        index.write_text("".join(kept), encoding="utf-8")

    # In other files, keep the link text but drop links to left-out concepts.
    full_link = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
    for md in out.rglob("*.md"):
        if md.name == "index.md":
            continue
        text = md.read_text(encoding="utf-8")

        def unlink(match: re.Match) -> str:
            label, target = match.group(1), match.group(2)
            if target.startswith(("http", "#", "mailto")):
                return match.group(0)
            resolved = (md.parent / target.split("#")[0]).resolve()
            if out in resolved.parents and root / resolved.relative_to(out) in hidden:
                return label
            return match.group(0)

        new = full_link.sub(unlink, text)
        if new != text:
            md.write_text(new, encoding="utf-8")

    for path in sorted(hidden):
        print(f"left out  {path.relative_to(root)}")
    print(f"public bundle written to {out} ({len(hidden)} concept(s) left out)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
