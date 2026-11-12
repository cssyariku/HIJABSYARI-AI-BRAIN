# DAY 33 — AI Prompt Record

## ImageGen source prompt

**Use case:** photorealistic-natural  
**Asset type:** controlled three-panel source for a 1080 × 1920 Instagram Reel about a hijab that does not stay neatly along the cheek area

Create one cohesive horizontal triptych with three equal vertical portrait panels. Show the exact same adult Southeast Asian Muslim woman, age 28–35, wearing the same opaque lightweight matte muted-mocha hijab and loose warm-ivory long-sleeve abaya.

- **Panel 1 — starting placement:** close three-quarter portrait while she gently checks the hijab edge beside one cheek; the edge is slightly loose but still modest, natural, and not exaggerated.
- **Panel 2 — fabric layers:** close front three-quarter portrait showing a smooth, flat inner layer and one outer hijab layer aligned beside the cheek, with no bulky stack.
- **Panel 3 — movement check:** waist-up portrait during a gentle head turn; the side drape remains balanced and she lightly checks the lower side edge with one natural hand.

Use a seamless warm-ivory editorial studio. Preserve identical facial identity, body proportions, pose family, camera height, lens, lighting, background, white balance, and garment. Keep enough independent crop space around head, shoulders, cheek edge, and hand. Use soft diffused daylight, natural skin texture, realistic matte textile weave, folds, seams, gravity, and edge behavior.

Keep hair, ears, neck, shoulders, and chest fully covered in all panels. Adult Muslim woman, modest opaque wardrobe, anatomically correct hands and fingers. No text, letters, numbers, logos, brands, or watermark.

## Negative constraints

No exposed hair/ears/neck/chest, tight or transparent clothing, beauty transformation, face reshaping, inconsistent identity, malformed hands, extra fingers, duplicated limbs, floating cloth, impossible folds, pins near skin, visible sharp objects, random jewelry, clutter, plastic skin, exaggerated distress, or fake typography.

## Motion boundaries

- Apply only a restrained 0–1.8% push-in to the still source.
- Do not independently animate eyes, face, hand, fabric, or background.
- Do not imply a product result, testimonial, medical result, or filmed before/after.
- All typography and scene changes are deterministic in `render.py`.

## Composition note

The HyperFrames contract defines deterministic, seekable timing. The local environment has no verified current HyperFrames CLI/runtime, so Pillow and FFmpeg implement the same frame-indexed contract. No HyperFrames CLI result is claimed.
