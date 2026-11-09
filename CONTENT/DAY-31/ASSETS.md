# Asset Manifest — Day 31

**Content ID:** `HS-FIX-006`  
**Status:** READY; not published  
**QA date:** 9 November 2026

## Expected upload-ready set

- `assets/reel-final.mp4` — 1080 × 1920, H.264/yuv420p, 30 fps, 450 frames, 15.000 seconds, no audio.
- `assets/reel-cover.png` — 1080 × 1920.
- `assets/story-01.png` through `assets/story-03.png` — 1080 × 1920.
- `assets/glasses-hijab-triptych.png` — ImageGen source.
- `assets/scene-01-hook.png` through `assets/scene-05-cta.png` — exact scene previews.
- `assets/contact-sheet.png` and `assets/stories-contact-sheet.png` — QA previews.
- `render.py` — editable deterministic Pillow/FFmpeg renderer.

## SHA-256 inventory

| File | SHA-256 |
|---|---|
| `assets/reel-final.mp4` | `6b11a94c3a3cabc1106575448a91ab2ffe0ebab660ca908cdf3fca86e308d6c0` |
| `assets/reel-cover.png` | `8fdd4549b4a8f55637038b2b806bb2bc5b9ce2f384a01a1f935511abbb506c8a` |
| `assets/story-01.png` | `1fa47046934943c9ab3d5a57177cac41d5f3b8e07a38ec9ab83cceae9cbc34a7` |
| `assets/story-02.png` | `25c228f5d97e8424b29eb3e1a8e6ad8231236e0ef6be32ab8853f02515397f72` |
| `assets/story-03.png` | `470edd2f1a0fd9a676697d042d456cd8990ffdd609b57f25e32da9555e51bdf3` |
| `assets/glasses-hijab-triptych.png` | `e8bb0050a44e809f4dbda6525b312d6c173e509c638ad6350bfac5cee4ba181b` |
| `assets/scene-01-hook.png` | `7f6fae10e0e7abd8e3cd399aab9106b545a5389b95c462357ea06012fbed6904` |
| `assets/scene-02-gagang.png` | `d259704c5f634ffb255f3a46fc16e578cf0ed270b4b40e5dcd9865367eb79554` |
| `assets/scene-03-pelipis.png` | `0f8ee55b3d1fc6c4083748eb5c321f2ae2da5fd1245a3526c52a0750a90f696a` |
| `assets/scene-04-drape.png` | `fe2a040b29e8144f68ac9ffc30a3977b0524127969f6123c7294952a4bc0546c` |
| `assets/scene-05-cta.png` | `f740daeb3ea882f53eeb56c0898d910f52dd2005a4d6ea502a1dba1847bcbcc4` |
| `assets/contact-sheet.png` | `9f47bffe67cc073cfe2014c4a642c80fbf78b20e3d20498baf2d3bc16e8ed28e` |
| `assets/stories-contact-sheet.png` | `80836162dd64aca2da5cc2b2614f566002f4d0c6d9827ecc254cf9650a653df0` |

## QA evidence

- FFprobe: H.264, 1080 × 1920, yuv420p, 30 fps, 450 frames, 15.000 seconds.
- Full FFmpeg decode completed without error.
- Every final PNG opened successfully and matched its intended dimensions.
- Visual inspection passed for spelling, hierarchy, safe margins, mobile readability, adult Muslim model, opaque modest coverage, identity, anatomy, hands, skin, fabric, lenses, bridge, hinges, temple arms, and source realism.
- No HyperFrames CLI output is claimed; Pillow and FFmpeg produced the verified final files from the deterministic composition contract.
