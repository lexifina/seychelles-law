"""Build Seychelles' corpus.json from the cache only, through the shared Peachjam adapter.

    python -X utf8 scripts/seychelles-law/parse.py

Reads acts.json (configuration), sources.json (pinned Wayback captures, written by fetch.py) and .cache/; writes
corpus.json (atomically) and verification.json (the checks). Deterministic: the same cache gives the same bytes.

After peachjam.parse() it applies three Seychelles-specific steps (candidates for the shared adapter):
1. expressions left out on purpose (acts.json "skip": {date: reason}) get their reason in `decisions` and in the next
   version's note, in place of the adapter's generic "the Internet Archive holds no copy";
2. an amending law whose archived page loads its text by script has no coverpage notices; its assent and publication
   dates are then read from the History tab of that same page ("Assented to", "Published in ...");
3. the Constitution of 1993 is SeyLII work si/1993/38 (S.I. series), which the adapter would call a decree; it is
   recorded as kind "law".
"""
import json
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SHARED = HERE.parent / "africa-law" / "peachjam.py"
if SHARED.exists() and (not (HERE / "peachjam.py").exists()
                        or SHARED.read_bytes() != (HERE / "peachjam.py").read_bytes()):
    shutil.copyfile(SHARED, HERE / "peachjam.py")
sys.path.insert(0, str(HERE))
import peachjam  # noqa: E402


def post(corpus: dict, report: dict) -> None:
    cfg = peachjam.load_config(HERE)
    pins = json.loads((HERE / "sources.json").read_text(encoding="utf-8"))
    cache = peachjam.Cache(HERE, offline=True)
    by_slug = {a["slug"]: a for a in corpus["acts"]}
    for act in cfg["acts"]:
        skip = act.get("skip") or {}
        if not skip:
            continue
        days = sorted(skip)
        generic = (f"{act['short']}: the LII lists expression(s) {', '.join(days)}, but the Internet Archive holds no "
                   f"copy, so their changes appear in the next version that is archived.")
        corpus["decisions"] = [d for d in corpus["decisions"] if d != generic]
        for day in days:
            corpus["decisions"].append(f"{act['short']}: {skip[day]}")
            vs = by_slug[act["slug"]]["versions"]
            nxt = next((v for v in vs if v["from"] > day), None)
            if nxt is not None:
                prev = max((v["from"] for v in vs if v["from"] < day), default=None)
                nxt["note"] = (f"SeyLII's {day} consolidation is left out (see REPRODUCE.md, decisions); this version "
                               f"follows the {prev} version directly.")
    # law dates from the History tab of the law's own page, where its coverpage is not in the archived copy
    for uri, p in pins.get("laws", {}).items():
        key = peachjam.law_key(uri)
        if not p or key not in corpus["laws"]:
            continue
        law = corpus["laws"][key]
        if law.get("enacted") and law.get("published"):
            continue
        info = peachjam.page_info(cache.get(p["url"]))
        for t in info["timeline"]:
            for e in t["events"]:
                if not law.get("enacted") and e["text"].startswith("Assented to"):
                    law["enacted"] = t["date"]
                if not law.get("published") and e["text"].startswith("Published"):
                    law["published"] = t["date"]
        if not law.get("title") or law["title"] == corpus["acts"][0]["title"]:
            law["title"] = p.get("title_checked") or law["title"]
    for a in corpus["acts"]:
        if a["slug"] == "constitution" and a.get("first_law"):
            corpus["laws"][a["first_law"]]["kind"] = "law"


corpus, report = peachjam.parse(HERE)
post(corpus, report)
peachjam.write_corpus(HERE, corpus)
peachjam.write_docs(HERE, corpus)
(HERE / "verification.json").write_text(json.dumps(report, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps(peachjam.summary(corpus, report), indent=1))
