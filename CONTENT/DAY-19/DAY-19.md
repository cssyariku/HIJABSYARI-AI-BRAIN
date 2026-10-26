# DAY 19 — Tiga clean hijab looks

**Content ID:** `HS-INSPO-002`  
**Production day:** Day 19  
**Production date:** 26 October 2026  
**Status:** READY — final Reel, cover, Stories, source, editable renderer, and QA previews are synced; not published.  
**Format:** Reel 15 seconds + cover + 3 Stories  
**Pillar:** Hijab Inspo  
**Primary objective:** Discovery / completion  
**Secondary objective:** Saves and preference comments  
**Experiment:** `EXP-020`  
**Monetization:** OFF

## Objective
Menampilkan tiga arah clean modest look yang mudah dibedakan—light minimal, soft contrast, dan deep clean—dalam Reel pendek yang cepat dipahami dan dapat disimpan sebagai referensi styling.

## Audience desire
Audience menginginkan tampilan rapi dan minimal tanpa semuanya harus putih atau beige. Mereka membutuhkan contoh full look yang konkret, tetapi tetap fleksibel untuk disesuaikan dengan isi lemari.

## Opportunity score

| Dimension | Score | Rationale |
|---|---:|---|
| Hook | 4 | Membantah asumsi clean look harus serba putih |
| Relevance | 4 | Mudah diterapkan pada wardrobe modest harian |
| Utility | 4 | Tiga formula warna dan siluet langsung terlihat |
| Saveability | 4 | Berfungsi sebagai referensi look |
| Shareability | 4 | Mudah dikirim sebagai inspirasi styling |
| Visual potential | 5 | Progression light–soft–deep kuat |
| Originality | 4 | Clean look dibagi menjadi tiga nuansa |
| Feasibility | 5 | Triptych terkontrol dan render deterministik |
| **Total** | **34/40** | Di atas heuristic threshold 28/40 |

## Hook variants
1. **Clean look nggak harus serba putih.**
2. Tiga clean hijab looks, tiga nuansa berbeda.
3. Mau clean look yang light, soft, atau deep?
4. Satu konsep clean, tiga arah warna.
5. Kalau kamu suka tampilan rapi dan minimal, pilih satu dari tiga look ini.

**Selected hook:** “Clean look nggak harus serba putih.”  
**Rationale:** Ringkas, memicu rasa ingin tahu, dan membuka variasi warna tanpa mengklaim tren.

## Timed storyboard / shot list

| Time | Scene | On-screen text | Visual / motion |
|---|---|---|---|
| 0.0–2.2 s | Hook | **Clean look nggak harus serba putih.** | Look B, slow push-in |
| 2.2–5.3 s | Look 1 | **01 Light minimal** / ivory + oatmeal | Look A, slow push-in |
| 5.3–8.4 s | Look 2 | **02 Soft contrast** / taupe + cream + sage | Look B, slow push-in |
| 8.4–11.5 s | Look 3 | **03 Deep clean** / charcoal + mocha | Look C, slow push-in |
| 11.5–15.0 s | Recap / CTA | **Light, soft, atau deep?** / Simpan referensinya. | Tiga look berdampingan |

## HyperFrames composition contract
- Canvas: 1080 × 1920, 30 fps, exactly 15.0 seconds / 450 frames.
- Playhead is the only timing source; every frame is reproducible from scene index and local frame progress.
- Five sequential scenes with explicit frame counts: 66, 93, 93, 93, 105.
- Motion vocabulary: one restrained 2.5% push-in per scene; no wall-clock timers, random values, autoplay state, or network dependency.
- Text remains within 72 px side margins and away from Instagram top/bottom UI zones.
- HyperFrames CLI/Chrome runtime is unavailable locally; the same deterministic contract is implemented by Pillow and FFmpeg. No HyperFrames CLI render is claimed.

## Visual direction
- Vertical 1080 × 1920, warm ivory studio, soft daylight.
- Same adult Southeast Asian Muslim woman, pose, camera, and lighting across three looks.
- Look 1: soft ivory hijab + oatmeal loose maxi dress.
- Look 2: warm taupe hijab + cream blouse + muted sage maxi skirt.
- Look 3: charcoal hijab + dark mocha loose abaya.
- Hijab matte and opaque, covering hair, ears, neck, shoulders, and chest.
- No small category, series, production, or day label above the headline.
- Visual is editorial inspiration, not a testimonial, product result, or trend claim.

## Caption, CTA, keywords, hashtags
- Final: `COPYWRITING.md`
- CTA: “Simpan referensinya, lalu pilih: light, soft, atau deep?”
- Keywords: clean hijab look, inspirasi hijab minimalis, modest outfit clean, ivory hijab outfit, taupe hijab sage outfit, charcoal hijab mocha abaya.
- Hashtags: `#HijabInspo #CleanHijabLook #ModestStyle #HijabIndonesia #OutfitHijab`

## Stories derivative
1. Teaser tiga clean looks.
2. Poll: light minimal atau deep clean.
3. Questions: look 1, 2, atau 3 dan konteks pemakaiannya.

Poll dan Questions ditambahkan secara native saat unggah.

## KPI dan EXP-020
**Hypothesis:** Tiga full look bernama dengan progression light–soft–deep akan menghasilkan completion, saves, dan preference comments yang lebih kuat daripada montage clean look tanpa label visual.

- **Variable:** named looks + controlled comparison + ordered progression.
- **Control:** Reel inspirasi tiga look tanpa nama/look descriptor dengan durasi serupa.
- **Primary KPI:** completion rate dan average watch time, bila data tersedia.
- **Secondary KPI:** saves, shares, replays, komentar pilihan, Poll participation, dan Questions replies.
- **Limitations:** Hook, audio, distribusi, wardrobe audience, dan preferensi warna dapat memengaruhi respons.
- **Result:** Belum ada; belum dipublikasikan.

## QA / release status
- [x] Reel final 1080 × 1920, H.264/yuv420p, 30 fps, 15.0 seconds / 450 frames.
- [x] Full-decode video berhasil.
- [x] Cover dan 3 Stories PNG, masing-masing 1080 × 1920.
- [x] Ejaan, hierarchy, safe area, dan keterbacaan mobile diperiksa.
- [x] Model perempuan Muslim dewasa; modest coverage, identitas, anatomi, tangan, dan kain diperiksa.
- [x] Tiga look berbeda jelas; tidak ada label kecil kategori/series/produksi di atas headline.
- [x] Tidak ada klaim tren, testimonial, hard selling, publikasi, atau metrik rekaan.

## Files
- Reel: `assets/reel-final.mp4`
- Cover: `assets/reel-cover.png`
- Stories: `assets/story-01.png` sampai `assets/story-03.png`
- Source: `assets/clean-looks-triptych.jpg`
- Exact scenes: `assets/scene-01-hook.png` sampai `assets/scene-05-recap.png`
- QA previews: `assets/contact-sheet.png`, `assets/stories-contact-sheet.png`
- Renderer: `render.py`
- Manifest: `ASSETS.md`

