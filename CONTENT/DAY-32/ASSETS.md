# DAY 32 — Asset Manifest

**Status:** READY  
**Generated:** 11 November 2026  
**Source method:** built-in ImageGen source + deterministic Pillow renderer  
**Publication:** NOT PUBLISHED

## Source

| File | Dimensions | SHA-256 |
|---|---:|---|
| `assets/storage-triptych.png` | 2172 × 724 | `3d2fe7a0282207d1ca7a7327522558297f790d82d33d68b183af8336100e4b18` |

## Carousel

| File | Dimensions | SHA-256 |
|---|---:|---|
| `assets/carousel-01.png` | 1080 × 1350 | `4da3e5f729ab7870ab2daace28e06acfc4044f419358d2fe5c5b90d5b3761ad4` |
| `assets/carousel-02.png` | 1080 × 1350 | `efa016d519f2804450d9767cc3ae01ee7d34739c90e841e74b70c49d8db7a6a8` |
| `assets/carousel-03.png` | 1080 × 1350 | `f1f8abc37a0840d0c612be450ded3ffe54b453e6ad2c6771707aa0024d970697` |
| `assets/carousel-04.png` | 1080 × 1350 | `5772ee041046e8ef5d76fa856d0236b911353d82bb36ecc19aced355775623b4` |
| `assets/carousel-05.png` | 1080 × 1350 | `1588d7ed774514dea1e4b7dfd58260d7d842fc019a4ce63975ea9c1d7c9bad86` |
| `assets/carousel-06.png` | 1080 × 1350 | `1acc29cc38c2ab943cd975fa8ac114a78bae135c85ccd41d46d335c50c6415fd` |
| `assets/carousel-07.png` | 1080 × 1350 | `39bb5664fd11557d47b58b0bbcc9f9fd4e25683d39783de0691775e27bfd0f66` |
| `assets/carousel-08.png` | 1080 × 1350 | `a2a977e004108ec8f0f571fe32c9d3cff9a856b81e01eb60e192c098fe023f81` |

## Stories

| File | Dimensions | SHA-256 |
|---|---:|---|
| `assets/story-01.png` | 1080 × 1920 | `5a7fc6423191b0b14af87576ea37b3d14aab2788551ee360affed9988d971075` |
| `assets/story-02.png` | 1080 × 1920 | `63483295c977f9f1b7b6d654923f840d81dcf88d8f03e51b90f690f59f94240e` |
| `assets/story-03.png` | 1080 × 1920 | `d4630318560fa64b4b6ae3c7b05ec83ab661405fc65004f97d4b1675ce680e9b` |

## QA previews

| File | SHA-256 |
|---|---|
| `assets/contact-sheet.png` | `def2ba3aef8c1fa32426f578c61ada03c48b0ef6d1cb1504fd77a761584bce7c` |
| `assets/stories-contact-sheet.png` | `4f785002f5d556216c25f1506d9c107f57358e90f2e9e1366ad72785bae32352` |

## QA performed

- Full PNG decode and exact dimensions checked.
- Carousel and Stories contact sheets visually inspected.
- Source checked for adult Muslim model, full modest coverage, realistic hands, fabric folds, and absence of text/watermark.
- Mobile hierarchy, safe margins, and Indonesian spelling checked.
- No category/series/production label appears above final visual headlines.
- Claims remain conditional; no publication or performance result inferred.

## Rebuild

Run `python CONTENT/DAY-32/render.py` with Pillow installed. The renderer reads `assets/storage-triptych.png` and reproduces the final PNG set.
