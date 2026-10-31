#!/usr/bin/env python3
"""lab: scaffold and check rounds of the AI Collaborative Laboratory.

Python 3.11+, standard library only.

    lab.py new-round FIELD... [--mode race|swap|duel]
    lab.py status
    lab.py check [N]
    lab.py advance [N]

`check` validates what the current phase must deliver. `advance` runs `check`
and, only if it passes, moves the round to the next phase.
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import os
import re
import shutil
import sys
import tomllib
from pathlib import Path
from string import Template

PHASES = ("claim", "challenge", "proof", "verdict", "done")
MODES = ("race", "swap", "duel")
CHANNELS = ("papers", "code", "products", "patents")
IDEA_HEADINGS = (
    "## The claim",
    "## Who needs it, and why now",
    "## How it works",
    "## Nearest neighbours",
    "## Proof plan (pre-registered)",
    "## Risks and kill criteria",
)
MIN_LONGLIST = 8
MIN_NEIGHBOURS = 3
VERIFY_STUB = "verify.sh not written yet"

PLACEHOLDER = re.compile(r"\{\{.*?\}\}")
LIST_ITEM = re.compile(r"^[ \t]*(?:[-*]|\d+[.)])[ \t]+\S", re.M)
THREAD_ENTRY = re.compile(
    r"^### \d+ · (?P<author>[\w.-]+) · (?P<role>Proposer|Challenger|Synthesizer)[ \t]*$",
    re.M,
)
TICKED = re.compile(r"^- \[[xX]\]", re.M)
SEPARATOR_ROW = re.compile(r"^\|[\s:|-]+\|$")


class LabError(Exception):
    """A problem the user can fix; reported without a traceback."""


# ── small helpers ──────────────────────────────────────────────────────


def sections(text: str) -> dict[str, str]:
    """Split markdown into {'## Heading': body} on level-2 headings."""
    found: dict[str, list[str]] = {}
    current = None
    for line in text.splitlines():
        if line.startswith("## "):
            current = line.strip()
            found[current] = []
        elif current is not None:
            found[current].append(line)
    return {k: "\n".join(v) for k, v in found.items()}


def table_rows(block: str) -> list[list[str]]:
    """Data rows of the first markdown table in `block` (header and rule dropped)."""
    rows: list[list[str]] = []
    for raw in block.splitlines():
        line = raw.strip()
        if not line.startswith("|") or SEPARATOR_ROW.match(line):
            continue
        inner = line[1:-1] if line.endswith("|") else line[1:]
        rows.append([cell.strip() for cell in inner.split("|")])
    return rows[1:]


def complete(rows: list[list[str]], width: int) -> list[list[str]]:
    return [r for r in rows if len(r) >= width and all(r[:width])]


# ── the lab ────────────────────────────────────────────────────────────


class Lab:
    def __init__(self, root: Path):
        self.root = Path(root)
        roster_path = self.root / "roster.toml"
        if not roster_path.exists():
            raise LabError(f"no roster.toml in {self.root}")
        self.roster = tomllib.loads(roster_path.read_text(encoding="utf-8"))
        self.teams: dict[str, dict] = self.roster["teams"]
        if len(self.teams) != 2:
            raise LabError("roster.toml must define exactly two teams")
        for key, team in self.teams.items():
            if len(team["members"]) != 2:
                raise LabError(f"team {key} must have exactly two members")

    # paths

    def rel(self, path: Path) -> str:
        return str(Path(path).relative_to(self.root))

    def rounds_dir(self) -> Path:
        return self.root / "arena" / "rounds"

    def round_dir(self, n: int) -> Path:
        return self.rounds_dir() / f"{n:03d}"

    def rubric_path(self) -> Path:
        return self.root / self.roster["lab"]["rubric"]

    def rubric_hash(self) -> str:
        return hashlib.sha256(self.rubric_path().read_bytes()).hexdigest()

    def other(self, team: str) -> str:
        return next(k for k in self.teams if k != team)

    # rounds

    def round_numbers(self) -> list[int]:
        base = self.rounds_dir()
        if not base.exists():
            return []
        return sorted(int(p.name) for p in base.iterdir() if re.fullmatch(r"\d{3}", p.name))

    def resolve(self, n: int | None) -> int:
        numbers = self.round_numbers()
        if n is None:
            if not numbers:
                raise LabError("no rounds yet. Start one with: lab.py new-round FIELD")
            return numbers[-1]
        if n not in numbers:
            raise LabError(f"round {n:03d} does not exist")
        return n

    def load_round(self, n: int) -> dict:
        path = self.round_dir(n) / "round.toml"
        return tomllib.loads(path.read_text(encoding="utf-8"))

    # templates

    def render(self, template: str, dest: Path, ctx: dict[str, str]) -> None:
        source = self.root / "templates" / template
        if not source.exists():
            raise LabError(f"missing template: templates/{template}")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(Template(source.read_text(encoding="utf-8")).safe_substitute(ctx), encoding="utf-8")

    # commands

    def new_round(self, field: str, mode: str = "race") -> int:
        if mode not in MODES:
            raise LabError(f"mode must be one of {', '.join(MODES)}")
        if not field.strip():
            raise LabError("a round needs a field, even if it is 'open field'")
        numbers = self.round_numbers()
        n = (numbers[-1] if numbers else 0) + 1
        num, rid, today = f"{n:03d}", f"r{n:03d}", datetime.date.today().isoformat()
        rd = self.round_dir(n)
        (rd / "challenges").mkdir(parents=True)
        (rd / "reviews").mkdir()

        (rd / "round.toml").write_text(
            f'number = {n}\n'
            f'field = {json.dumps(field, ensure_ascii=False)}\n'
            f'mode = "{mode}"\n'
            f'phase = "claim"\n'
            f'created = "{today}"\n'
            f'rubric_sha256 = "{self.rubric_hash()}"\n'
            f'\n'
            f'# Subscriptions meter usage in windows, not dollars.\n'
            f'# Budget is in sessions per model, per phase.\n'
            f'[budget]\n'
            f'claim_sessions = 4\n'
            f'challenge_sessions = 1\n'
            f'proof_sessions = 6\n'
            f'verdict_sessions = 1\n',
            encoding="utf-8",
        )

        base_ctx = {"round": num, "rid": rid, "field": field, "mode": mode, "date": today}
        for key, team in self.teams.items():
            members = team["members"]
            ids = [m["id"] for m in members]
            ctx = {
                **base_ctx,
                "team": key,
                "team_title": team["title"],
                "target_team": self.other(key),
                "member_ids": ", ".join(ids),
                "member1": ids[0],
                "member2": ids[1],
            }
            folder = self.root / team["folder"]
            ideas = folder / "ideas" / rid
            for m in members:
                self.render("longlist.md", ideas / f"longlist-{m['id']}.md",
                            {**ctx, "member_id": m["id"], "member_display": m["display"]})
            for name in ("idea-card.md", "prior-art.md", "thread.md"):
                self.render(name, ideas / "entry" / name, ctx)
            (ideas / "shelved").mkdir(parents=True, exist_ok=True)
            (ideas / "shelved" / ".gitkeep").touch()

            builds = folder / "builds" / rid
            self.render("build-readme.md", builds / "README.md", ctx)
            verify = builds / "verify.sh"
            shutil.copyfile(self.root / "templates" / "verify.sh", verify)
            verify.chmod(verify.stat().st_mode | 0o755)

            self.render("challenge.md", rd / "challenges" / f"{key}.md", ctx)
            self.render("review.md", rd / "reviews" / f"{key}.md", ctx)

        self.render("verdict.md", rd / "verdict.md", base_ctx)
        self.render("retro.md", rd / "retro.md", base_ctx)

        keys = list(self.teams)
        print(f"Round {num} scaffolded. Phase: claim. Mode: {mode}. Field: {field}")
        print("\nCommit the scaffold, then give each team a sealed branch:")
        print(f"  git add -A && git commit -m 'Round {num}: scaffold'")
        for k in keys:
            print(f"  git branch {rid}/{k}")
        print("\nEach team works only on its own branch. Longlists first, written apart.")
        return n

    def status(self) -> None:
        numbers = self.round_numbers()
        if not numbers:
            print("No rounds yet. Start one: lab.py new-round \"open field\"")
        else:
            print(f"{'Round':<7}{'Phase':<11}{'Mode':<7}Field")
            for n in numbers:
                info = self.load_round(n)
                print(f"{n:03d}    {info['phase']:<11}{info['mode']:<7}{info['field']}")
        warnings = [
            f"roster: {m['id']} has no model id yet. Fill it in: roster.toml"
            for team in self.teams.values()
            for m in team["members"]
            if m.get("model", "TODO") == "TODO"
        ]
        if warnings:
            print()
            print("\n".join(warnings))

    # checks

    def _read(self, path: Path, errs: list[str]) -> str | None:
        if not path.exists():
            errs.append(f"missing: {self.rel(path)}")
            return None
        return path.read_text(encoding="utf-8")

    def _filled(self, path: Path, text: str, errs: list[str]) -> bool:
        left = PLACEHOLDER.findall(text)
        if left:
            errs.append(f"{self.rel(path)}: {len(left)} unfilled placeholder(s), first: {left[0]}")
        return not left

    def check(self, n: int) -> list[str]:
        info = self.load_round(n)
        phase = info["phase"]
        rid = f"r{n:03d}"
        rd = self.round_dir(n)
        errs: list[str] = []

        if info.get("rubric_sha256") != self.rubric_hash():
            errs.append(f"{self.rel(self.rubric_path())} changed since the round started")

        for key, team in self.teams.items():
            folder = self.root / team["folder"]
            ids = [m["id"] for m in team["members"]]

            if phase == "claim":
                base = folder / "ideas" / rid
                for mid in ids:
                    self._check_longlist(base / f"longlist-{mid}.md", errs)
                self._check_idea_card(base / "entry" / "idea-card.md", errs)
                self._check_prior_art(base / "entry" / "prior-art.md", errs)
                self._check_thread(base / "entry" / "thread.md", ids, errs)

            elif phase == "challenge":
                self._check_challenge(rd / "challenges" / f"{key}.md", errs)

            elif phase == "proof":
                self._check_build(folder / "builds" / rid, errs)

            elif phase == "verdict":
                path = rd / "reviews" / f"{key}.md"
                text = self._read(path, errs)
                if text is not None:
                    self._filled(path, text, errs)

        if phase == "verdict":
            for name in ("verdict.md", "retro.md"):
                path = rd / name
                text = self._read(path, errs)
                if text is not None:
                    self._filled(path, text, errs)
        return errs

    def _check_longlist(self, path: Path, errs: list[str]) -> None:
        text = self._read(path, errs)
        if text is None or not self._filled(path, text, errs):
            return
        count = len(LIST_ITEM.findall(text))
        if count < MIN_LONGLIST:
            errs.append(f"{self.rel(path)}: {count} claim(s), need at least {MIN_LONGLIST}")

    def _check_idea_card(self, path: Path, errs: list[str]) -> None:
        text = self._read(path, errs)
        if text is None:
            return
        self._filled(path, text, errs)
        for heading in IDEA_HEADINGS:
            if not re.search(rf"^{re.escape(heading)}[ \t]*$", text, re.M):
                errs.append(f"{self.rel(path)}: missing section '{heading}'")
        block = sections(text).get("## Nearest neighbours", "")
        have = len(complete(table_rows(block), 4))
        if have < MIN_NEIGHBOURS:
            errs.append(f"{self.rel(path)}: {have} complete nearest neighbour(s), need at least {MIN_NEIGHBOURS}")

    def _check_prior_art(self, path: Path, errs: list[str]) -> None:
        text = self._read(path, errs)
        if text is None:
            return
        self._filled(path, text, errs)
        covered = {r[1].lower() for r in complete(table_rows(text), 5)}
        missing = [c for c in CHANNELS if c not in covered]
        if missing:
            errs.append(f"{self.rel(path)}: no complete row for channel(s): {', '.join(missing)}")

    def _check_thread(self, path: Path, member_ids: list[str], errs: list[str]) -> None:
        text = self._read(path, errs)
        if text is None:
            return
        self._filled(path, text, errs)
        entries = list(THREAD_ENTRY.finditer(text))
        authors = {m["author"] for m in entries}
        unknown = authors - set(member_ids)
        if unknown:
            errs.append(f"{self.rel(path)}: entries signed by non-members: {', '.join(sorted(unknown))}")
        if len(authors & set(member_ids)) < 2:
            errs.append(f"{self.rel(path)}: both team members must sign at least one entry")
        attacked = False
        for i, m in enumerate(entries):
            end = entries[i + 1].start() if i + 1 < len(entries) else len(text)
            if m["role"] == "Challenger" and "Strongest case against" in text[m.end():end]:
                attacked = True
        if not attacked:
            errs.append(f"{self.rel(path)}: needs a Challenger entry with a 'Strongest case against'")

    def _check_challenge(self, path: Path, errs: list[str]) -> None:
        text = self._read(path, errs)
        if text is None:
            return
        self._filled(path, text, errs)
        ticked = len(TICKED.findall(text))
        if ticked != 1:
            errs.append(f"{self.rel(path)}: tick exactly one result (found {ticked})")

    def _check_build(self, build: Path, errs: list[str]) -> None:
        readme = build / "README.md"
        text = self._read(readme, errs)
        if text is not None:
            self._filled(readme, text, errs)
        verify = build / "verify.sh"
        script = self._read(verify, errs)
        if script is None:
            return
        if VERIFY_STUB in script:
            errs.append(f"{self.rel(verify)}: still the stub")
        if not os.access(verify, os.X_OK):
            errs.append(f"{self.rel(verify)}: not executable (chmod +x)")

    def advance(self, n: int) -> list[str]:
        info = self.load_round(n)
        phase = info["phase"]
        if phase == "done":
            raise LabError(f"round {n:03d} is already done")
        errs = self.check(n)
        if errs:
            return errs
        nxt = PHASES[PHASES.index(phase) + 1]
        path = self.round_dir(n) / "round.toml"
        text = path.read_text(encoding="utf-8")
        path.write_text(re.sub(r'^phase = ".*"$', f'phase = "{nxt}"', text, count=1, flags=re.M), encoding="utf-8")
        print(f"Round {n:03d}: {phase} -> {nxt}")
        self._hints(n, phase, nxt)
        return []

    def _hints(self, n: int, old: str, new: str) -> None:
        rid = f"r{n:03d}"
        keys = list(self.teams)
        if old in ("claim", "proof"):
            kind = old
            print(f"\nSeal each team's work, then open it:")
            for k in keys:
                print(f"  git tag {rid}-{kind}-{k} {rid}/{k}")
            branches = " ".join(f"{rid}/{k}" for k in keys)
            print(f"  git checkout main && git merge --no-ff {branches}")
        if new == "challenge":
            print("\nEach team now reads the other's entry and fills in its challenge file.")
        elif new == "proof":
            print(f"\nTeams return to their own branches ({', '.join(f'{rid}/{k}' for k in keys)}) and build apart.")
        elif new == "verdict":
            print("\nReferee: label the two builds X and Y by coin flip. Each team then fills in its review.")
        elif new == "done":
            print("\nUpdate arena/SCOREBOARD.md, then:  git tag " + f"{rid}-done")


# ── command line ───────────────────────────────────────────────────────


def main(argv: list[str] | None = None, root: Path | None = None) -> int:
    parser = argparse.ArgumentParser(prog="lab.py", description="Scaffold and check rounds of the lab.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_new = sub.add_parser("new-round", help="scaffold the next round")
    p_new.add_argument("field", nargs="+", help='what the round is about, e.g. "open field"')
    p_new.add_argument("--mode", default="race", choices=MODES)

    sub.add_parser("status", help="show every round and its phase")
    for name, text in (("check", "validate the current phase"), ("advance", "check, then move to the next phase")):
        p = sub.add_parser(name, help=text)
        p.add_argument("round", nargs="?", type=int, help="round number (default: latest)")

    args = parser.parse_args(argv)
    try:
        lab = Lab(root or Path(__file__).resolve().parent.parent)
        if args.command == "new-round":
            lab.new_round(" ".join(args.field), args.mode)
        elif args.command == "status":
            lab.status()
        else:
            n = lab.resolve(args.round)
            if args.command == "check":
                errs = lab.check(n)
                phase = lab.load_round(n)["phase"]
                if errs:
                    print(f"Round {n:03d}, phase {phase}: not ready.\n")
                    print("\n".join(f"  - {e}" for e in errs))
                    return 1
                print(f"Round {n:03d}, phase {phase}: ready to advance.")
            else:
                errs = lab.advance(n)
                if errs:
                    print(f"Round {n:03d}: cannot advance yet.\n")
                    print("\n".join(f"  - {e}" for e in errs))
                    return 1
    except LabError as exc:
        print(f"lab: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
