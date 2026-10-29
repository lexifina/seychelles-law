# Seychelles: law history in git

The law of Seychelles as a git history: one file per provision, one commit per law on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change to a provision; `tools/on.py` gives the text in force on any day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `sc/`. Every version is a dated point-in-time version published by [SeyLII](https://seylii.org) on the Laws.Africa Peachjam platform.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | [Constitution of the Republic of Seychelles](https://seylii.org/akn/sc/act/si/1993/38) | 14 | 1993-06-21 to 2025-07-04 |
| `civil-status/` | [Civil Status Act](https://seylii.org/akn/sc/act/1883/4) | 4 | 2015-12-31 to 2022-11-01 |
| `licences/` | [Licences Act, 2010](https://seylii.org/akn/sc/act/2010/23) | 4 | 2017-07-05 to 2024-04-29 |

**Constitution of the Republic of Seychelles**

| In force | Author |
| --- | --- |
| 1993-06-21 | Constitution of 1993 (as enacted) |
| 1994-07-11 | Act 7 of 1994 |
| 1995-03-27 | Act 5 of 1995 |
| 1995-11-20 | Act 19 of 1995 |
| 1996-08-14 | Act 14 of 1996 |
| 1998-02-21 | Act 14 of 1996 |
| 2000-06-26 | Act 7 of 2000 |
| 2011-07-12 | Act 7 of 2011 |
| 2016-10-16 | Act 4 of 2016 |
| 2017-04-19 | Act 5 of 2017 |
| 2018-08-23 | Act 8 of 2018 |
| 2022-06-20 | Act 13 of 2022 |
| 2025-03-31 | Act 14 of 2024 |
| 2025-07-04 | Act 6 of 2025 |

**Civil Status Act**

| In force | Author |
| --- | --- |
| 2015-12-31 | publisher (SeyLII): oldest version available |
| 2021-07-01 | Act 24 of 2021; publisher (SeyLII): 1 provision(s) unexplained |
| 2022-06-01 | Act 45 of 2021 |
| 2022-11-01 | Act 45 of 2021 |

**Licences Act, 2010**

| In force | Author |
| --- | --- |
| 2017-07-05 | publisher (SeyLII): oldest version available |
| 2019-03-04 | Statutory Instrument 9 of 2019 |
| 2021-12-20 | Act 60 of 2021 |
| 2024-04-29 | Act 2 of 2024 |

Each folder's `README.md` lists every provision, how often it changed and when.

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did art-081 say on 1993-06-21? | `python tools/on.py 1993-06-21 constitution art-081` |
| The same, with raw git (bash) | `git show $(git rev-list -1 --before="1993-06-21T23:59:59Z" main -- constitution/art-081.md):constitution/art-081.md` |
| The same, in PowerShell | `$r = git rev-list -1 --before="1993-06-21T23:59:59Z" main -- constitution/art-081.md; git show "$($r):constitution/art-081.md"` |
| Which law wrote each line? | `git blame constitution/art-081.md` |
| Every change, word by word | `git log -p --word-diff constitution/art-081.md` |
| Every law in the record, in order | `git log --reverse --format="%ad %an" --date=short main` |
| Everything one law changed | `git show law/<key>` (tags `law/<key>` mark each law's commit) |
| The whole act on a date | `python tools/on.py 1993-06-21 constitution` |
| Which law gave a provision its wording on a date | `python tools/on.py --law 1993-06-21 constitution art-081` |

After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## Dates

- Each commit is dated at **noon, Indian/Mahe, on the day the change took effect**. The day is also in the `In-force:` trailer, which the tools read; enactment (assent) and Gazette publication dates are trailers too, where SeyLII states them.
- **The day is SeyLII's.** Each version is a Laws.Africa expression, and its date is the day the amendment it takes in came into force, as the amendment list says ("[Amended by <Act> on <date>]"). For a consolidation (a revised edition) it is the date the edition is as at. An act's original expression is dated by its Gazette publication; where SeyLII gives a later commencement date ("Commenced on ..."), the first version is dated by that instead (see REPRODUCE.md, decisions).
- `--before="YYYY-MM-DD"` alone uses your clock's time of day, so a law that took effect that day may be missed before noon. Use `T23:59:59Z` as above, or the tool.

## How it is checked

- Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`); both must match `corpus.json`. Results are in `REPRODUCE.md`.
- **Against SeyLII today:** the last version of each act is SeyLII's current expression, as named by its own legislation listing on the retrieval day, and is the text of that expression page.
- **Every version is its own dated expression**: each was parsed from an archived copy of exactly that expression's page, whose sha256 is recorded with the version.
- The repository is rebuilt from the same data a second time and must give identical hashes.

## What "author" means

The author of a commit is the law that made the change, with an e-mail address that cannot exist, so `git blame` and `git log --author` name laws. The committer is always Lexifina.

- **Credits come only from SeyLII's own notes.** A version whose History entry names one amending Act is credited to it. Where one version takes in several Acts, or a revised edition, a provision is credited to an Act only if SeyLII's editorial note in that provision names it ("[section 5 amended by section 2 of Act 3 of 2020]"); the rest are committed by the publisher and labelled "unexplained", and the commit message names the Acts the version takes in.
- **The first commit** is the act as enacted where that is the oldest version; otherwise it is the oldest version available (a consolidation), credited to the publisher.
- Blame credits whole lines (one paragraph per line). Use `git log -p --word-diff` to see exactly which words each change made.

## What it does not show

- **Only the versions SeyLII publishes.** Changes before its oldest version are not separate commits.
- **Editorial notes.** SeyLII's bracketed notes ("[Act No. 18 of 1996]", "[section 5 amended by ...]") are left out of the text and used only for credits, except where a provision has no other text (repealed or spent), where the note is what SeyLII prints and is kept.
- **Headings above the provision** (Part, Chapter, Division) are left out; each file starts with its own number and heading. Footnotes are kept at the end of the file.
- **Amendments not yet applied.** Where the LII lists an amendment as not yet applied to its consolidated text, it is not in this history; REPRODUCE.md lists each one.
- **No OCR.** Acts the LII shows only as scanned PDFs are not included.

## How it is built


## Sources

| Source | What it gives | Used for |
| --- | --- | --- |
| [SeyLII](https://seylii.org) | Dated point-in-time versions (expressions) of each act, its History and amendment list, and per-provision editorial notes; its listing page names the current version | The text and dates of every version |
| [Internet Archive](https://web.archive.org/) | Archived copies of those expression pages | Reading them |

## Licence

See [LICENSE](LICENSE). Source: SeyLII (https://seylii.org), licensed under the Creative Commons Attribution-NonCommercial 4.0 International licence (CC BY-NC 4.0).

SeyLII's terms: CC BY-NC 4.0, crediting SeyLII as the source (SeyLII terms of use, s. 9, archived https://web.archive.org/web/20260301144011id_/https://seylii.org/terms-of-use/). Lexifina's arrangement, messages, tables and tools are CC0.

This repository is not legal advice. Seychelles's laws are published in English, so there is no separate summary in another language.
