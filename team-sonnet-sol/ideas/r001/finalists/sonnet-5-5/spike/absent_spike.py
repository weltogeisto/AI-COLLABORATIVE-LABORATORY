#!/usr/bin/env python3
"""Feasibility spike for "Receipts for nothing". NOT the build.

Shows that the five checks are implementable, and that a ledger-only baseline
(what receipts check today) misses most lies. The attacks are the author's own,
so this proves mechanics, not generality. Held-out attacks (criterion 5) and
replay precision/recall (criterion 4) are NOT tested here.

Stdlib only, offline, deterministic. Exit 0 if criteria 1, 2, 3 and 6 hold.
"""

import hashlib
import json
import random
import sys

CHANNELS = ["papers", "code", "products", "patents"]
WORDS = ("alpha river stone engine lamp orbit quartz maple signal harbor "
         "thread ember cipher meadow vector prism anchor ledger falcon cobalt "
         "lattice mirror tundra beacon fabric socket vellum garnet kernel "
         "summit canyon lantern oxide parcel quiver rivet saddle timber "
         "umber valley willow yarrow zenith ribbon pepper nickel mosaic").split()
GENESIS = "0" * 12
K = 3


def digest(s):
    return hashlib.sha256(s.encode()).hexdigest()[:12]


# ── corpus and source ──────────────────────────────────────────────────

def make_corpus(rng, per_channel=14):
    return [{"id": f"{ch}-{i}", "channel": ch, "text": " ".join(rng.sample(WORDS, 8))}
            for ch in CHANNELS for i in range(per_channel)]


def search(docs, channel, query, k):
    q = set(query.split())
    scored = sorted((-len(q & set(d["text"].split())), d["id"])
                    for d in docs if d["channel"] == channel and q & set(d["text"].split()))
    return [doc_id for _, doc_id in scored[:k]]


# ── the ledger: hash-chained, one entry per query, empty results included ──

def entry_hash(e):
    return digest(json.dumps({k: v for k, v in e.items() if k != "hash"}, sort_keys=True))


def record(docs, plan, k=K):
    by_id = {d["id"]: d for d in docs}
    ledger, prev = [], GENESIS
    for seq, (channel, query) in enumerate(plan):
        hits = [{"id": i, "digest": digest(by_id[i]["text"])} for i in search(docs, channel, query, k)]
        e = {"seq": seq, "channel": channel, "query": query, "k": k, "hits": hits, "prev": prev}
        e["hash"] = entry_hash(e)
        ledger.append(e)
        prev = e["hash"]
    return ledger


def honest_report(ledger):
    return {
        "claim_scope": {"channels": sorted({e["channel"] for e in ledger}), "k": min(e["k"] for e in ledger)},
        "cited": [e["seq"] for e in ledger],
        "excluded": {},
        "empty_claims": [e["seq"] for e in ledger if not e["hits"]],  # queries the report says found nothing
        "dispositions": {h["id"]: "distinct" for e in ledger for h in e["hits"]},
    }


# ── verifiers ──────────────────────────────────────────────────────────

def chain_ok(ledger):
    prev = GENESIS
    for i, e in enumerate(ledger):
        if e["seq"] != i or e["prev"] != prev or e["hash"] != entry_hash(e):
            return False
        prev = e["hash"]
    return True


def count_check(ledger, report):
    """NabaOS-style baseline: a 'found nothing' claim fails if the ledger shows hits for that query."""
    by_seq = {e["seq"]: e for e in ledger}
    return {"FALSE_EMPTY"} if any(by_seq.get(s, {}).get("hits") for s in report["empty_claims"]) else set()


def verify(ledger, report, docs_now=None, full=True):
    """Return the set of lie classes found. Empty set means the report is honest."""
    found, seqs = set(), {e["seq"] for e in ledger}
    if not chain_ok(ledger) or not set(report["cited"]) <= seqs:
        found.add("FABRICATION")
    if not full:  # the ledger-only baseline stops here
        return found
    found |= count_check(ledger, report)  # the full verifier contains the count check
    cited = [e for e in ledger if e["seq"] in set(report["cited"])]
    if {h["id"] for e in cited for h in e["hits"]} - set(report["dispositions"]):
        found.add("OMISSION")
    if seqs - set(report["cited"]) - set(report["excluded"]):
        found.add("CHERRY_PICKING")
    scope = report["claim_scope"]
    if not set(scope["channels"]) <= {e["channel"] for e in ledger} or scope["k"] > min(e["k"] for e in ledger):
        found.add("INFLATION")
    if docs_now is not None and any(
            search(docs_now, e["channel"], e["query"], e["k"]) != [h["id"] for h in e["hits"]] for e in ledger):
        found.add("STALENESS")
    return found


