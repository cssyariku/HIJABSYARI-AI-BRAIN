# Asset Manifest — Day 22

**Content ID:** `HS-FACE-003`  
**Status:** READY; not published  
**QA date:** 29 October 2026

## Final deliverables

| File | Use | Specification | SHA-256 |
|---|---|---|---|
| `assets/reel-final.mp4` | Final Reel | 1080 × 1920, H.264, yuv420p, 30 fps, 450 frames, 15.000 sec, no audio | `266a39c357e0c500eb2bdf49d1d33dc450f3e318c05b311a98b4de241786dfee` |
| `assets/reel-cover.png` | Reel cover | 1080 × 1920 PNG | `1ec26f178cb701bae12825bbe977ff129910cb0b010ee611121fa10b9af77d34` |
| `assets/story-01.png` | Stories derivative 1 | 1080 × 1920 PNG | `94ff2c911bf4b11854e09d79bde5d5e248b22d2401317d82e113ac4e32e34580` |
| `assets/story-02.png` | Stories derivative 2 | 1080 × 1920 PNG; add Poll natively | `dde36d15b3d403450da1071a247552a999ac87a887aa5ed11db3461c1b4f0d5d` |
| `assets/story-03.png` | Stories derivative 3 | 1080 × 1920 PNG; add Questions sticker natively | `cd5379aab3429f30423dc18fdc3944f1e831bca143db925f9dd7b2fa7cfcc5b2` |

## Source, exact scenes, and previews

| File | Purpose | SHA-256 |
|---|---|---|
| `assets/face-framing-square-triptych.png` | Controlled ImageGen source; three styling options | `3537e486b2a3828023c17dcbd1e72b1f1bdeeaf371662f1e884b21c823b5f76b` |
| `assets/scene-01-hook.png` | Exact hook scene | `9f422bb881ba25dcbafce62d95061f1a4fcf6b35f57077dca84e415d33e046cb` |
| `assets/scene-02-soft-curve.png` | Exact option A scene | `2e0b4d69a9997e92761ff4360d1d7749a4b728469090427f76e34defc810a886` |
| `assets/scene-03-clean-line.png` | Exact option B scene | `b793512154c5b82e0d2d779426c0b578422210a9bb7f0edee8149be41870269a` |
| `assets/scene-04-relaxed-frame.png` | Exact option C scene | `12d331a617e45b62a1f16d0fbc87eba7dc08893bc2e64ef4b775a2c09b6b99e6` |
| `assets/scene-05-recap.png` | Exact recap scene | `2a13a64686001b57f3d198c55be4586a944c3264a4ca2eb56065637fbbc629bb` |
| `assets/contact-sheet.png` | Five-scene QA preview, 1350 × 480 | `5bb396baa059c8334c7f7281de22f284fede3dc830fafb951e60f46b207aa94b` |
| `assets/stories-contact-sheet.png` | Three-Story QA preview, 810 × 480 | `1318abc83dabd3058c303b599a74daaf830933ecc35978b9da4d697507671d5c` |

## Reproducibility

- `render.py` builds the final video, cover, Stories, exact scenes, and previews from the controlled source.
- The HyperFrames skill informed the deterministic 1080 × 1920 / 30 fps / 450-frame composition contract. A HyperFrames CLI/Chrome runtime was not available, so Pillow and FFmpeg produced the verified final files; no HyperFrames CLI output is claimed.
- Motion is limited to a subtle deterministic crop/zoom over still editorial imagery. It does not imply filmed model motion, a testimonial, or product performance.

## QA evidence

- FFprobe: H.264, 1080 × 1920, yuv420p, 30 fps, 15.000 seconds, 450 decoded frames.
- Full FFmpeg decode completed without error.
- Every final PNG opened and passed Pillow checksum verification.
- Visual inspection passed for headline hierarchy, spelling, mobile readability, safe margins, adult Muslim model, modest opaque wardrobe, realistic anatomy/fabric, consistent identity/lighting/outfit, and distinct A/B/C framing.
- No small category, series, or production label appears above the visual headline.
- The original incomplete-checksum cover detected during QA was regenerated and re-verified before release.
- Publication remains unverified; no Instagram URL, Insights, or metric is recorded.
