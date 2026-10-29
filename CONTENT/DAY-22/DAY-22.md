# DAY 22 — Tiga opsi framing hijab untuk wajah square

**Content ID:** `HS-FACE-003`  
**Production day:** Day 22  
**Production date:** 29 October 2026  
**Status:** READY — final Reel, cover, Stories, source, keyframes, editable renderer, and QA previews are present; not published.  
**Format:** Instagram Reel, 15 seconds, plus cover and 3 Stories  
**Pillar:** Face & Style  
**Primary objective:** Reach / non-follower discovery  
**Secondary objective:** Completion, saves, and preference research  
**Experiment:** `EXP-023`  
**Monetization:** OFF

## Objective

Memberi tiga opsi framing hijab yang mudah dibedakan untuk proporsi wajah square—soft curve, clean line, dan relaxed frame—tanpa menyatakan bahwa satu gaya memperbaiki wajah atau lebih benar daripada yang lain.

## Audience problem / desire

Audience dengan garis rahang tegas sering menerima saran yang berorientasi “menyamarkan” atau “memperbaiki”. Konten ini menggantinya dengan tiga arah visual yang setara sehingga pilihan dapat didasarkan pada nuansa, bahan, dan kenyamanan pribadi.

## Opportunity score

| Dimension | Score | Rationale |
|---|---:|---|
| Hook | 4 | Bentuk wajah dan tiga opsi disebut langsung |
| Relevance | 4 | Framing hijab adalah kebutuhan styling berulang |
| Utility | 4 | Tiga opsi dapat dibandingkan dan dicoba |
| Saveability | 4 | Menjadi referensi visual |
| Shareability | 4 | Bahasa pilihan aman dibagikan |
| Visual potential | 5 | Perbedaan garis depan dan drape terbaca |
| Originality | 4 | Tidak memakai angle koreksi wajah |
| Feasibility | 5 | Triptych terkontrol dan render deterministik |
| **Total** | **34/40** | Di atas heuristic threshold 28/40 |

## Hook variants

1. **Wajah square? Coba 3 framing dengan nuansa berbeda.**
2. Garis rahang tegas, tiga opsi framing yang sama-sama valid.
3. Soft, clean, atau relaxed—kamu pilih yang mana?
4. Tiga framing hijab untuk wajah square, tanpa aturan wajib.
5. Satu wajah, satu hijab, tiga nuansa framing.

**Selected hook:** “Wajah square? Coba 3 framing dengan nuansa berbeda.”  
**Rationale:** Spesifik dalam dua detik pertama, menjanjikan perbandingan visual, dan tidak membawa asumsi korektif.

## Timed storyboard / shot list

| Time | Scene | On-screen text | Visual / motion |
|---:|---|---|---|
| 0.0–2.4 s | Hook | **Wajah square?** / Coba 3 framing dengan nuansa berbeda. | Look A, subtle 2.5% push-in |
| 2.4–5.4 s | Option A | **A — Soft curve** / Garis depan membulat lembut | Panel A, subtle push-in |
| 5.4–8.4 s | Option B | **B — Clean line** / Garis depan rapi dan terstruktur | Panel B, subtle push-in |
| 8.4–11.4 s | Option C | **C — Relaxed frame** / Drape samping lebih santai | Panel C, subtle push-in |
| 11.4–15.0 s | Recap / CTA | **Soft, clean, atau relaxed?** / Simpan referensinya. | Triptych recap, static-to-micro push |

## HyperFrames composition contract

- Canvas: 1080 × 1920.
- Duration: exactly 15.0 seconds at 30 fps = 450 frames.
- Scene frame counts: 72, 90, 90, 90, 108.
- The playhead/frame index is the only timing source.
- Every frame can be reconstructed from scene index and local frame progress.
- Motion vocabulary: restrained 0–2.5% push-in; no independent animation runtime.
- No `setTimeout`, `setInterval`, autoplay state, `Date.now()`, random values, or network-dependent assets.
- Text stays inside 72 px side margins and Instagram-safe top/bottom zones.
- If a HyperFrames CLI/runtime is unavailable, the same contract may be implemented deterministically with Pillow and FFmpeg. No HyperFrames CLI output may be claimed without evidence.

