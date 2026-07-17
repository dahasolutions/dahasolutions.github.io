# sideledger-config

Public tax-year constants for the SideLedger app, served via GitHub Pages.

- `v1/manifest.json` — app checks this tiny file first (configVersion per year)
- `v1/tax/<year>.json` — full TaxYearConfig (mileage rate, SE tax, brackets,
  standard deduction, quarterly deadlines, safe harbor)
- `schema/` — JSON Schema; CI validates every change before it can merge
- Sources: IRS Notice 2026-10, IRS Publication 926, IRS Rev. Proc. 2025-32

## Ops
- Annual update (December): copy latest year file → new year, update numbers
  + `sources`, bump `manifest.json` (`latestYear`, `years`, `configVersion`)
  → open PR → CI must pass → merge → live globally in ~10-15 min (Pages CDN).
- Mid-year fix: edit year file, bump `configVersion` in BOTH the file and
  manifest (CI enforces the match) → PR → merge.
- Protect `main`: require PR + passing CI. Never commit secrets here.

Setup: Settings → Pages → Deploy from branch `main`, folder `/ (root)`.
App base URL: `https://<username>.github.io/sideledger-config/v1`
