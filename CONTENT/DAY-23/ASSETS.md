# Asset Manifest — Day 23

**Content ID:** `HS-COLOR-007`  
**Status:** READY; not published  
**QA date:** 30 October 2026

## Upload-ready deliverables

| File group | Count | Specification |
|---|---:|---|
| `assets/carousel-01.png`–`carousel-08.png` | 8 | 1080 × 1350 PNG |
| `assets/story-01.png`–`story-03.png` | 3 | 1080 × 1920 PNG |

Stories 2 and 3 require native Instagram Poll/Questions stickers at upload. The PNGs contain audience-facing prompts only; production instructions remain in `COPYWRITING.md`.

## Source and QA previews

| File | Specification | Purpose |
|---|---|---|
| `assets/brown-outfit-five-hijab-colors.png` | 2057 × 765 RGB PNG | Controlled five-color ImageGen source |
| `assets/contact-sheet.png` | 1080 × 730 PNG | Eight-slide carousel QA preview |
| `assets/stories-contact-sheet.png` | 810 × 534 PNG | Three-Story QA preview |
| `render.py` | Deterministic Pillow renderer | Rebuild final layouts from source |

## SHA-256 inventory

- `brown-outfit-five-hijab-colors.png`: `4929d99124742eb2e133d614794b62495ffbda9c48af98c7676d4bfc6f471a71`
- `carousel-01.png`: `ac012845b2c3dd3122e34c7b79d1ab8275c8f4be97d28afe27acd9832d528310`
- `carousel-02.png`: `32901f2f0b239de118bc0cbd221c4eb1fc7a3e88641ad739ea33b4f3fbf9949d`
- `carousel-03.png`: `04369c4fc5d16f5afdc75fdefcbfa8d1eeaff10005d6d56a3d77bd9b1f3b4985`
- `carousel-04.png`: `f738d12a880f0860d2e50113f183e7e70d4a5226ec09a7459a8033a08942a1ac`
- `carousel-05.png`: `5fc95076a9b8441dfbfaefe6db4b3958c720c246c281f18c8030168e1d904ebe`
- `carousel-06.png`: `e0457e7bf13cb4c8572787068a4515c455720682799bdd77f73d93cac100d129`
- `carousel-07.png`: `63004b9e17fa869db53b5395b13ea86fcc00af6a2fc296f0ebb2062c7017b98d`
- `carousel-08.png`: `fb1c2f04abbed729ac5e35926f48eac068bfa640f5dbd2e7b472f1c82dbb336b`
- `story-01.png`: `56931638d893ed9fb31c5451731dfb5573a93b07102ca7e0a3770bcb3fb43dcb`
- `story-02.png`: `5b05e0fe42632defbb37d9ea0e296351445e905f9fa58f29bc9d2562087ee6b6`
- `story-03.png`: `7ce70046f68701a06d27c031ba82eefdfe5eba6f63c391c8bf01433b7305c789`
- `contact-sheet.png`: `627a118dbd4f9ecd6dfe88715139c018cbf76fedc273135c2588f4e36fabaab1`
- `stories-contact-sheet.png`: `d27c093011f918da5e7b23f9782c2e3dc386d564f08941fa2fb21e0b4da63c61`

## QA evidence

- All 14 PNGs opened and passed Pillow checksum/decode verification.
- Eight upload carousel files verified at 1080 × 1350; three upload Stories verified at 1080 × 1920.
- Visual inspection passed for Indonesian spelling, hierarchy, safe margins, mobile readability, adult Muslim model, opaque modest coverage, consistent identity/pose/outfit/lighting, plausible anatomy and hands, realistic matte fabric, and five-color separation.
- No small category, series, production, day, or experiment label appears above a public headline.
- Stories contain no visible production instruction; native-sticker directions are stored only in the copy document.
- Color descriptions are observations, not trend, product-color, undertone, or universal-suitability claims.
- No Instagram publication, URL, response, Insight, or performance metric is recorded.
