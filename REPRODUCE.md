# How this repository was made (Seychelles)

This file is written by the build on 2026-10-28, the day the source data was retrieved. Everything below is enough to rebuild this repository hash for hash.

## Sources

| Source | Address | Retrieved | Requests | Licence |
| --- | --- | --- | ---: | --- |
| SeyLII, Seychelles Legal Information Institute (Laws.Africa Peachjam platform, read through the Internet Archive) | <https://seylii.org> | 2026-10-28 | 122 | CC BY-NC 4.0, crediting SeyLII as the source (SeyLII terms of use, s. 9, archived https://web.archive.org/web/20260301144011id_/https://seylii.org/terms-of-use/) |
| Internet Archive Wayback Machine | <https://web.archive.org> | 2026-10-28 | None | Archived copies of SeyLII pages; the content licence is SeyLII's |

Every response is cached by the sha256 of its URL, and the table above lists every source with its retrieval date. Lexifina keeps its fetch scripts privately; `tools/parse.py` reads only the cache and writes `corpus.json`, so the same cache always gives the same corpus.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution of the Republic of Seychelles | 14 | 1993-06-21 to 2025-07-04 |
| `civil-status` | Civil Status Act | 4 | 2015-12-31 to 2022-11-01 |
| `licences` | Licences Act, 2010 | 4 | 2017-07-05 to 2024-04-29 |

The build made 23 commits:

| Commits | Kind |
| ---: | --- |
| 3 | first version of an act |
| 19 | one law on its in-force day |
| 1 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-28.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 19 laws in the record.
- 40 tags.

## Dates

Each commit is dated at noon (Indian/Mahe) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Not applied: every version is dated by SeyLII's own expression date, the day the amendment it incorporates took effect as SeyLII (Laws.Africa) records it. No date is computed from a default rule. https://web.archive.org/web/20260218091524id_/https://seylii.org/akn/sc/act/si/1993/38/eng@2025-07-04

## Commands, in order

```sh
# fill the cache from the sources listed above (network; Lexifina's fetch scripts are kept privately)
python -X utf8 tools/parse.py                  # cache -> corpus.json (no network)
python -X utf8 tools/build.py <folder> --repo <empty folder> --docs-date 2026-10-28
python -X utf8 tools/check_repo.py <repo> --corpus <folder>/corpus.json --write
python -X utf8 tools/build.py <folder> --repo <another empty folder> --docs-date 2026-10-28 --compare <repo>
```

In the main Lexifina repository these files live as follows:
- `fetch.py`, `parse.py` and `repo/`: in `scripts/seychelles-law/`.
- `build.py`, `check_repo.py` (`check.py` there) and `on.py`: in `scripts/gitlaw_common/`, with the corpus format in `SCHEMA.md`.

## Exact inputs

- `corpus.json` sha256 `3eefb8550477a49309ae486d2186342d97702c5ae64397fa327c6c178948a833` (715420 bytes)
- Script blob hashes (`git hash-object`):

| Script | Blob |
| --- | --- |
| build.py | `2bfc4ac9df193a7be844556d7f69cdb9d93ec3f2` |
| check.py | `cd346c7ff9996d450240e3bab52bcae03b2bc865` |
| on.py | `644a6c0857fbcc72562032b58d57aa113fee0641` |
| fetch.py | `df09209f308e09a677feb632bc7f6c05a295df14` |
| parse.py | `11ac97adb0ecb14cc9a428b0a4051e6f61bf441d` |

- Tools:
  - Python 3.14.0
  - git version 2.52.0.windows.1
  - curl 8.21.0 (Windows) libcurl/8.21.0 Schannel zlib/1.3.2 WinIDN WinLDAP

## Checks

18 versions of 2 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 19 history commits and 33 tags (history tip `3cefe1d7c8dd187cd23788959caeb4303b478077`).

These results are from the check run on the build before this one, from the same corpus.

## Decisions made by hand

