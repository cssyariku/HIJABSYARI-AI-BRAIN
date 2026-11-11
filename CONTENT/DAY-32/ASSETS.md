# DAY 32 — Asset Manifest

**Status:** READY  
**Generated:** 11 November 2026  
**Source method:** built-in ImageGen source + deterministic Pillow renderer  
**Publication:** NOT PUBLISHED

## Source

| File | Dimensions | SHA-256 |
|---|---:|---|
| `assets/storage-triptych.png` | 2172 × 724 | `e4753874599dd42bafe3b2f025beeb55bdf51c134f1d1ff802f23601b1cece53` |

## Carousel

| File | Dimensions | SHA-256 |
|---|---:|---|
| `assets/carousel-01.png` | 1080 × 1350 | `86cf5b1bdfc05d031878c6ffe380144acc067eb8217924167e9eb283e1e8bf18` |
| `assets/carousel-02.png` | 1080 × 1350 | `41d689ce0285f5e6de83d4c62d78f48bd19252e8f2bd2c046e7ca7b0c2157cf2` |
| `assets/carousel-03.png` | 1080 × 1350 | `790b711ac0f1bf08ecf7f702599959f879f1ac0a17adca59c6c582776760907f` |
| `assets/carousel-04.png` | 1080 × 1350 | `5772ee041046e8ef5d76fa856d0236b911353d82bb36ecc19aced355775623b4` |
| `assets/carousel-05.png` | 1080 × 1350 | `d2f90ca27f5cc711461bd1051658309f2402b67545f2996112cc91c764cab931` |
| `assets/carousel-06.png` | 1080 × 1350 | `1acc29cc38c2ab943cd975fa8ac114a78bae135c85ccd41d46d335c50c6415fd` |
| `assets/carousel-07.png` | 1080 × 1350 | `ec3595db760a93df7b74beca5747f62c353a6ace8e8766231fdd2120672f5813` |
| `assets/carousel-08.png` | 1080 × 1350 | `a2a977e004108ec8f0f571fe32c9d3cff9a856b81e01eb60e192c098fe023f81` |

## Stories

| File | Dimensions | SHA-256 |
|---|---:|---|
| `assets/story-01.png` | 1080 × 1920 | `d3dac5f7d25b28496060f896d9946e9d5559615cfeb1b43fd5b33cba89dc666c` |
| `assets/story-02.png` | 1080 × 1920 | `549af45a7de6f518fba74ab5a2dddd568a7b9b2757cd2b44265814cca0dbbca2` |
| `assets/story-03.png` | 1080 × 1920 | `d4630318560fa64b4b6ae3c7b05ec83ab661405fc65004f97d4b1675ce680e9b` |

## QA previews

| File | SHA-256 |
|---|---|
| `assets/contact-sheet.png` | `af08ff02922558607864927f5d770354813585950bd52d6e329b49084370e719` |
| `assets/stories-contact-sheet.png` | `026cafc9c675f27c901513374d0c482e73239836a2a9ab26682e472a010fdb25` |

## QA performed

- Full PNG decode and exact dimensions checked.
- Carousel and Stories contact sheets visually inspected.
- Source checked for adult Muslim model, full modest coverage, realistic hands, fabric folds, and absence of text/watermark.
- Mobile hierarchy, safe margins, and Indonesian spelling checked.
- No category/series/production label appears above final visual headlines.
- Claims remain conditional; no publication or performance result inferred.

## Rebuild

Run `python CONTENT/DAY-32/render.py` with Pillow installed. The renderer reads `assets/storage-triptych.png` and reproduces the final PNG set.
