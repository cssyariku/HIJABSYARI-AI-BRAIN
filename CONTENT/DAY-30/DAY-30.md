# DAY 30 — Vote topik bulan berikutnya

**Content ID:** `HS-COMM-004`  
**Production day:** Day 30  
**Production date:** 8 November 2026  
**Status:** READY — four final Stories, ImageGen source, editable renderer, and QA preview are present; not published.  
**Format:** Instagram Stories, 4 frames  
**Pillar:** Community / Research  
**Primary objective:** Audience research  
**Secondary objective:** Low-friction interaction and next-calendar input  
**Experiment:** `EXP-031`  
**Monetization:** OFF

## Objective

Mengumpulkan pilihan audience untuk arah konten bulan berikutnya melalui dua Poll yang konkret dan satu Questions sticker, tanpa menganggap respons sebagai preferensi sebelum Stories benar-benar dipublikasikan dan datanya tercatat.

## Audience problem / desire

Audience mungkin ingin konten yang lebih dekat dengan masalah hariannya, tetapi kategori luas seperti “tips” atau “inspirasi” sulit dipilih. Empat opsi konkret membuat kebutuhan lebih mudah dikenali:

1. hijab lebih stay dan rapi;
2. padu padan warna;
3. memilih bahan;
4. framing sesuai gaya.

## Evidence boundary

- Fakta repo: Day 1–29 READY; belum ada publikasi Instagram atau baseline Insights yang tercatat.
- Observasi produksi: Poll memberi pilihan rendah-friksi; Questions memberi ruang kebutuhan yang tidak masuk empat opsi.
- Hipotesis: dua Poll konkret diikuti Questions sticker dapat menghasilkan input kalender yang lebih terstruktur daripada satu pertanyaan terbuka.
- Hasil: belum ada; paket belum dipublikasikan.

## Hook variants

1. **Bulan berikutnya, kamu yang pilih.**
2. Konten hijab berikutnya harus bahas apa?
3. Empat topik, dua pilihan, satu suara kamu.
4. Pilih masalah hijab yang paling ingin kamu bereskan.
5. Kalender berikutnya dimulai dari pilihanmu.

**Selected hook:** “Bulan berikutnya, kamu yang pilih.”  
**Rationale:** singkat, partisipatif, dan tidak menjanjikan hasil atau keputusan yang belum dibuat.

## Stories script / timing / shot list

| Frame | Suggested dwell | On-screen text | Native interaction | Visual |
|---:|---:|---|---|---|
| 1 | 5–7 s | **Bulan berikutnya, kamu yang pilih.** / Empat topik untuk konten Hijab Syari berikutnya. | None | Four-context editorial grid with strong headline |
| 2 | 6–8 s | **Mana yang paling ingin kamu bereskan?** / Hijab stay & rapi ↔ Padu padan warna | Poll: `STAY RAPI` / `PADU WARNA` | Two-panel controlled comparison |
| 3 | 6–8 s | **Mana yang paling ingin kamu pahami?** / Pilih bahan ↔ Framing gaya | Poll: `PILIH BAHAN` / `FRAMING GAYA` | Two-panel controlled comparison |
| 4 | 7–10 s | **Topik spesifik versimu?** / Tulis masalah, konteks, atau warna outfitmu. | Questions | Darkened editorial source + large sticker-safe card |

Poll and Questions stickers must be added natively when uploading. The rendered cards mark safe placement but do not imitate live sticker functionality.

## Visual direction

- Same adult Southeast Asian Muslim woman in all four panels.
- Opaque cocoa hijab and loose warm-stone abaya; full hair, ears, neck, shoulders, chest, and arm coverage.
- Four distinct actions: checking hijab stay, comparing colors, reading fabric/care information, and evaluating face framing.
- Realistic skin, hands, anatomy, fabric weave, paper label, mirror, and garment rail.
- Warm ivory, cocoa, taupe, muted sage, and dusty rose editorial palette.
- Strong mobile hierarchy and sticker-safe zones.
- No small category, series, production, day, or experiment label above the public headline.

## Prompt AI image

The exact ImageGen prompt and constraints are recorded in `PROMPTS.md`.

## Caption / CTA / keywords

Stories publishing copy is in `COPYWRITING.md`.

- **CTA:** “Pilih di dua Poll, lalu tulis topik spesifikmu di Questions.”
- **Keywords:** vote topik hijab, masalah hijab harian, padu padan hijab, pilih bahan hijab, framing hijab.
- **Hashtags:** Stories-first; no hashtag is required. Optional archive tags: `#HijabIndonesia #HijabTips #ModestFashion`.

## Stories derivative / follow-up

After actual responses exist:

1. export Poll counts and Questions replies;
2. code replies into `stay/rapi`, `warna/outfit`, `bahan/perawatan`, `framing/gaya`, and `other`;
3. publish a separate results recap only with verified counts;
4. turn the leading problem into a feed package without calling it a winner unless response volume and denominator are recorded.

No results-recap asset is finalized now because no responses exist.

## KPI / EXP-031

**Hypothesis:** two concrete binary Polls followed by one open Questions sticker will generate more classifiable next-topic input than a single broad Questions prompt.

- **Variable:** two-stage concrete voting + free-text follow-up.
- **Control:** one broad “Mau bahas apa?” Questions Story of comparable reach, if tested later.
- **Primary KPI:** Poll participation rate per frame when Insights are available.
- **Secondary KPI:** Questions reply rate, valid/classifiable reply count, completion from frame 1 to frame 4, exits, and next-topic conversion.
- **Guardrail:** Poll and Questions are different interaction types; do not compare raw counts without denominators.
- **Result:** none; not published.

## QA / release status

- [x] Four final Stories PNGs are 1080 × 1920.
- [x] ImageGen source is present and prompt-recorded.
- [x] Spelling, hierarchy, safe margins, sticker zones, and mobile readability checked.
- [x] Adult Muslim model, modest coverage, identity, anatomy, hands, skin, fabric, mirror, label, and rail checked.
- [x] No small label above the public headline.
- [x] No response, percentage, publication, performance, winner, trend, testimonial, or product claim.

## Files

- Stories: `assets/story-01.png` through `assets/story-04.png`
- ImageGen source: `assets/topic-vote-source.png`
- QA preview: `assets/contact-sheet.png`
- Editable renderer: `render.py`
- Copy: `COPYWRITING.md`
- Prompt record: `PROMPTS.md`
- Manifest: `ASSETS.md`

READY means upload-ready, not PUBLISHED. Add native stickers at upload and record dates, URLs, responses, and Insights only after evidence exists.
