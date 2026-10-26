# DAY 19 — Asset Manifest

Status: READY. Final Reel, cover, Stories, source, exact scenes, editable renderer, and QA previews are present in this package. READY means upload-ready; it does not mean published.

## Final files
- `assets/reel-final.mp4`: 1080 × 1920, H.264/yuv420p, 30 fps, 15.0 seconds
- `assets/reel-cover.png`: 1080 × 1920 PNG
- `assets/story-01.png` through `assets/story-03.png`: 1080 × 1920 PNG
- `assets/scene-01-hook.png` through `assets/scene-05-recap.png`: exact scene/keyframe PNGs
- `assets/contact-sheet.png`: Reel scene QA preview
- `assets/stories-contact-sheet.png`: Stories QA preview
- `assets/clean-looks-triptych.jpg`: ImageGen editorial source
- `render.py`: deterministic Pillow/FFmpeg renderer

## Native Instagram elements
Add Poll to Story 2 and Questions to Story 3 natively. These stickers are intentionally not baked into the PNG.

## Runtime note
The HyperFrames skill defined the composition/timing contract. No local HyperFrames CLI or Chrome runtime was available; Pillow and FFmpeg produced the final deterministic render. No HyperFrames CLI output is claimed.

## Final QA — 26 October 2026
- Verified `reel-final.mp4`: H.264, yuv420p, 1080 × 1920, 30 fps, 15.000 seconds, exactly 450 frames.
- Full FFmpeg decode completed without errors.
- Verified cover, 3 Stories, and 5 exact scene PNGs decode at 1080 × 1920.
- Visually checked scene and Stories contact sheets plus full-size cover, soft-contrast scene, and recap.
- Passed: Indonesian spelling, mobile hierarchy, safe area, adult Muslim model, modest coverage, identity consistency, plausible hands/anatomy, realistic fabric, three-look differentiation, and CTA readability.
- No small category, series, day, or production label appears above the public-facing headline.
- Look names are editorial descriptors, not current-trend or universal-suitability claims.

## SHA-256
- `reel-final.mp4`: `739c23e71bf6bc7014b29097109f019df07cd673da4d3b57596bd7df960936fc`
- `reel-cover.png`: `8f69efea724c758fb41de4641e485c8cd60e1df115a5466227e611ea78cc22c2`
- `story-01.png`: `aec59851f1eb4c898c7bc2aa6aeeced4deb1d2385f30823559a278d6af3e374d`
- `story-02.png`: `e40fd92f6a428903df68c08a30656f8b08c0b703b37976cded4f66177e4de9ed`
- `story-03.png`: `aa81018ce7dbf2dd8b800e101807d32a041a9c777b75e596ce10518103861bcc`
- `scene-01-hook.png`: `5f8aa50240841434f8bcb318dac3c2e667db41ee1db2059923660216bd34fa90`
- `scene-02-light-minimal.png`: `6e88cfe20f27b678019dfe0695eba0ebf33df91b5fdb8001bc951bd050e2beaa`
- `scene-03-soft-contrast.png`: `89372879d2a38c5dc21de5e8bcd09b4b9d0f4667ea5f2d26129e534d5c840b99`
- `scene-04-deep-clean.png`: `ca26cda0ee1239f61cd8f51fa22044a9f12d58afc5606cc23ea38cb1c1724a8a`
- `scene-05-recap.png`: `cb62d6f8c12a96468e414969c6c7210c85a0df76a52b414bc6a7d2307f15e64d`
- `clean-looks-triptych.jpg`: `c3721dd7868efe241080df3e0cebc34cc98010ce3df6e198b3ca03840600ec7b`