- SeyLII files the Constitution of 1993 as /akn/sc/act/si/1993/38; every one of its 15 expressions (1993-06-21 to 2025-07-04) has an Internet Archive copy, so each version is read from its own dated expression. In 2023-24 SeyLII also showed the Constitution at /akn/sc/act/1994/7 (2 expressions), a number it later gave to the First Amendment Act 1994; those pages are not used.
- The Constitution as adopted in 1993 is credited as kind 'law' (SeyLII files it among its Acts, in the S.I. series); the commit names it 'Constitution of 1993'. No referendum or assent date is taken from outside the source.
- Licence and terms: SeyLII licensed its content CC BY-NC 4.0 with attribution, and its terms of use (archived 2026-03-01) prohibit scraping and bulk downloading; its robots.txt sends Content-Signal ai-train=no and disallows ClaudeBot and other AI crawlers. No SeyLII document page was fetched: every version is read from the Internet Archive's copy, for the configured acts only. The user decided on 2026-10-28 that reading these archived copies is acceptable (relayed by the coordinator: "scraping wayback is fair game, dont overdo it"). The repository stays private; CC BY-NC allows only non-commercial use. No legal text was given to a model.
- Version dates are SeyLII's expression dates. Laws.Africa's terminology guide (https://docs.laws.africa/getting-started/terminology-guide) says "Amendments to Principal works come into force on the Commencement date of the Amending work" and that the first point in time is "the work as originally published"; so an amendment's expression is dated by its commencement (in force), and an act's original expression by its publication, which is replaced by the commencement date the page states.
- Credits: a version whose History names exactly one amending law (and no consolidation) between it and the previous version is credited to that law for every provision that changed. Otherwise a provision is credited only to laws that SeyLII's editorial note inside that provision links to; the rest are unexplained (publisher).
- Editorial notes (akn-remark) are left out of the text and used only as credit evidence, except where a provision has no other text (repealed or spent), where the note is the provision's whole printed content.
- Part, Chapter and Division headings are left out; each provision file starts with its own number and heading. Every other text of each version is in a provision file: parse.py checks this per version (verification.json, fidelity).
- Constitution: SeyLII's 2020-06-01 expression is its 2020 consolidation, keyed as a separate text: it marks every article up as a section, gives 97 articles different wording from both the 2018 and the 2022 expressions (spelling such as naturalization/naturalisation, dropped words such as 'if' in art. 13(1)(b), and headings such as 'Declaration of Authority' for art. 1), and SeyLII's next expression (2022-06-20) is built on the 2018 text, not on it. Taking it in would show 185 articles changing and changing back with no law behind either change, so it is left out; the 2022-06-20 version follows the 2018-08-23 version directly, and differs from it only in arts. 50, 162 and 163, each of which SeyLII's own note credits to Act 13 of 2022.
- Constitution: lines that held only a number or a quoted term, left over from a subprovision whose whole printed content is an editorial remark (SeyLII's '[... repealed by ...]' or its notes to the 1991 edition), are removed: art-066a (11) (12); art-081 (2A); art-112 (c); art-115c (4A); art-146 (8); sch-02 "Electoral Commissioner".
- Civil Status Act: lines that held only a number or a quoted term, left over from a subprovision whose whole printed content is an editorial remark (SeyLII's '[... repealed by ...]' or its notes to the 1991 edition), are removed: sch-02 (1) (2) (3); sec-002 "interment"; sec-034 (b).
- Licences Act: held back from main (corpus.d/50-licences.json, no .PUBLISH): its latest SeyLII expression (2024-04-29) does not match the Licences (Amendment) Act, 2024 (Act 2 of 2024) as printed in the Supplement to the Official Gazette of 29 April 2024 (gazette.sc, text layer): in the definition of "fixed penalty" SeyLII reads "regulation made under this Act" and "by payment of the fixed penalty" where the Act inserts "regulations made under this Act" and "on payment of the fixed penalty", and the definition of "Minister" ends "responsible for investment and;" where the Act has "responsible for Investment; and". Every other provision Act 2 of 2024 inserts or substitutes (ss. 1A, 20(1), 22A, 28A, 30(2)-(3), the Schedule) matches word for word. Today's text is therefore not verified as the official text, and the act stays off main until it is.
- Licences Act: lines that held only a number or a quoted term, left over from a subprovision whose whole printed content is an editorial remark (SeyLII's '[... repealed by ...]' or its notes to the 1991 edition), are removed: sch-01 14. 15. 24.; sec-020 (3) (4).
- Licences Act: an en dash not between two digits is printed as an em dash (26 in all versions): SeyLII typeset some expressions' chapeaux with en dashes and later ones with em dashes, so this is one form of dash, not a change of wording.

## What AI did and did not do

The fetch, parse and check scripts were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above, through code that anyone can rerun.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code (Claude Opus 5.5, claude-opus-5-5) wrote fetch.py and the configuration and chose the acts. No model wrote, summarised or transformed legal text: parse.py is deterministic code (the shared adapter scripts/africa-law/peachjam.py).
