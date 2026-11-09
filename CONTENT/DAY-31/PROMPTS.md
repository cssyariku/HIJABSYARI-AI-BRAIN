# DAY 31 — AI Prompt Record

## ImageGen source prompt

Use case: photorealistic-natural. Asset type: controlled three-panel source for a 1080 × 1920 Instagram Reel about wearing eyeglasses with hijab without excessive bulk.

Create one highly realistic premium editorial triptych with three equal vertical portrait panels. Show the exact same adult Southeast Asian Muslim woman, age 28–35, wearing the same lightweight matte deep-taupe hijab, loose warm-ivory long-sleeve abaya, and simple medium-size dark tortoiseshell prescription eyeglasses.

- Panel 1 — temple arm position: close three-quarter side view showing the arm resting naturally over one smooth hijab layer.
- Panel 2 — temple volume: clean front three-quarter frame with controlled low volume around both temples.
- Panel 3 — movement check: waist-up portrait during a gentle head turn, eyeglasses level and drape balanced.

Preserve identical identity, frame, wardrobe, camera, light, and color. Keep hair, ears, neck, shoulders, and chest fully covered. Maintain physically plausible lenses, bridge, hinges, temple arms, hands, skin, fabric weave, folds, and gravity.

## Negative constraints

No text, letters, numbers, logos, brands, watermark, exposed hair/ears/neck/chest, tight or transparent clothing, warped lenses, duplicate glasses, impossible hinges, temple arms crossing through fabric, malformed hands, extra fingers, duplicated limbs, inconsistent identity, face slimming, beauty transformation, floating fabric, plastic skin, glamour pose, distress, clutter, or hyper-saturated AI styling.

## Motion boundaries

- Apply only restrained 0–1.8% push-in to the still source.
- Do not animate eyes, face, glasses, hands, fabric, or background independently.
- Do not imply a medical result, product result, testimonial, or filmed before/after.
- All typography and scene changes are deterministic in `render.py`.

## Composition note

The HyperFrames contract defines deterministic, seekable timing. If no current HyperFrames CLI/runtime is available, Pillow and FFmpeg may implement the same frame-indexed contract; no HyperFrames CLI result may be claimed without evidence.
