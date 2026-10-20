# DAY 15 — Asset Manifest

Status: PARTIAL. Final raster assets were rendered locally and QA-checked, but PNG/JPEG binaries are not yet synced into GitHub because the available file-write action accepts UTF-8 text only.

- `assets/carousel-01.png` through `assets/carousel-08.png`: 1080 × 1350 PNG
- `assets/story-01.png` through `assets/story-03.png`: 1080 × 1920 PNG
- `assets/carousel-contact-sheet.png`: visual QA preview
- `assets/stories-contact-sheet.png`: visual QA preview
- `assets/undertone-portrait-source.jpg`: ImageGen editorial source
- `render.py`: deterministic Pillow renderer in the local package

Add Poll natively to Story 1 (`Ikuti warna outfit` / `Pilih warna yang kusuka`) and Questions natively to Story 3. Do not mark READY until final PNG/JPEG binaries are present in `CONTENT/DAY-15/assets/` and verified.