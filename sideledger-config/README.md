# sideledger-config

Public tax-year constants for the SideLedger app, served from GitHub Pages at
`https://dahasolutions.github.io/sideledger-config/`. This folder lives inside the
`dahasolutions.github.io` repo; the workflow sits at that repo's root as
`.github/workflows/sideledger-config-validate.yml`.

- `v2/manifest.json` — the app checks this tiny file first (configVersion per year)
- `v2/tax/<year>.json` — full TaxYearConfig: dated mileage rates, SE tax, brackets,
  standard deduction, §199A parameters, quarterly deadlines, safe harbor
- `schema/` — JSON Schema; CI validates every change before it can merge
- Sources: IRS Notice 2026-10 + Announcement 2026-11 (mileage), SSA COLA fact sheet
  (wage base), Rev. Proc. 2025-32 (brackets, standard deduction, §199A thresholds),
  Form 1040-ES (deadlines)

`schemaVersion` is the folder name. A breaking change to the JSON shape ships under
a new folder so builds that only understand the old shape keep reading the old one.
`v1/` was retired 2026-09-02 before any build shipped against it.

## Ops
- Annual update (December): copy the latest year file → new year, update numbers
  + `sources`, bump `manifest.json` (`latestYear`, `years`, `configVersion`)
  → PR → CI must pass → merge → live globally in ~10-15 min (Pages CDN).
- Mid-year fix (a second mileage rate, say): edit the year file, append to
  `mileageRates` with its `from` date, bump `configVersion` in BOTH the file and
  the manifest (CI enforces the match) → PR → merge.
- Protect `main`: require PR + passing CI. Never commit secrets here.

App base URL: `https://dahasolutions.github.io/sideledger-config/v2/`
