# DAY 33 — ASSET MANIFEST

Status aset: **READY**  
Format: Reel 15 detik + cover + 3 Stories  
Folder: `CONTENT/DAY-33/assets/`

## Set final

| File | Fungsi | Dimensi / durasi |
|---|---|---|
| `reel-final.mp4` | Video final unggah | 1080×1920, 15,000 detik, 30 fps |
| `reel-cover.png` | Cover Reel final | 1080×1920 |
| `story-01.png` | Stories pembuka | 1080×1920 |
| `story-02.png` | Stories poll | 1080×1920 |
| `story-03.png` | Stories question | 1080×1920 |
| `scene-01-hook.png` s.d. `scene-05-cta.png` | Frame sumber render | 1080×1920 per frame |
| `cheek-stay-triptych.png` | Raster AI sumber visual | 1672×941 |
| `contact-sheet.png` | Pratinjau kelima scene | 1080×464 |
| `stories-contact-sheet.png` | Pratinjau tiga Stories | 810×560 |

## Hash SHA-256

| File | SHA-256 |
|---|---|
| `cheek-stay-triptych.png` | `4650c364bcb6d051d22711e9c38d0399e8e61b0107ccfa9dd4696ab66d089c5b` |
| `contact-sheet.png` | `c9208928e1806734013cca3da0e64db1d742d7c68d2af0a9a7de839f8dac9e4e` |
| `reel-cover.png` | `cbb68f486a579d59cce729428e46eaaddfa974fa145d612269fb1efb5afd9e9e` |
| `reel-final.mp4` | `8713ac76504dc73db3ba292c61fde9caf3223e4bce8ea360b9a3388f01e402ff` |
| `scene-01-hook.png` | `2c9ad1bfa8d184d2cc3cb2bdb09bfb9cf0098c4165febb87d26c0891e2c8b62d` |
| `scene-02-garis-awal.png` | `d4c27f8ae42339401517c86ac843e71826b1ba16f9b71301c2e33601fb082af3` |
| `scene-03-lapisan.png` | `994b27afd0f291ab70419dd36be6e1958899a015f6b3fb84367cd06ac3c73c52` |
| `scene-04-arah-tarik.png` | `b60982a3582d2fb42cae2931aafe0ad5f9dce04563f1c40f1a20a445e16656d4` |
| `scene-05-cta.png` | `4cb7ed36f2105584f8b305131b62c6a4f611c762ca8aa56fe053a23750a0738c` |
| `stories-contact-sheet.png` | `7ccbb2cb5ee05d74839f0e55a6552d80e98f06de242cda2b82748b31e1ddfb26` |
| `story-01.png` | `44ee5fd8faea4dacaf5d0eae172e5355f7e47091feda67b222cc816e47ace8e3` |
| `story-02.png` | `273188a5a1e141ccfe22c22a67c6f4f124e9aa34afe88cae9a3b9c18c7e4583b` |
| `story-03.png` | `961d7d75aa6df51db56bafe2672003eefc72506f0036cb97c787ff767de6a64e` |

## Bukti QA

- `ffprobe`: H.264, 1080×1920, `yuv420p`, 30 fps, 450 frame, durasi tepat 15,000 detik.
- Decode penuh FFmpeg selesai tanpa error.
- Seluruh PNG lolos decode dan pemeriksaan dimensi.
- Contact sheet Reel dan Stories diperiksa visual: teks terbaca, kontras memadai, komposisi aman untuk layar vertikal, dan tidak ada label kecil kategori/series/produksi di atas headline.
- Model tampil sebagai perempuan Muslim dewasa dengan busana tertutup; kain, tangan, dan anatomi tampak realistis.
- Ejaan visual diperiksa: `Hijab nggak stay di area pipi?`, `Garis awal`, `Jumlah lapisan`, `Arah tarik & pengunci`, dan `Tes 30 detik`.
- Renderer deterministik tersedia di `render.py`. Video dibuat dengan Pillow + FFmpeg; paket ini tidak mengklaim keluaran dari CLI HyperFrames.

