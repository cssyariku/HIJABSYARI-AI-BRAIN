# Asset Manifest — Day 28

**Content ID:** `HS-FACE-004`  
**Status:** READY; not published  
**QA date:** 6 November 2026

## Expected upload-ready set

- `assets/reel-final.mp4` — 1080 × 1920, H.264/yuv420p, 30 fps, 450 frames, 15.000 seconds, no audio.
- `assets/reel-cover.png` — 1080 × 1920.
- `assets/story-01.png` through `assets/story-03.png` — 1080 × 1920.
- `assets/daily-formal-diptych.png` — ImageGen source.
- `assets/scene-01-hook.png` through `assets/scene-05-cta.png` — exact scene previews.
- `assets/contact-sheet.png` and `assets/stories-contact-sheet.png` — QA previews.
- `render.py` — editable deterministic Pillow/FFmpeg renderer.

## SHA-256 inventory

| File | SHA-256 |
|---|---|
| `assets/reel-final.mp4` | `3d8e7a82b8ed36a986ab2e8d3333d6cab02058b07e7b2bb4f9ed6fb849c2ad65` |
| `assets/reel-cover.png` | `3217e4f6f499079bf35d0ad6e14685435e579d1cabf95651d162c932dc27d5b2` |
| `assets/story-01.png` | `019e2f176038dba19f62d413639107ead20be24292b05086bcaf29fd8b3b16cd` |
| `assets/story-02.png` | `d693673da8662520c7cc3b8d9c91aa96373447b30e23fe735ad5f8acb5430bdf` |
| `assets/story-03.png` | `57eb2f8b8780567d42004cb6a66142eb6a035dd225fc44401009e622a0f125ee` |
| `assets/daily-formal-diptych.png` | `acf771d89279cd363126430c0f721eb6253cc430fe190d61192e0d4f49c8a9d3` |
| `assets/scene-01-hook.png` | `9a1269edce2a59d775071f32d8fc48d8b869f39080c6a534605bf65ab38312e7` |
| `assets/scene-02-daily.png` | `040dbd7a4f3581a16ff2ee9a05adb22020fdc7fd9daec9520ddf907a30fb819b` |
| `assets/scene-03-formal.png` | `1bcc7ac64a7e296a29f092718dfee5de79c660ec01ce8f92d0a03546da52caf1` |
| `assets/scene-04-framework.png` | `ae644e0b1f6b79bb6d770fab642706810c93cb3eab1ba3a5debccb24cd9ec125` |
| `assets/scene-05-cta.png` | `20413c71717810404930843551e91fb0a5f4319c4c8cd5cd2cb2e7185f4bdd8f` |
| `assets/contact-sheet.png` | `12fecb9af86837b9addd2cff1593391fcc60f1ef5a4cbdb17bb47a178a36ef4c` |
| `assets/stories-contact-sheet.png` | `cd2cbecf9e2e732f572b9acbcad30460dc4bb6f01ecca8e5164f94655fd96ea7` |

## QA evidence

- FFprobe: H.264, 1080 × 1920, yuv420p, 30 fps, 450 frames, 15.000 seconds.
- Full FFmpeg decode completed without error.
- Every final PNG opened successfully and matched its intended dimensions.
- Visual inspection passed for spelling, hierarchy, safe margins, mobile readability, adult Muslim model, opaque modest coverage, identity, anatomy, hands, skin, fabric, shoes, clutch, and daily/formal distinction.
- No HyperFrames CLI output is claimed; Pillow and FFmpeg produced the verified final files from the HyperFrames deterministic composition contract.
