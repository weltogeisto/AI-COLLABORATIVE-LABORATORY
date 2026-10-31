"""Tests for tools/lab.py. Run: python3 -m unittest discover -s tests"""

from __future__ import annotations

import contextlib
import io
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "tools"))

import lab  # noqa: E402

TEAMS = {
    "sonnet-soul": ("team-sonnet-soul", ["sonnet-5-5", "gpt-6-1-soul"]),
    "opus-astra": ("team-opus-astra", ["opus-5-5", "gpt-6-astra"]),
}

IDEA_CARD = """---
id: r001-x-01
---

# A thing

## The claim

Nobody has built X that does Y.

## Who needs it, and why now

Someone, today.

## How it works

Like this.

## Nearest neighbours

| What exists | Link | What it does | Delta |
|---|---|---|---|
| A | https://a.example | does a | not b |
| B | https://b.example | does b | not c |
| C | https://c.example | does c | not d |

## Proof plan (pre-registered)

- It works if: the demo runs.

## Risks and kill criteria

None worth naming.
"""

PRIOR_ART = """# Prior-art search

| Date | Channel | Query | Best hit (URL) | Covers the claim? |
|---|---|---|---|---|
| 2026-10-31 | papers | q1 | none | no |
| 2026-10-31 | code | q2 | https://x.example | partly |
| 2026-10-31 | products | q3 | none | no |
| 2026-10-31 | patents | q4 | none | no |
"""


def thread(a: str, b: str) -> str:
    return (
        f"# Thread\n\n### 1 · {a} · Proposer\n\nHere is the claim.\n\n"
        f"### 2 · {b} · Challenger\n\n**Strongest case against:** it may exist.\n"
    )


def run(*argv: str, root: Path) -> tuple[int, str]:
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = lab.main(list(argv), root=root)
    return code, out.getvalue() + err.getvalue()


class LabTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        shutil.copy(REPO / "roster.toml", self.root / "roster.toml")
        (self.root / "arena").mkdir()
        shutil.copy(REPO / "arena" / "RUBRIC.md", self.root / "arena" / "RUBRIC.md")
        shutil.copytree(REPO / "templates", self.root / "templates")
        self.lab = lab.Lab(self.root)

    def tearDown(self):
        self._tmp.cleanup()

    # helpers

    def new_round(self) -> int:
        code, _ = run("new-round", "open", "field", root=self.root)
        self.assertEqual(code, 0)
        return 1

    def fill_claim(self, n: int = 1, team: str | None = None):
        for key, (folder, ids) in TEAMS.items():
            if team and key != team:
                continue
            base = self.root / folder / "ideas" / f"r{n:03d}"
            for mid in ids:
                (base / f"longlist-{mid}.md").write_text(
                    "# Longlist\n\n" + "".join(f"{i}. Nobody has done thing {i}.\n" for i in range(1, 9))
                )
            (base / "entry" / "idea-card.md").write_text(IDEA_CARD)
            (base / "entry" / "prior-art.md").write_text(PRIOR_ART)
            (base / "entry" / "thread.md").write_text(thread(*ids))

    def fill_challenge(self, n: int = 1):
        for key in TEAMS:
            (self.root / "arena" / "rounds" / f"{n:03d}" / "challenges" / f"{key}.md").write_text(
                "# Challenge\n\n- [ ] **Prior art found.**\n- [x] **No prior art found.**\n"
            )

    def fill_proof(self, n: int = 1):
        for folder, _ in TEAMS.values():
            build = self.root / folder / "builds" / f"r{n:03d}"
            (build / "README.md").write_text("# Build\n\nIt works.\n")
            verify = build / "verify.sh"
            verify.write_text("#!/usr/bin/env sh\nexit 0\n")
            verify.chmod(0o755)

    def fill_verdict(self, n: int = 1):
        rd = self.root / "arena" / "rounds" / f"{n:03d}"
        for key in TEAMS:
            (rd / "reviews" / f"{key}.md").write_text("# Review\n\nDone.\n")
        (rd / "verdict.md").write_text("# Verdict\n\nDone.\n")
        (rd / "retro.md").write_text("# Retro\n\nDone.\n")

    # scaffolding

    def test_new_round_scaffolds_both_teams(self):
        n = self.new_round()
        info = self.lab.load_round(n)
        self.assertEqual(info["phase"], "claim")
        self.assertEqual(info["mode"], "race")
        self.assertEqual(info["field"], "open field")
        self.assertEqual(info["rubric_sha256"], self.lab.rubric_hash())
        for folder, ids in TEAMS.values():
            base = self.root / folder / "ideas" / "r001"
            for mid in ids:
                self.assertTrue((base / f"longlist-{mid}.md").exists())
            for name in ("idea-card.md", "prior-art.md", "thread.md"):
                self.assertTrue((base / "entry" / name).exists())
            self.assertTrue((self.root / folder / "builds" / "r001" / "verify.sh").exists())
        rd = self.root / "arena" / "rounds" / "001"
        for name in ("challenges/sonnet-soul.md", "reviews/opus-astra.md", "verdict.md", "retro.md"):
            self.assertTrue((rd / name).exists(), name)

    def test_rounds_number_up(self):
        self.new_round()
        code, _ = run("new-round", "second", root=self.root)
        self.assertEqual(code, 0)
        self.assertEqual(self.lab.round_numbers(), [1, 2])

    def test_bad_mode_is_rejected(self):
        with self.assertRaises(SystemExit):
            run("new-round", "x", "--mode", "brawl", root=self.root)

    # claim phase

    def test_fresh_round_is_not_ready(self):
        n = self.new_round()
        errs = self.lab.check(n)
        self.assertTrue(any("unfilled placeholder" in e for e in errs))
        code, out = run("check", root=self.root)
        self.assertEqual(code, 1)
        self.assertIn("not ready", out)

    def test_filled_claim_passes(self):
        n = self.new_round()
        self.fill_claim(n)
        self.assertEqual(self.lab.check(n), [])

    def test_short_longlist_fails(self):
        n = self.new_round()
        self.fill_claim(n)
        path = self.root / "team-sonnet-soul" / "ideas" / "r001" / "longlist-sonnet-5-5.md"
        path.write_text("# Longlist\n\n1. one\n2. two\n")
        self.assertTrue(any("need at least 8" in e for e in self.lab.check(n)))

    def test_missing_channel_fails(self):
        n = self.new_round()
        self.fill_claim(n)
        path = self.root / "team-opus-astra" / "ideas" / "r001" / "entry" / "prior-art.md"
        path.write_text(PRIOR_ART.replace("| 2026-10-31 | patents | q4 | none | no |\n", ""))
        self.assertTrue(any("patents" in e for e in self.lab.check(n)))

    def test_too_few_neighbours_fails(self):
        n = self.new_round()
        self.fill_claim(n)
        path = self.root / "team-opus-astra" / "ideas" / "r001" / "entry" / "idea-card.md"
        path.write_text(IDEA_CARD.replace("| C | https://c.example | does c | not d |\n", ""))
        self.assertTrue(any("nearest neighbour" in e for e in self.lab.check(n)))

    def test_thread_needs_both_members_and_an_attack(self):
        n = self.new_round()
        self.fill_claim(n)
        path = self.root / "team-sonnet-soul" / "ideas" / "r001" / "entry" / "thread.md"
        path.write_text("# Thread\n\n### 1 · sonnet-5-5 · Proposer\n\nAll good.\n")
        errs = self.lab.check(n)
        self.assertTrue(any("both team members" in e for e in errs))
        self.assertTrue(any("Strongest case against" in e for e in errs))

    def test_thread_rejects_impostors(self):
        n = self.new_round()
        self.fill_claim(n)
        path = self.root / "team-sonnet-soul" / "ideas" / "r001" / "entry" / "thread.md"
        path.write_text(thread("sonnet-5-5", "opus-5-5"))
        self.assertTrue(any("non-members" in e for e in self.lab.check(n)))

    def test_rubric_change_mid_round_fails(self):
        n = self.new_round()
        self.fill_claim(n)
        with (self.root / "arena" / "RUBRIC.md").open("a") as f:
            f.write("\nQuietly changed.\n")
        self.assertTrue(any("RUBRIC.md changed" in e for e in self.lab.check(n)))

    # phase gates

    def test_advance_blocks_until_ready(self):
        n = self.new_round()
        code, _ = run("advance", root=self.root)
        self.assertEqual(code, 1)
        self.assertEqual(self.lab.load_round(n)["phase"], "claim")

    def test_challenge_needs_exactly_one_tick(self):
        n = self.new_round()
        self.fill_claim(n)
        self.assertEqual(run("advance", root=self.root)[0], 0)
        self.fill_challenge(n)
        path = self.root / "arena" / "rounds" / "001" / "challenges" / "opus-astra.md"
        path.write_text("# Challenge\n\n- [ ] one\n- [ ] two\n")
        self.assertTrue(any("tick exactly one" in e for e in self.lab.check(n)))

    def test_proof_rejects_stub_and_non_executable(self):
        n = self.new_round()
        self.fill_claim(n)
        run("advance", root=self.root)
        self.fill_challenge(n)
        run("advance", root=self.root)
        self.assertEqual(self.lab.load_round(n)["phase"], "proof")
        errs = self.lab.check(n)
        self.assertTrue(any("still the stub" in e for e in errs))
        self.fill_proof(n)
        self.assertEqual(self.lab.check(n), [])
        verify = self.root / "team-opus-astra" / "builds" / "r001" / "verify.sh"
        verify.chmod(0o644)
        self.assertTrue(any("not executable" in e for e in self.lab.check(n)))

    def test_full_round_reaches_done(self):
        n = self.new_round()
        self.fill_claim(n)
        self.assertEqual(run("advance", root=self.root)[0], 0)
        self.fill_challenge(n)
        self.assertEqual(run("advance", root=self.root)[0], 0)
        self.fill_proof(n)
        self.assertEqual(run("advance", root=self.root)[0], 0)
        self.assertEqual(self.lab.load_round(n)["phase"], "verdict")
        self.assertEqual(run("advance", root=self.root)[0], 1)
        self.fill_verdict(n)
        code, out = run("advance", root=self.root)
        self.assertEqual(code, 0)
        self.assertEqual(self.lab.load_round(n)["phase"], "done")
        self.assertIn("SCOREBOARD", out)
        code, out = run("advance", root=self.root)
        self.assertEqual(code, 2)
        self.assertIn("already done", out)

    # status and roster

    def test_status_before_and_after(self):
        code, out = run("status", root=self.root)
        self.assertEqual(code, 0)
        self.assertIn("No rounds yet", out)
        self.new_round()
        _, out = run("status", root=self.root)
        self.assertIn("claim", out)
        self.assertIn("open field", out)

    def test_status_flags_missing_model_ids(self):
        _, out = run("status", root=self.root)
        self.assertIn("gpt-6-1-soul has no model id yet", out)
        self.assertIn("gpt-6-astra has no model id yet", out)

    def test_check_without_rounds_is_a_clean_error(self):
        code, out = run("check", root=self.root)
        self.assertEqual(code, 2)
        self.assertIn("no rounds yet", out)


if __name__ == "__main__":
    unittest.main()
