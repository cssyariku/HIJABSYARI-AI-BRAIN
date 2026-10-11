# DAY 06 — Tiga opsi framing hijab untuk wajah bulat

**Content ID:** `HS-FACE-001`  
**Production day:** Day 6  
**Production date:** 11 October 2026  
**Status:** READY — final Reel, cover, Stories, and copy complete; not published  
**Format:** Instagram Reel, 15 seconds, plus 3 Stories  
**Pillar:** Face & Style  
**Primary objective:** Reach / non-follower discovery  
**Monetization:** OFF

## Objective dan audience problem

Memberi tiga opsi framing hijab yang mudah dibedakan tanpa memperlakukan wajah bulat sebagai kekurangan. Audience sering menemukan bahasa styling yang korektif atau aturan tunggal, padahal hasil visual juga dipengaruhi bahan, ketebalan lipatan, inner, kacamata, dan kenyamanan pribadi.

Konten ini adalah visualisasi editorial, bukan diagnosis bentuk wajah atau janji bahwa satu gaya pasti memberi hasil yang sama pada semua orang.

## Opportunity score

| Dimension | Score | Rationale |
|---|---:|---|
| Hook | 5 | Membantah rasa kurang percaya diri, lalu langsung menawarkan utility |
| Relevance | 4 | Face framing adalah kebutuhan styling yang berulang |
| Utility | 4 | Tiga opsi dapat langsung dibandingkan dan dicoba |
| Saveability | 4 | Referensi praktis untuk sesi styling berikutnya |
| Shareability | 4 | Bahasa afirmatif membuatnya aman dibagikan |
| Visual potential | 5 | Perbedaan framing terlihat dalam format Reel |
| Originality | 4 | Menjauh dari format “kesalahan wajah” yang menghakimi |
| Feasibility | 5 | Satu identitas model, tiga framing, timeline deterministik |
| **Total** | **35/40** | Di atas heuristic threshold 28/40 |

## Hook variants

1. **Wajah bulat bukan masalah. Coba 3 framing ini.**
2. Ubah framing, bukan wajahmu.
3. Tiga cara mengatur framing hijab—efek visualnya berbeda.
4. Kalau wajahmu cenderung bulat, kamu tim A, B, atau C?
5. Bukan aturan bentuk wajah: ini 3 opsi framing.

**Selected hook:** #1. Cepat dipahami, afirmatif, dan menjelaskan manfaat dalam dua kalimat pendek.

## Script, timing, dan shot list

| Time | Scene | On-screen text | Shot / motion |
|---:|---|---|---|
| 0.0–2.0s | Hook | Wajah bulat bukan masalah. / Coba 3 framing ini. | Medium close-up, gentle push-in |
| 2.0–5.5s | Opsi 1 | 1 Soft open / Garis depan rileks, volume samping ringan. | Panel A, slow push-in |
| 5.5–9.0s | Opsi 2 | 2 Gentle structure / Sedikit tinggi di atas, jatuh seimbang di sisi. | Panel B, slow push-in |
| 9.0–12.5s | Opsi 3 | 3 Vertical drape / Jatuh memanjang dengan volume samping rendah. | Panel C, slow push-in |
| 12.5–15.0s | CTA | Mana yang paling kamu suka? / A, B, atau C | Three-look recap, save/comment CTA |

Voice-over tidak diperlukan. Gunakan musik berlisensi dari Instagram saat unggah jika diinginkan; file final sengaja tanpa audio agar tidak membawa risiko lisensi.

## Visual direction

- 1080 × 1920, 30 fps, warm editorial neutral.
- Model perempuan Muslim Asia Tenggara dewasa, satu identitas konsisten, outfit modest, hijab opaque menutup rambut, leher, dan dada.
- Perbedaan difokuskan pada garis depan dan volume kain, bukan manipulasi anatomi wajah.
- Logo asli digunakan; tidak ada label kecil kategori, series, atau produksi di atas headline.
- Tipografi cream–charcoal dengan kontras tinggi dan safe area mobile.
- Gerak berupa gentle push-in agar perbandingan tetap mudah dipindai.

