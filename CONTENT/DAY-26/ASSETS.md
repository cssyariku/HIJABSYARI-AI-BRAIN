# Asset Manifest — Day 26

**Content ID:** `HS-INSPO-003`  
**Status:** READY; not published  
**QA date:** 1 November 2026

## Expected upload-ready set

- `assets/reel-final.mp4` — 1080 × 1920, H.264/yuv420p, 30 fps, 450 frames, 15.000 seconds, no audio.
- `assets/reel-cover.png` — 1080 × 1920.
- `assets/story-01.png` through `assets/story-03.png` — 1080 × 1920.
- `assets/monochrome-three-look-triptych.png` — ImageGen source.
- `assets/scene-01-hook.png` through `assets/scene-06-cta.png` — exact scene previews.
- `assets/contact-sheet.png` and `assets/stories-contact-sheet.png` — QA previews.

SHA-256 values are appended after final render and verification. AI imagery is editorial visualization, not product or testimonial evidence.

## SHA-256 inventory

| File | SHA-256 |
|---|---|
| `assets/reel-final.mp4` | `7419ca96d010f52935f2c99df7a1a54ece4e214cd58b9767a2e0ba65e36a51ee` |
| `assets/reel-cover.png` | `50a8c0435c8b57a910b50012b2a08062e4bdc20745350242809ffb4957a64aa6` |
| `assets/story-01.png` | `000dff5b3fbf0907db9f843e740ab68dbe96b29e1029efda02a0c752b22dbb9b` |
| `assets/story-02.png` | `9bc83c900fec5aed07ec0cad656a2ab7f647e62c7fdb5d884c6a73cdb8bbec1a` |
| `assets/story-03.png` | `e069585786b73a8690bcb7c5c38fdbe479ca62e2e3ad8ff38c93feb7b8cc77d8` |
| `assets/monochrome-three-look-triptych.png` | `5259db4adb112b0576bafe1549a349a9d0d04dd726b05b52840b029e1818642e` |
| `assets/scene-01-hook.png` | `dbef98d5e0d0995403b0013296c6ae7f8f166ce3666b9a7e8c8a6f38f8b7d84e` |
| `assets/scene-02-light.png` | `cfa797fe607cdc64f311ea769051439ae44bb36069951554a41b4b30909dbe30` |
| `assets/scene-03-soft.png` | `d1f36440f22e8a29946b7b9507ed76a19570fea19c9ea6c788285943930d38c8` |
| `assets/scene-04-deep.png` | `a934f3a37540ae24afe8fc3ac279ef5a7172750eaf09224bd345df9ad5e343ab` |
| `assets/scene-05-formula.png` | `c78bfdeb3eaec922f3de6754d8ef831105d1f44d649f990f9d7ed1b038ac7a03` |
| `assets/scene-06-cta.png` | `4e0923731d0b27d50e1898cc7caaa9bf0883c926598c67407b33c9c6b822ee0c` |
| `assets/contact-sheet.png` | `3b4976ca360dc08f5543bc89a43cfcf4aa390215466ca6a4ed21bde9ed714ffc` |
| `assets/stories-contact-sheet.png` | `0eec290a26c9c1dd7342ffc95ca82234927bf616d70b1a4384d0feb24ae5ce22` |

## QA evidence

- FFprobe: H.264, 1080 × 1920, yuv420p, 30 fps, 450 frames, 15.000 seconds.
- Full FFmpeg decode completed without error.
- Every final PNG opened successfully and matched its intended dimensions.
- Visual inspection passed for headline hierarchy, spelling, safe margins, mobile readability, adult Muslim model, opaque modest coverage, identity, anatomy, hands, fabric, accessories, footwear, and light–soft–deep separation.
- A first recap render cropped the outer looks too aggressively; the renderer was corrected to compose three independent vertical columns and all affected files were regenerated before release.
- No HyperFrames CLI output is claimed; Pillow and FFmpeg produced the verified final files from the HyperFrames deterministic composition contract.
