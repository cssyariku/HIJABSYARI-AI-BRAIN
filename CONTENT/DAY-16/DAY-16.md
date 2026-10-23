# DAY 16 — Tiga opsi framing hijab untuk wajah oval

**Content ID:** `HS-FACE-002`  
**Production day:** Day 16  
**Production date:** 23 October 2026  
**Status:** READY — final Reel, cover, Stories, source, renderer, and QA previews are synced; not published.  
**Format:** Instagram Reel, 15 seconds, plus cover and 3 Stories  
**Pillar:** Face & Style  
**Primary objective:** Reach / non-follower discovery  
**Secondary objective:** Completion, saves, shares, and audience preference research  
**Experiment:** `EXP-017`  
**Monetization:** OFF

## Objective
Memberi tiga opsi framing hijab yang mudah dibedakan untuk proporsi wajah oval, tanpa menyatakan bahwa wajah oval wajib memakai gaya tertentu atau bahwa satu opsi lebih benar.

## Audience problem / desire
Audience sering menerima klaim bahwa wajah oval “cocok dengan semua gaya”, tetapi tetap membutuhkan contoh visual yang spesifik. Konten ini mengubah generalisasi tersebut menjadi tiga pilihan yang dapat dibandingkan berdasarkan nuansa visual, bahan, dan kenyamanan pribadi.

## Opportunity score

| Dimension | Score | Rationale |
|---|---:|---|
| Hook | 4 | Menjawab kebutuhan yang spesifik dalam dua detik pertama |
| Relevance | 4 | Face framing adalah kebutuhan styling yang berulang |
| Utility | 4 | Tiga opsi dapat langsung dibandingkan dan dicoba |
| Saveability | 4 | Menjadi referensi saat styling |
| Shareability | 4 | Bahasa pilihan aman dibagikan |
| Visual potential | 5 | Perbedaan garis depan dan jatuh kain jelas |
| Originality | 4 | Menghindari klaim “satu gaya terbaik” |
| Feasibility | 5 | Satu identitas model, tiga framing, timeline deterministik |
| **Total** | **34/40** | Di atas heuristic threshold 28/40 |

## Hook variants
1. **Wajah oval? Coba 3 framing dengan nuansa berbeda.**
2. Wajah oval bukan berarti harus pakai satu gaya.
3. Soft, clean, atau relaxed—kamu pilih framing yang mana?
4. Tiga framing hijab untuk wajah oval, tanpa aturan wajib.
5. Garis depan yang berbeda bisa mengubah nuansa look.

**Selected hook:** “Wajah oval? Coba 3 framing dengan nuansa berbeda.”  
**Rationale:** Spesifik, langsung menawarkan perbandingan visual, dan tidak menjanjikan koreksi bentuk wajah.

## Script, timing, dan shot list

| Time | Scene | On-screen text | Shot / motion |
|---:|---|---|---|
| 0.0–2.0s | Hook | Wajah oval? / Coba 3 framing dengan nuansa berbeda. | Look B, gentle push-in |
| 2.0–5.5s | Opsi A | A — Soft curve / Garis depan membulat, kesannya lebih lembut. | Panel A, slow push-in |
| 5.5–9.0s | Opsi B | B — Clean angle / Sudut ringan, kesannya lebih rapi. | Panel B, slow push-in |
| 9.0–12.5s | Opsi C | C — Relaxed drape / Bukaan lebih rileks, jatuh kain memanjang. | Panel C, slow push-in |
| 12.5–15.0s | Recap / CTA | A, B, atau C? / Pilih yang nyaman dan sesuai bahan hijabmu. | Three-look recap, static cards |

Voice-over tidak diperlukan. Gunakan musik berlisensi dari Instagram saat unggah bila diinginkan; file final sengaja tanpa audio.

