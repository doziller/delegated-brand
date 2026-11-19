#!/usr/bin/env python3
"""Approve a brand rule and bind the approval to its current content.

Adds a verified entry with the actor, the time and a content hash
(x-brand-hash), and sets status: stable. If anyone later changes the rule's
text or fields, check_bundle.py finds that the hash no longer matches and
fails until someone approves again.

Run it only as the person (or process, for limits) who approves. Who may
approve which files is enforced on GitHub with CODEOWNERS and branch
protection, not by this script.

Usage:
    approve.py RULE_FILE --by human:<id> [--at 2026-11-19T12:00:00Z]
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brandlib import content_hash, split  # noqa: E402

ACTOR_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:\S+$")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("rule", type=Path)
    parser.add_argument("--by", required=True, help='actor, e.g. "human:jane-doe"')
    parser.add_argument("--at", help="RFC 3339 time; default: now (UTC)")
    args = parser.parse_args()

    if not ACTOR_RE.match(args.by):
        print("error: --by must be an actor such as human:jane-doe", file=sys.stderr)
        return 2
    meta, _ = split(args.rule)
    if not meta or not meta.get("type"):
        print(f"error: {args.rule} is not a rule (no frontmatter with type)", file=sys.stderr)
        return 2
    if isinstance(meta.get("verified"), dict):
        print("error: write verified as a list (one '- {...}' line per entry) before approving", file=sys.stderr)
        return 2

    at = args.at or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    entry = f'  - {{ by: "{args.by}", at: "{at}", x-brand-hash: "{content_hash(args.rule)}" }}\n'

    text = args.rule.read_text(encoding="utf-8")
    end = text.find("\n---", 4)
    head, rest = text[: end + 1], text[end + 1:]
    lines = head.splitlines(keepends=True)

    if any(line.startswith("verified:") for line in lines):
        i = next(i for i, line in enumerate(lines) if line.startswith("verified:")) + 1
        while i < len(lines) and lines[i].startswith("  - "):
            i += 1
        lines.insert(i, entry)
    else:
        lines.append("verified:\n")
        lines.append(entry)

    if any(line.startswith("status:") for line in lines):
        lines = [("status: stable\n" if line.startswith("status:") else line) for line in lines]
    else:
        lines.append("status: stable\n")

    args.rule.write_text("".join(lines) + rest, encoding="utf-8")
    print(f"approved {args.rule} by {args.by} at {at}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