## Prompt AI image final

**Built-in ImageGen / use case `photorealistic-natural`:**

> Create a photorealistic editorial triptych source image for an Indonesian modest-fashion Instagram Reel. A single adult Southeast Asian Muslim woman with natural round facial proportions appears consistently in exactly three equal vertical portrait panels, same identity, warm ivory long-sleeve blouse, warm taupe opaque hijab, beige studio background and lighting. Panel 1: soft open framing, relaxed front edge, low side volume. Panel 2: gently structured framing, subtle height at crown, balanced side drape. Panel 3: elongated vertical drape lines, low side volume. All are equally valid styling options. Hijab fully covers hair, ears, neck, and chest. Realistic fabric folds, skin texture, facial anatomy, and camera angle. No text, labels, logo, watermark, exposed hair/neck, distorted features, extra people, or beauty-filter look.

**Source asset:** [face-framing-triptych.png](assets/face-framing-triptych.png).

## Image-to-video / render direction

Create a deterministic 15-second 9:16 sequence at 30 fps from the five keyframes above. Use a restrained 1.0×→1.025× push-in per scene, hard scene changes at the stated timestamps, no face morphing, no generative motion, no extra limbs or fabric changes, and no audio. Preserve the exact on-screen typography and safe margins. Export H.264, `yuv420p`, 1080 × 1920, fast-start MP4.

HyperFrames CLI was checked but was not available in the runtime. The included [render.py](render.py) therefore implements the same explicit timeline and deterministic frame generation with Pillow + FFmpeg. The final MP4 is present and QA-verified; this is not a partial package.

## Caption, CTA, keywords, hashtags

- **Final caption and publishing copy:** [COPYWRITING.md](COPYWRITING.md).
- **Natural CTA:** “Kamu paling ingin mencoba A, B, atau C? Simpan dulu untuk sesi styling berikutnya.”
- **Keywords:** framing hijab wajah bulat, styling hijab, bentuk wajah bulat, soft framing hijab, structured hijab, vertical drape.
- **Hashtags:** `#StylingHijab #HijabWajahBulat #TipsHijab #HijabIndonesia #GayaHijab`.

## Stories derivative

1. Teaser: wajah bulat bukan masalah; tiga framing memberi efek visual berbeda.
2. Poll: A soft open atau B gentle structure.
3. Questions: framing A/B/C dan bahan hijab yang biasa dipakai.

Tambahkan stiker Poll dan Questions secara native saat unggah di ruang yang disediakan.

## KPI dan experiment

- **Primary KPI:** 3-second view rate and average watch time, only after actual Insights are available.
- **Secondary KPI:** completion rate, replays, shares, saves, profile visits, comments A/B/C, Story Poll participation, and Questions responses.
- **Experiment tag:** `EXP-007` — affirmative/options-based framing hook versus the usual corrective “mistakes” framing.
- **Interpretation rule:** do not attribute performance to the hook alone unless topic, length, format, and distribution conditions are reasonably comparable.
- **Baseline:** not established; no target, winner, or performance label is inferred.

## QA / release status

- Final Reel: 1080 × 1920, 30 fps, exactly 15.0 seconds, H.264/yuv420p; full decode check passed.
- Cover and three Stories: 1080 × 1920 PNG; spelling, hierarchy, safe margins, and mobile readability checked.
- Adult Muslim model, modest wardrobe, opaque chest-covering hijab, realistic fabric and facial anatomy checked.
- Identity, outfit, lighting, and camera angle are sufficiently consistent for editorial comparison.
- No face-shaming, medical/beauty promise, trend claim, testimonial, hard selling, affiliate, or invented metric.
- **Not published to Instagram.** Publication date, URL, and Insights remain empty.

## Files

- Final Reel: [reel-final.mp4](assets/reel-final.mp4)
- Reel cover: [reel-cover.png](assets/reel-cover.png)
- Stories: [assets/](assets)
- QA preview: [contact-sheet.png](assets/contact-sheet.png)
- Editable renderer: [render.py](render.py)
- Final copy: [COPYWRITING.md](COPYWRITING.md)

