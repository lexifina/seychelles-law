# How this repository was made (Seychelles)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| SeyLII, Seychelles Legal Information Institute (Laws.Africa Peachjam platform, read through the Internet Archive) | <https://seylii.org> | 2026-10-28 | CC BY-NC 4.0, crediting SeyLII as the source (SeyLII terms of use, s. 9, archived https://web.archive.org/web/20260301144011id_/https://seylii.org/terms-of-use/) |
| Internet Archive Wayback Machine | <https://web.archive.org> | 2026-10-28 | Archived copies of SeyLII pages; the content licence is SeyLII's |
| SeyLII, Seychelles Legal Information Institute (Laws.Africa Peachjam platform, read through the Internet Archive): Evidence Act | <https://seylii.org> | 2026-10-30 | CC BY-NC 4.0, crediting SeyLII as the source (SeyLII terms of use, s. 9, archived https://web.archive.org/web/20260301144011id_/https://seylii.org/terms-of-use/) |
| SeyLII, Seychelles Legal Information Institute (Laws.Africa Peachjam platform, read through the Internet Archive): Civil Code (1976) | <https://seylii.org> | 2026-10-30 | CC BY-NC 4.0, crediting SeyLII as the source (SeyLII terms of use, s. 9, archived https://web.archive.org/web/20260301144011id_/https://seylii.org/terms-of-use/) |
| SeyLII, Seychelles Legal Information Institute (Laws.Africa Peachjam platform, read through the Internet Archive): Commercial Code | <https://seylii.org> | 2026-10-30 | CC BY-NC 4.0, crediting SeyLII as the source (SeyLII terms of use, s. 9, archived https://web.archive.org/web/20260301144011id_/https://seylii.org/terms-of-use/) |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution of the Republic of Seychelles | 14 | 1993-06-21 to 2025-07-04 |
| `civil-status` | Civil Status Act | 4 | 2015-12-31 to 2022-11-01 |
| `evidence` | Evidence Act | 1 | 2014-12-01 to 2014-12-01 |
| `civil-code-1976` | Civil Code of Seychelles Act | 2 | 2015-12-31 to 2021-07-01 |
| `commercial-code` | Commercial Code Act | 2 | 2014-12-01 to 2021-07-01 |

The build made 23 commits:

| Commits | Kind |
| ---: | --- |
| 5 | first version of an act |
| 17 | one law on its in-force day |
| 1 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 17 laws in the record.
- 39 tags.

## Dates