## Visual direction
- 1080 × 1920, 30 fps, warm cream editorial system.
- Satu perempuan Muslim Asia Tenggara dewasa dengan proporsi wajah oval alami.
- Identitas, outfit, warna hijab, kamera, dan pencahayaan konsisten; hanya garis depan dan drape yang berubah.
- Hijab opaque menutup rambut, telinga, leher, dan dada; blouse longgar dan modest.
- Gerak hanya gentle push-in 1.0×→1.025× agar identitas dan kain tidak berubah.
- Headline langsung tampil tanpa label kategori, series, atau produksi kecil di atasnya.

## AI source prompt
Lihat `PROMPTS.md`. Source final: `assets/face-framing-oval-triptych.jpg`.

## Image-to-video / render direction
Gunakan timeline deterministik 15 detik pada 30 fps. Setiap scene berasal dari keyframe statis dengan push-in halus, hard cut sesuai timestamp, tanpa face morphing, generative motion, perubahan warna hijab, atau gerak kain yang tidak konsisten.

Kontrak HyperFrames digunakan untuk dimensi, durasi, seekability, safe area, scene timing, dan determinisme. Karena CLI/runtime HyperFrames tidak tersedia di lingkungan produksi, `render.py` merealisasikan kontrak yang sama memakai Pillow dan FFmpeg. Tidak ada output CLI HyperFrames yang diklaim.

## Caption, CTA, keywords, hashtags
- Final: `COPYWRITING.md`
- CTA: “Kamu paling ingin mencoba A, B, atau C? Simpan dulu untuk sesi styling berikutnya.”
- Keywords: styling hijab wajah oval, framing hijab, hijab wajah oval, soft curve hijab, clean angle hijab, relaxed drape.
- Hashtags: `#StylingHijab #HijabWajahOval #TipsHijab #HijabIndonesia #GayaHijab`

## Stories derivative
1. Teaser tiga framing setara untuk wajah oval.
2. Poll A soft curve vs B clean angle.
3. Questions A/B/C dan bahan hijab yang biasa dipakai.

Stiker Poll dan Questions ditambahkan secara native saat unggah pada ruang yang disediakan.

## KPI dan EXP-017
**Hypothesis:** Reel tiga opsi yang diberi nama dan dibandingkan secara terkontrol akan menghasilkan completion, saves, dan komentar pilihan yang lebih berguna daripada satu look tanpa pembanding.

- **Variable:** tiga framing bernama + recap A/B/C.
- **Control:** Reel Face & Style satu-look dengan durasi dan kualitas visual sebanding.
- **Primary KPI:** 3-second view rate dan average watch time, jika tersedia.
- **Secondary KPI:** completion, replays, saves, shares, profile visits, komentar A/B/C, Poll participation, dan Questions replies.
- **Limitations:** Topik, cover, distribusi, bahan kain, dan familiarity audience dapat memengaruhi hasil; satu post tidak membuktikan sebab-akibat.
- **Result:** Belum ada; belum dipublikasikan.

## QA / release status
- [x] Reel final 1080 × 1920, 30 fps, tepat 15.0 detik, H.264/yuv420p.
- [x] Full decode dan frame-count check berhasil.
- [x] Cover dan 3 Stories PNG: 1080 × 1920.
- [x] Ejaan, hierarchy, safe area, dan keterbacaan mobile diperiksa.
- [x] Model perempuan Muslim dewasa; coverage, anatomi, kulit, dan kain diperiksa.
- [x] Identitas, outfit, lighting, dan kamera konsisten untuk perbandingan.
- [x] Tidak ada label kecil kategori/series/produksi di atas headline.
- [x] Tidak ada face-shaming, janji transformasi, klaim tren, hard selling, atau metrik rekaan.
- [x] Belum dipublikasikan ke Instagram.

## Files
- Reel: `assets/reel-final.mp4`
- Cover: `assets/reel-cover.png`
- Stories: `assets/story-01.png` sampai `assets/story-03.png`
- Source: `assets/face-framing-oval-triptych.jpg`
- Keyframes: `assets/scene-01-hook.png` sampai `assets/scene-05-cta.png`
- QA previews: `assets/contact-sheet.png`, `assets/stories-contact-sheet.png`
- Renderer: `render.py`
- Asset manifest: `ASSETS.md`

