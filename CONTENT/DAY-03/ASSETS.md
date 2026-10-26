# ASSETS — DAY 03 · versi foto realistis

## Final

| File | Format | Fungsi |
|---|---|---|
| [reel_day3.mp4](assets/reel_day3.mp4) | MP4 1080 × 1920, 30 fps, 16 s | Reel utama |
| [cover_day3.png](assets/cover_day3.png) | PNG 1080 × 1920 | Cover unggahan |
| [story-01-poll.png](assets/story-01-poll.png) | PNG 1080 × 1920 | Poll setelah sticker native |
| [story-02-recap.png](assets/story-02-recap.png) | PNG 1080 × 1920 | Recap/share Reel |
| [story-03-question.png](assets/story-03-question.png) | PNG 1080 × 1920 | Questions setelah sticker native |
| [contact-sheet.jpg](assets/contact-sheet.jpg) | JPEG | QA delapan scene |

## Sumber produksi

Lima foto `photo-cream.jpg`, `photo-taupe.jpg`, `photo-mocha.jpg`, `photo-dusty-rose.jpg`, dan `photo-burgundy.jpg` adalah foto editorial yang dibuat dengan imagegen. Delapan `scene-*.jpg` adalah komposisi bertipografi yang dirender deterministik. [render.py](source/render.py) bisa menghasilkan ulang cover, scene, Stories, dan video dari kelima foto tersebut.

Versi motion graphic ilustratif sebelumnya tetap tersedia melalui riwayat commit GitHub; file final di folder ini sekarang menunjuk ke versi foto realistis.

## QA

- Foto sumber: satu model dewasa, outfit hitam longgar, rambut/leher/dada tertutup, pose dan latar konsisten.
- Warna hijab berubah tanpa klaim kesesuaian universal.
- Delapan scene diperiksa melalui contact sheet; cover memakai foto nyata secara visual, tanpa clip-art/manekin vektor.
- MP4 H.264, 1080 × 1920, 30 fps, 16,0 detik; video dibangun dari still AI dengan gerak kamera halus, bukan rekaman manusia bergerak.
- Tidak ada audio bawaan; teks terbaca tanpa audio.
- Status Instagram: belum diposting; tidak ada Insights yang dikarang.