Each commit is dated at noon (Indian/Mahe) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Not applied: every version is dated by SeyLII's own expression date, the day the amendment it incorporates took effect as SeyLII (Laws.Africa) records it. No date is computed from a default rule. https://web.archive.org/web/20260218091524id_/https://seylii.org/akn/sc/act/si/1993/38/eng@2025-07-04

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `13dcdb7fc30cc2ca4ad41a228776c9f5efd6504bcaf96a3e38254b53c9cb9bfe` (2008630 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

23 versions of 5 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- SeyLII files the Constitution of 1993 as /akn/sc/act/si/1993/38; every one of its 15 expressions (1993-06-21 to 2025-07-04) has an Internet Archive copy, so each version is read from its own dated expression. In 2023-24 SeyLII also showed the Constitution at /akn/sc/act/1994/7 (2 expressions), a number it later gave to the First Amendment Act 1994; those pages are not used.
- The Constitution as adopted in 1993 is credited as kind 'law' (SeyLII files it among its Acts, in the S.I. series); the commit names it 'Constitution of 1993'. No referendum or assent date is taken from outside the source.
- Licence: SeyLII licensed its content CC BY-NC 4.0 with attribution; CC BY-NC allows only non-commercial use. Every version is read from the Internet Archive's copy, for the configured acts only. No legal text was given to a model.
- Version dates are SeyLII's expression dates. Laws.Africa's terminology guide (https://docs.laws.africa/getting-started/terminology-guide) says "Amendments to Principal works come into force on the Commencement date of the Amending work" and that the first point in time is "the work as originally published"; so an amendment's expression is dated by its commencement (in force), and an act's original expression by its publication, which is replaced by the commencement date the page states.
- Credits: a version whose History names exactly one amending law (and no consolidation) between it and the previous version is credited to that law for every provision that changed. Otherwise a provision is credited only to laws that SeyLII's editorial note inside that provision links to; the rest are unexplained (publisher).
- Editorial notes (akn-remark) are left out of the text and used only as credit evidence, except where a provision has no other text (repealed or spent), where the note is the provision's whole printed content.
- Part, Chapter and Division headings are left out; each provision file starts with its own number and heading. Every other text of each version is in a provision file: this is checked per version (verification.json, fidelity).
- Constitution: SeyLII's 2020-06-01 expression is its 2020 consolidation, keyed as a separate text: it marks every article up as a section, gives 97 articles different wording from both the 2018 and the 2022 expressions (spelling such as naturalization/naturalisation, dropped words such as 'if' in art. 13(1)(b), and headings such as 'Declaration of Authority' for art. 1), and SeyLII's next expression (2022-06-20) is built on the 2018 text, not on it. Taking it in would show 185 articles changing and changing back with no law behind either change, so it is left out; the 2022-06-20 version follows the 2018-08-23 version directly, and differs from it only in arts. 50, 162 and 163, each of which SeyLII's own note credits to Act 13 of 2022.
- Constitution: lines that held only a number or a quoted term, left over from a subprovision whose whole printed content is an editorial remark (SeyLII's '[... repealed by ...]' or its notes to the 1991 edition), are removed: art-066a (11) (12); art-081 (2A); art-112 (c); art-115c (4A); art-146 (8); sch-02 "Electoral Commissioner".
- Civil Status Act: lines that held only a number or a quoted term, left over from a subprovision whose whole printed content is an editorial remark (SeyLII's '[... repealed by ...]' or its notes to the 1991 edition), are removed: sch-02 (1) (2) (3); sec-002 "interment"; sec-034 (b).
- Evidence Act: SeyLII publishes one expression, its consolidation of 1 December 2014, and its History lists no amendment after it (and none not yet applied), so that text is the act as SeyLII holds it in force. It is dated 2014-12-01 and credited to SeyLII as the oldest version available; the amending laws SeyLII lists before it (Act 16 of 1856 to Act 23 of 2013) are named in the long title.
- Evidence Act: The long title is SeyLII's editorial list of amending laws, with its two footnotes ('Mauritius Ordinance'); it is kept because it is the preface's whole printed content. The adapter's character check flags it only because the footnote markers sit inside that editorial remark; it was compared with the page by hand and matches. Every other unit passes the character check, and no text is left outside the units.
- Civil Code (1976): lines that held only a number or a quoted term, left over from a subprovision whose whole printed content is an editorial remark, are removed: sch-01-art-1351 3..
- Civil Code (1976): an en dash not between two digits is printed as an em dash (3 in all versions), one form of dash, not a change of wording.
- Civil Code (1976): repealed on 2021-07-01 by Civil Code of Seychelles Act, 2020 (Act 1 of 2021), the day it commenced: SeyLII's History of the act: "Repealed by Civil Code of Seychelles Act, 2020" on 1 July 2021; SeyLII's page of the Civil Code of Seychelles Act, 2020 (Act 1 of 2021): "Assented to on 23 November 2020", "Published in 1 on 4 January 2021", "Commenced on 1 July 2021 by Civil Code of Seychelles Act, 2020 (Commencement) Notice, 2021". Every unit is removed in that version. The LII lists no amendment between its last expression and the repeal.
- Commercial Code: the LII's page says: There are outstanding amendments that have not yet been applied. See the History tab for more information.
- Commercial Code: Civil Code of Seychelles (Consequence of Enactment) Act, 2021 (Act 24 of 2021) in force 2021-07-01: its section 2 says it "shall come into operation on the same date that the Civil Code of Seychelles Act 2020, (Act 1 of 2021) comes into operation", which SeyLII gives as 1 July 2021 (commencement notice), and SeyLII's History of the Commercial Code lists "Amended by Civil Code of Seychelles (Consequence of Enactment) Act, 2021" on 1 July 2021 and nothing after it. Assent 28 June 2021, Supplement to the Official Gazette of 28 June 2021. The LII has no consolidation after it, so its amendments are applied here from the Act as printed in the Supplement to the Official Gazette (text layer): sch-01-art-002 repealed; sch-01-art-004 repealed; sch-01-art-012 line 2 replaced; sch-01-art-091 set; sch-01-art-109-9 set; sch-01-art-191 set. The new text keeps the Act's own numbering style ("(2)", "(1)"..., "Article 109-8"), not the "2." / "109 — 7" style of SeyLII's consolidation; article 109-8 is the unit after article 109-7 (file sch-01-art-109-9, since SeyLII's file names for articles 109-1 to 109-7 run one ahead of their numbers). Article 191 was a repealed placeholder in the 2014 consolidation and is replaced by the new article.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code (Claude Opus 5.5, claude-opus-5-5) wrote the configuration and chose the acts. No model wrote, summarised or transformed legal text: the text is parsed by Lexifina's shared deterministic code.
- Evidence Act: none at data-build time (deterministic parser).
- Civil Code (1976): none at data-build time (deterministic parser).
- Commercial Code: none at data-build time (deterministic parser).
