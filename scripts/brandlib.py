"""Shared helpers for the bundle scripts."""

from __future__ import annotations

import hashlib
import json
import re
from datetime import date, datetime
from pathlib import Path

import yaml

LINK_RE = re.compile(r"\[([^\]]*)\]\([^)\s]+\)")

# Keys left out of the content hash: the approval itself and lifecycle fields
# that change when a rule is approved or scheduled for review.
HASH_EXCLUDED = {"verified", "status", "stale_after"}


def split(path: Path) -> tuple[dict | None, str]:
    """Return (frontmatter, body). Frontmatter is None if the file has none."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    data = yaml.safe_load(text[4:end])
    body = text[end + 4:]
    return (data if isinstance(data, dict) else None), body


def _plain(value):
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    if isinstance(value, dict):
        return {k: _plain(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_plain(v) for v in value]
    return value


def content_hash(path: Path) -> str:
    """SHA-256 over the rule's meaning: frontmatter without approval fields, plus the body.

    Link targets are left out (only the link text counts), so moving files or
    exporting a public copy does not invalidate an approval.
    """
    meta, body = split(path)
    kept = {k: v for k, v in (meta or {}).items() if k not in HASH_EXCLUDED}
    body = LINK_RE.sub(lambda m: m.group(1), body)
    normalized_body = "\n".join(line.rstrip() for line in body.strip().splitlines())
    payload = json.dumps(_plain(kept), sort_keys=True, ensure_ascii=False) + "\n---\n" + normalized_body
    return "sha256:" + hashlib.sha256(payload.encode("utf-8")).hexdigest()
