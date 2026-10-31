# 0001 · Private first, public by exception

**Status:** Proposed · 2026-10-31 · **Decider:** the repo owner

## Decision

Keep the lab private. Publish selectively: a winning build and its verdict, once the Challenge has cleared the idea and the repo has been scanned for secrets.

## Why

The lab produces ideas that do not exist yet. Three things follow.

- **Disclosure runs one way.** Private to public is a click. Public to private does not recall clones, forks, or search indexes.
- **Novelty is the asset.** In many patent systems, the EU's among them, a public disclosure before filing counts against novelty. If any idea might become a product or a filing, publish after advice, not before. This is not legal advice.
- **Transcripts leak.** Agent threads capture paths, snippets, and now and then a credential. Private contains the blast radius while the habits form.

## Three options

| Option | Works best when | What it costs |
|---|---|---|
| **Private lab** (recommended) | Ideas are unproven and some may become products. | No audience, no outside feedback. |
| **Public lab from day one** | The open record is the point. Nothing in it needs protecting, and visibility matters more than control. | The one-way door, and secret hygiene from the first commit. |
| **Private lab, public showcase repo** | You want both: protected work and public proof. | A second repo, and a manual publish step. |

The third option is the natural destination. It starts as the first.

## Publish checklist

Before any artifact leaves the lab:

1. The Challenge has run, and G1 passed.
2. No one has a reason to file. Ask first.
3. Secret scan over the full history, not just the tip.
4. Agent threads read through for paths, names, and tokens.
5. A licence chosen. A public repo without one is all rights reserved by default.
6. Published as a copy into the showcase repo, not by flipping the lab.

## Current state

The repo was created public and held no commits before this scaffold. The scaffold is process only: rules, templates, and tooling. No idea has been committed, so nothing needs retracting.

To go private: **Settings → General → Danger Zone → Change repository visibility.**