# ── cases ──────────────────────────────────────────────────────────────

def make_case(seed, n_channels=4):
    rng = random.Random(seed)
    docs, chans = make_corpus(rng), CHANNELS[:n_channels]
    plan = []
    for i in range(8):
        ch = chans[i % len(chans)]
        d = rng.choice([x for x in docs if x["channel"] == ch])
        plan.append((ch, " ".join(rng.sample(d["text"].split(), 3))))
    plan.append((chans[0], "zzqq nothing"))  # an honest empty result
    ledger = record(docs, plan)
    return docs, ledger, honest_report(ledger)


def attack(kind, seed):
    """Return (docs_now, ledger, report) containing exactly one kind of lie."""
    docs, ledger, report = make_case(seed, n_channels=3 if kind == "INFLATION" and seed % 2 == 0 else 4)
    rng = random.Random(seed * 7 + 1)
    docs_now = docs
    with_hits = [e for e in ledger if e["hits"]]
    if kind == "FABRICATION":
        mode = seed % 3
        if mode == 0:
            report["cited"].append(len(ledger) + 5)           # cite a query that was never run
        elif mode == 1:
            ledger[rng.randrange(len(ledger))]["query"] += " edited"  # rewrite history
        else:
            del ledger[rng.randrange(1, len(ledger) - 1)]       # drop an inconvenient entry
    elif kind == "OMISSION":
        hit = rng.choice(rng.choice(with_hits)["hits"])["id"]
        del report["dispositions"][hit]                       # never address a near-miss
    elif kind == "CHERRY_PICKING":
        hidden = rng.choice(with_hits)["seq"]
        report["cited"].remove(hidden)                        # cite only the convenient queries
    elif kind == "INFLATION":
        if seed % 2 == 0:
            report["claim_scope"]["channels"] = list(CHANNELS)  # claim a channel never searched
        else:
            report["claim_scope"]["k"] = K + 5                  # claim a depth never read
    elif kind == "STALENESS":
        e = rng.choice(with_hits)
        docs_now = docs + [{"id": "new-doc", "channel": e["channel"], "text": e["query"] + " fresh"}]
    elif kind == "FALSE_EMPTY":  # the case a count check targets: results exist, report says none
        e = rng.choice(with_hits)
        report["empty_claims"].append(e["seq"])
        for h in e["hits"]:
            report["dispositions"].pop(h["id"], None)
    return docs_now, ledger, report


def main():
    kinds = ["FABRICATION", "OMISSION", "CHERRY_PICKING", "INFLATION", "STALENESS"]
    honest_rejected = 0
    for seed in range(20):
        docs, ledger, report = make_case(seed)
        honest_rejected += bool(verify(ledger, report, docs_now=docs))
    print(f"honest reports falsely rejected: {honest_rejected} of 20")
    print(f"\n{'lie class':<16}{'caught, right class':>20}{'ledger-only':>14}{'count check':>14}")
    caught_total = ledger_total = count_total = 0
    for kind in kinds + ["FALSE_EMPTY"]:
        caught = ledger_only = count_only = 0
        for seed in range(100, 110):
            docs_now, ledger, report = attack(kind, seed)
            caught += kind in verify(ledger, report, docs_now=docs_now)
            ledger_only += bool(verify(ledger, report, full=False))
            count_only += bool(count_check(ledger, report))
        if kind == "FALSE_EMPTY":
            print("-" * 64)
            false_empty = caught
        else:
            caught_total, ledger_total, count_total = caught_total + caught, ledger_total + ledger_only, count_total + count_only
        print(f"{kind:<16}{caught:>17} /10{ledger_only:>11} /10{count_only:>11} /10")
        if kind == "STALENESS":
            print(f"{'total (5 classes)':<16}{caught_total:>14} /50{ledger_total:>11} /50{count_total:>11} /50")
    ok = (honest_rejected <= 1 and caught_total >= 48 and ledger_total <= 12 and count_total <= 12
          and false_empty >= 9)
    print(f"\ncriteria 1, 2, 3, 6: {'HOLD' if ok else 'DO NOT HOLD'}  (not tested here: 4 replay precision/recall, 5 held-out attacks)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
