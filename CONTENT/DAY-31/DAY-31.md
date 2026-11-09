# DAY 31 — Kacamata + hijab terasa bulky?

**Content ID:** `HS-FIX-006`  
**Production day:** Day 31  
**Production date:** 9 November 2026  
**Status:** READY — final Reel, cover, three Stories, ImageGen source, exact scenes, editable renderer, and QA previews are present; not published.  
**Format:** Instagram Reel, 15 seconds, plus cover and 3 Stories  
**Pillar:** Hijab Fix × Hijab 101  
**Primary objective:** Reach / non-follower discovery  
**Secondary objective:** Saves, completion, and problem-specific replies  
**Experiment:** `EXP-032`  
**Monetization:** OFF

## Objective

Memberi tiga titik pemeriksaan visual saat kacamata dan hijab terasa menumpuk—posisi gagang, volume di pelipis, dan arah drape—tanpa mengklaim satu styling cocok untuk semua frame, bentuk wajah, atau kebutuhan penglihatan.

## Audience problem / desire

Pengguna kacamata dapat merasa area pelipis terlihat atau terasa penuh ketika gagang bertemu beberapa lapis kain. Konten ini mengubah masalah umum tersebut menjadi urutan pemeriksaan yang sederhana sebelum mengganti seluruh gaya hijab.

## Evidence boundary

- Fakta anatomi frame: temple/arm adalah bagian panjang di sisi kacamata yang menuju area telinga; fit frame melibatkan hidung, telinga, dan pelipis.
- Observasi styling: lipatan kain, volume di pelipis, dan arah drape dapat dilihat dan dibandingkan.
- Hipotesis: urutan tiga titik plus movement check dapat membantu audience menemukan sumber bulk visual.
- Bukan diagnosis, resep frame, atau jaminan kenyamanan. Tekanan, kemerahan, nyeri, sakit kepala, atau masalah penglihatan perlu evaluasi profesional.

Research notes and official sources are recorded in `RESEARCH.md`.

## Hook variants

1. **Kacamata + hijab terasa bulky? Cek 3 titik ini.**
2. Area pelipis terasa penuh? Jangan langsung ganti hijab.
3. Hijab dan gagang kacamata bertumpuk? Mulai dari tiga cek ini.
4. Sebelum ubah styling, cek posisi gagang, volume, dan drape.
5. Kacamata tetap sama—rapikan tiga titik di sekitar hijab.

**Selected hook:** “Kacamata + hijab terasa bulky? Cek 3 titik ini.”  
**Rationale:** problem-first, menjanjikan tiga pemeriksaan spesifik, dan tidak menjanjikan hasil universal.

## Timed storyboard / shot list

| Time | Scene | On-screen text | Visual / motion |
|---:|---|---|---|
| 0.0–2.4 s | Hook | **Kacamata + hijab terasa bulky?** / Cek 3 titik ini. | Triptych, push-in halus |
| 2.4–5.2 s | Check 1 | **01 Posisi gagang** / Mulai dari satu lapis kain yang rata. | Close side panel, callout line |
| 5.2–8.0 s | Check 2 | **02 Volume di pelipis** / Kurangi lipatan yang menumpuk. | Front panel, controlled crop |
| 8.0–11.0 s | Check 3 | **03 Arah drape** / Rapikan samping, lalu tes menoleh. | Movement panel + three-step cue |
| 11.0–15.0 s | CTA | **Cek 30 detik** / pakai · menoleh · bicara / Bagian mana yang terasa penuh? | Triptych recap + hold |

## HyperFrames composition contract

- Canvas: 1080 × 1920.
- Duration: exactly 15.000 seconds.
- Frame rate: 30 fps; total 450 frames.
- Scene frame counts: 72, 84, 84, 90, 120.
- The playhead/frame index is the only timing source.
- Every frame reconstructs from source, scene index, and local progress.
- Motion vocabulary: restrained 0–1.8% push-in; no independent face, glasses, hand, or fabric animation.
- No wall-clock timers, autoplay state, random values, or network-dependent assets.
- Text stays inside mobile-safe margins and avoids eyes, glasses, and hands.
- If no current HyperFrames CLI/runtime is available, the same deterministic contract may be rendered with Pillow and FFmpeg. No HyperFrames CLI output is claimed without evidence.

