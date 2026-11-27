# Structure

| Folder | What it holds |
| --- | --- |
| `constitution/` | The Constitution of the Republic of Seychelles, 1993, one file per article (`art-081.md`) |
| `acts/<year>/<NNN>-<slug>/` | An Act, by its year and number, e.g. `acts/2026/016-trade-remedies/` (Act 16 of 2026); the older acts consolidated by SeyLII by the year and number SeyLII gives them, e.g. `acts/1883/004-civil-status/` |
| `acts/2021/001-civil-code-of-seychelles/` | The Civil Code of Seychelles Act, 2020 (Act 1 of 2021): its sections, and the Civil Code (its Schedule) in `code/0001-0999/`, `code/1000-1999/` and `code/2000-2999/`, one file per article (`art-1382.md`) |
| `subsidiary/<year>/<NNN>-<slug>/` | A statutory instrument, by the year and number of the S.I. |

Each folder holds one file per section (`s-012.md`; `s-005-a.md` is section 5A) or article, the schedules
(`schedule-1.md`), and a `README.md` with the source and the provisions. No folder holds more than 1,000 entries.

## Dates

Each version is one commit, dated 12:00 Indian/Mahe on the day it took effect, which its `In-force:` trailer
repeats; `In-force-basis:` says where that day comes from:

- `commencement-provision`: the day the Act or instrument itself names;
- `commencement-notice (S.I. N of YYYY)`: the day the Act's (Commencement) Notice appoints, when the notice brings
  the whole Act into operation;
- `gazette-publication`: the day the Act was published in the Gazette, where it names no other day (an Act becomes
  law on publication or such other date as it prescribes: Digitization and Publication of Gazette Act, 2020, s. 6(2));
- the SeyLII consolidations keep the dates of SeyLII's point-in-time versions (see README.md).

Acts brought into operation by a notice not yet found, or only in part, are held back, as are PDFs without a text
layer (no OCR is run) and Acts whose sections could not be split cleanly. No date in this repository is the day we
downloaded anything.
