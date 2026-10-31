# Asset Manifest — Day 24

**Content ID:** `HS-FIX-005`  
**Status:** READY; not published  
**QA date:** 31 October 2026

## Upload-ready deliverables

| File | Use | Specification | SHA-256 |
|---|---|---|---|
| `assets/reel-final.mp4` | Final Reel | 1080 × 1920, H.264, yuv420p, 30 fps, 450 frames, 15.000 sec, no audio | `de43e03180fd8fb7885592ec3b7b8a581990afc01c5a4caaef6d2aec73c23b93` |
| `assets/reel-cover.png` | Reel cover | 1080 × 1920 PNG | `98315cf0332481af149950486fac30158c876c2af5060e79df6c41e9b1a54098` |
| `assets/story-01.png` | Stories derivative 1 | 1080 × 1920 PNG | `7622151148938db2ee4e480780ee241f03d500fb9b5d06bded5f2fcf112e6668` |
| `assets/story-02.png` | Stories derivative 2 | 1080 × 1920 PNG; add Poll natively | `b8203a465b2f4e72d8e19eec7fd67df9f72f9f14f29caefeddc9836e3712b43e` |
| `assets/story-03.png` | Stories derivative 3 | 1080 × 1920 PNG; add Questions natively | `47f8252d0e70e44917d38ecf724157973f9cf9e8f6515d16352f59e81362ace6` |

## Source, exact scenes, and previews

| File | Purpose | SHA-256 |
|---|---|---|
| `assets/pashmina-shift-three-checks.png` | Controlled ImageGen triptych | `ca43892021fa594ec0ba2a51a8deea29a40125953739c1c040f6f7d63db3a94d` |
| `assets/scene-01-hook.png` | Exact hook scene | `4c84292393171831e2cbdeacaca23094fedc1be3bc01a913156fb40abc2dabcb` |
| `assets/scene-02-surface.png` | Surface-pairing scene | `f928221b62fc599f5db3538b81db2613e66271945ec45f14e3a3208a46d2d69f` |
| `assets/scene-03-anchor.png` | Anchor-position scene | `4c43e356a501b5ba822740787f5972ba8a85dfe235e2885d2629b86414f81903` |
| `assets/scene-04-balance.png` | Length/drape scene | `e1edfe8b24555e92c8c008ff5e1fd7faac1e86f85ace32380b790ab1e4f79486` |
| `assets/scene-05-test.png` | 30-second test scene | `d163a4c87e9ff987cb1d5fabe06f1bad41ca3036b7016047a32998f9a52c1c65` |
| `assets/scene-06-cta.png` | CTA scene | `e8a838d7fe2de2cbbd6f83972bbeb77eafcb24f6118d20f08c3f97091d6f0735` |
| `assets/contact-sheet.png` | Six-scene QA preview, 1620 × 480 | `a955583b430628b674ecad5d45cf31fda5f74935a741f733e2ff80097d775f44` |
| `assets/stories-contact-sheet.png` | Three-Story QA preview, 810 × 480 | `84a89229b54c7a9f65184dae829f158574b1a7f8df53de1caa571c488f25f9d1` |

## Reproducibility

- `render.py` rebuilds the video, cover, Stories, exact scenes, and previews from the triptych.
- The HyperFrames skill defined the deterministic 1080 × 1920 / 30 fps / 450-frame composition contract.
- A HyperFrames CLI/Chrome runtime was not available, so Pillow and FFmpeg produced the verified final files. No HyperFrames CLI output is claimed.
- Motion is limited to deterministic still-image push-ins; it does not imply filmed movement, testimony, or product performance.

## QA evidence

- FFprobe: H.264, 1080 × 1920, yuv420p, 30 fps, 15.000 seconds, 450 decoded frames.
- Full FFmpeg decode completed without error.
- Every PNG opened and passed Pillow checksum verification.
- Visual inspection passed for headline hierarchy, spelling, safe margins, mobile readability, adult Muslim model, opaque modest coverage, consistent identity/outfit/lighting, realistic anatomy/hands/fabric, appropriate magnet placement, and distinct diagnostic actions.
- No small category, series, production, day, or experiment label appears above a public headline.
- Claims remain conditional; no product endorsement, universal fix, publication, response, Insight, or metric is recorded.