## Visual direction

- Same adult Southeast Asian Muslim woman, identity, skin tone, glasses, hijab, expression, camera, and light.
- Opaque deep-taupe hijab with full hair, ears, neck, shoulders, and chest coverage.
- Loose warm-ivory abaya; no tight or transparent garment.
- Physically plausible tortoiseshell frame, lenses, hinges, bridge, and temple arms.
- Realistic skin, hands, anatomy, textile weave, folds, gravity, and glasses geometry.
- No small category, series, production, day, or experiment label above the public headline.

## Prompt AI image/video

The exact ImageGen prompt, motion boundaries, and negative constraints are in `PROMPTS.md`.

## Caption / CTA / search terms

Final publishing copy is in `COPYWRITING.md`.

- **CTA:** “Simpan tiga ceknya. Yang paling sering terasa penuh: gagang, pelipis, atau drape?”
- **Keywords:** kacamata dan hijab, hijab untuk pengguna kacamata, hijab bulky di pelipis, styling hijab berkacamata, hijab stay dengan kacamata.
- **Hashtags:** `#HijabBerkacamata #HijabTips #HijabFix #HijabIndonesia #ModestFashion`

## Stories derivative

1. Teaser: kacamata + hijab terasa menumpuk.
2. Poll native: `GAGANG` / `PELIPIS`.
3. Questions native: frame + masalah spesifik.

Poll and Questions stickers must be added natively at upload.

## KPI / EXP-032

**Hypothesis:** a three-point glasses-and-hijab diagnostic plus a 30-second movement check will produce stronger saves and problem-specific replies than a generic “thin your hijab folds” tip.

- **Variable:** named three-point diagnostic + movement check.
- **Control:** single-tip Reel of comparable duration and visual quality, if tested later.
- **Primary KPI:** 3-second view rate and average watch time when Insights are available.
- **Secondary KPI:** completion, replays, saves, shares, profile visits, comments naming one of the three points, Poll participation, and Questions replies.
- **Limitations:** frame size/weight/fit, prescription, face proportions, fabric, inner, drape, activity, and personal comfort vary.
- **Result:** none; not published.

## Claim boundaries

- “Bulky” describes visual or perceived layering; it is not a diagnosis.
- One flat layer is a styling starting point, not a rule for every hijab or frame.
- Do not bend or self-modify prescription frames based on this content.
- Persistent pressure, redness, pain, headache, or vision issues should be discussed with an optician, optometrist, or eye-care professional.
- AI imagery is editorial visualization, not a testimonial or documented product result.

## QA / release status

- [x] Final Reel 1080 × 1920, H.264/yuv420p, 30 fps, exactly 15.000 seconds / 450 frames.
- [x] Full video decode and frame-count checks passed.
- [x] Cover and three Stories PNGs are 1080 × 1920.
- [x] Indonesian spelling, hierarchy, safe area, and mobile readability checked.
- [x] Adult Muslim model; modest coverage, identity, anatomy, hands, skin, fabric, and glasses geometry checked.
- [x] No small label above the public headline.
- [x] No trend, product, publication, response, medical-result, or performance claim.

## Files

- Reel: `assets/reel-final.mp4`
- Cover: `assets/reel-cover.png`
- Stories: `assets/story-01.png` through `assets/story-03.png`
- Source: `assets/glasses-hijab-triptych.png`
- Exact scenes: `assets/scene-01-hook.png` through `assets/scene-05-cta.png`
- QA previews: `assets/contact-sheet.png`, `assets/stories-contact-sheet.png`
- Editable renderer: `render.py`
- Copy: `COPYWRITING.md`
- Prompt record: `PROMPTS.md`
- Research: `RESEARCH.md`
- Manifest: `ASSETS.md`

READY means upload-ready, not PUBLISHED. Add the posting date, Instagram URL, responses, and Insights only after evidence exists.
