# DAY 16 — Asset Manifest

Status: READY. Final video, cover, Stories, source, keyframes, renderer, and QA previews are present in this package. READY means upload-ready; it does not mean published.

## Final publication assets
- `assets/reel-final.mp4`: 1080 × 1920, H.264/yuv420p, 30 fps, 15.0 seconds, no audio
- `assets/reel-cover.png`: 1080 × 1920
- `assets/story-01.png` through `assets/story-03.png`: 1080 × 1920

## Source and editable production
- `assets/face-framing-oval-triptych.jpg`: final ImageGen source
- `assets/scene-01-hook.png` through `assets/scene-05-cta.png`: exact Reel keyframes
- `render.py`: deterministic Pillow + FFmpeg renderer

## QA previews
- `assets/contact-sheet.png`: Reel keyframes
- `assets/stories-contact-sheet.png`: Stories

## QA result — 23 October 2026
- Reel: H.264/yuv420p, 1080 × 1920, 30 fps, 450 frames, exactly 15.0 seconds; full decode passed.
- Cover, three Stories, and five keyframes decoded successfully at 1080 × 1920.
- Spelling, hierarchy, safe area, mobile readability, and absence of small category/series/production labels above the headline were checked.
- Adult Muslim model, full modest coverage, identity consistency, facial anatomy, skin, and fabric folds were visually checked.
- Face-shape language is options-based; no correction, guaranteed result, trend, testimonial, publication, metric, or performance result is claimed.

## SHA-256
- `reel-final.mp4`: `bc1608ffed57cfa09e764e1de7b1963f375e3d917188fae7a7ce00bcfd5b9fcf`
- `reel-cover.png`: `89505aa2780be3405843abec32229f424b9d80f57b9561c0c11d9adb7b0d6123`
- `story-01.png`: `3818a161965160c58a123634fb7254df4827fb0fec02be4d16799a3c109d50df`
- `story-02.png`: `b3aedcb81698397b623d35eb31dcd17f58d62d31f6e861c877de545fce802c5b`
- `story-03.png`: `09a5d1c6dec070ab0a451ae593407eb61979966ead3b2a550d2071e3c6b3f33d`
- `face-framing-oval-triptych.jpg`: `403f96f1dd99443102f678b4c3acdbc3ef6296b1c1d083fb371a89ef5a522c90`

## Native Instagram elements
Add Poll natively to Story 2 (`A — SOFT` / `B — CLEAN`) and Questions natively to Story 3 (`A, B, atau C?`). These stickers are intentionally not baked into the PNG.

## Release note
The HyperFrames skill supplied the composition contract. No HyperFrames CLI/runtime was available, so the verified final render was produced deterministically with Pillow and FFmpeg; no HyperFrames CLI output is claimed.
