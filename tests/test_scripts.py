"""Regression tests for the bundle scripts. Run: python -m unittest discover tests"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

from check_bundle import check  # noqa: E402
from export_public import export  # noqa: E402


def copy_example(tmp: Path) -> Path:
    target = tmp / "example"
    shutil.copytree(REPO / "example", target)
    return target


def edit(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    assert old in text, f"{old!r} not in {path}"
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


class CheckBundle(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.bundle = copy_example(self.tmp)

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def errors(self):
        return check(self.bundle.resolve())[0]

    def test_example_and_template_pass(self):
        self.assertEqual(self.errors(), [])
        self.assertEqual(check((REPO / "bundle").resolve())[0], [])

    def test_changed_approved_rule_fails(self):
        edit(self.bundle / "glossary/color/brass.md", "Never as a background.", "Fine as a background.")
        self.assertTrue(any("content hash differs" in e for e in self.errors()))

    def test_changed_frontmatter_fails(self):
        edit(self.bundle / "glossary/color/brass.md", "x-brand-rule-type: limit", "x-brand-rule-type: preference")
        self.assertTrue(any("brass.md" in e for e in self.errors()))

    def test_regenerated_after_approval_fails(self):
        edit(self.bundle / "glossary/color/paper.md",
             'generated: { by: "human:tobias-renner", at: "2026-10-20T09:15:00Z" }',
             'generated: { by: "hessling-quote-assistant/v2", at: "2026-11-12T08:15:00Z" }')
        self.assertTrue(any("regenerated after its latest approval" in e for e in self.errors()))

    def test_reapproval_restores_pass(self):
        rule = self.bundle / "glossary/color/brass.md"
        edit(rule, "Never as a background.", "Never as a page background.")
        subprocess.run([sys.executable, str(REPO / "scripts/approve.py"), str(rule),
                        "--by", "human:anna-hessling", "--at", "2026-11-19T12:00:00Z"], check=True,
                       capture_output=True)
        self.assertEqual(self.errors(), [])

    def test_primitive_token_reference_fails(self):
        edit(self.bundle / "glossary/type/headline.md", "x-brand-token: font.headline",
             "x-brand-token: primitive.color.brass-500")
        self.assertTrue(any("is a primitive" in e for e in self.errors()))

    def test_missing_token_fails(self):
        edit(self.bundle / "glossary/type/headline.md", "x-brand-token: font.headline", "x-brand-token: font.missing")
        self.assertTrue(any("does not exist" in e for e in self.errors()))

    def test_derived_with_rule_type_fails(self):
        edit(self.bundle / "signals/dealer-survey.md", "x-brand-knowledge: derived",
             "x-brand-knowledge: derived\nx-brand-rule-type: principle")
        self.assertTrue(any("derived knowledge" in e for e in self.errors()))

    def test_bad_owner_fails(self):
        edit(self.bundle / "glossary/voice/trade-voice.md", 'x-brand-owner: "human:lars-becker"', 'x-brand-owner: "lars"')
        self.assertTrue(any("x-brand-owner" in e for e in self.errors()))

    def test_bad_vocabulary_fails(self):
        edit(self.bundle / "glossary/imagery/workshop-light.md", "x-brand-rule-type: preference",
             "x-brand-rule-type: maybe")
        self.assertTrue(any("x-brand-rule-type" in e for e in self.errors()))


class ExportPublic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp())
        cls.out = cls.tmp / "public"
        cls.hidden, cls.removed_tokens = export((REPO / "example").resolve(), cls.out)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp)

    def test_internal_concept_left_out(self):
        self.assertFalse((self.out / "glossary/principles/who-decides.md").exists())
        self.assertTrue((self.out / "glossary/principles/exact-over-warm.md").exists())

    def test_no_links_to_left_out_concepts(self):
        for md in self.out.rglob("*.md"):
            self.assertNotIn("who-decides.md", md.read_text(encoding="utf-8"), md)

    def test_table_row_keeps_public_content(self):
        index = (self.out / "index.md").read_text(encoding="utf-8")
        self.assertIn("A quote, order, payment or warranty action", index)
        self.assertIn("when-no-one-answers.md", index)

    def test_logs_left_out(self):
        self.assertEqual(list(self.out.rglob("log.md")), [])

    def test_internal_tokens_left_out(self):
        tokens = json.loads((self.out / "tokens.json").read_text(encoding="utf-8"))
        self.assertNotIn("brand-accent-proposal", tokens["color"])
        self.assertIn("brand-accent", tokens["color"])
        self.assertGreaterEqual(self.removed_tokens, 1)

    def test_export_still_passes_check(self):
        self.assertEqual(check(self.out.resolve())[0], [])


if __name__ == "__main__":
    unittest.main()