## Visual direction

- Vertical 1080 × 1920, warm ivory studio, soft diffused daylight.
- Same adult Southeast Asian Muslim woman with naturally square facial proportions in all panels.
- Same muted-rose matte hijab and loose cream abaya.
- Hair, ears, neck, shoulders, and chest fully covered.
- Only the face-framing line/drape changes:
  - A: gently rounded front edge;
  - B: neat, slightly straighter line;
  - C: softly loosened side drape.
- No beauty transformation, jaw reshaping, face slimming, or before/after implication.
- No small category, series, production, experiment, or day label above the public headline.

## AI image and image-to-video prompts

Exact prompts and invariants are stored in `PROMPTS.md`. The final video uses deterministic camera motion over the verified still source; it does not claim filmed model motion.

## Caption, CTA, keywords, hashtags

- Final caption: `COPYWRITING.md`
- CTA: “Simpan referensinya, lalu pilih: soft, clean, atau relaxed?”
- Keywords: framing hijab wajah square, hijab untuk garis rahang tegas, styling hijab wajah kotak, soft curve hijab, clean line hijab, relaxed hijab frame.
- Hashtags: `#HijabStyle #WajahSquare #StylingHijab #HijabIndonesia #TipsHijab`

## Stories derivative

1. Teaser: tiga framing pada model yang sama.
2. Poll: soft curve atau clean line.
3. Questions: A, B, atau C—dan konteks pemakaiannya.

Poll dan Questions ditambahkan native saat unggah.

## KPI / EXP-023

**Hypothesis:** Reel tiga opsi framing bernama dengan model dan styling terkontrol akan menghasilkan completion, saves, dan komentar pilihan yang lebih berguna daripada satu look dengan saran korektif.

- **Variable:** three named options + controlled comparison + recap A/B/C.
- **Control:** Face & Style Reel satu-look dengan durasi dan kualitas visual sebanding.
- **Primary KPI:** 3-second view rate dan average watch time, bila data tersedia.
- **Secondary KPI:** completion, replays, saves, shares, profile visits, komentar A/B/C, Poll participation, dan Questions replies.
- **Limitations:** cover, audio saat publikasi, distribusi, bahan kain, dan familiarity audience dapat memengaruhi respons; satu Reel tidak membuktikan sebab-akibat.
- **Result:** Belum ada; belum dipublikasikan.

## QA / release status

- [x] Reel final 1080 × 1920, H.264/yuv420p, 30 fps, exactly 15.0 seconds / 450 frames.
- [x] Full-decode video and frame-count checks passed.
- [x] Cover and three Stories PNGs at 1080 × 1920.
- [x] Indonesian spelling, hierarchy, safe area, and mobile readability checked.
- [x] Adult Muslim model; modest coverage, identity, face, anatomy, hands, skin, and fabric checked.
- [x] Model, outfit, lighting, camera, and hijab color/material remain controlled.
- [x] Three framing options remain visually distinct and equally valid.
- [x] No small label above the public headline.
- [x] No face-shaming, correction promise, trend claim, product claim, publication, or invented metric.

## Files

- Reel: `assets/reel-final.mp4`
- Cover: `assets/reel-cover.png`
- Stories: `assets/story-01.png` through `assets/story-03.png`
- Source: `assets/face-framing-square-triptych.png`
- Exact scenes: `assets/scene-01-hook.png` through `assets/scene-05-recap.png`
- QA previews: `assets/contact-sheet.png`, `assets/stories-contact-sheet.png`
- Editable renderer: `render.py`
- Copy: `COPYWRITING.md`
- Prompt record: `PROMPTS.md`
- Manifest: `ASSETS.md`

