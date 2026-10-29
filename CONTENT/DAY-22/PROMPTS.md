# DAY 22 — AI Visual and Motion Prompts

## Final ImageGen source prompt

Use case: photorealistic-natural. Asset type: controlled three-panel source for an Instagram Reel about optional hijab framing for a naturally square face.

Create one highly realistic premium editorial vertical triptych with three equal full-height panels. Show the exact same adult Southeast Asian Muslim woman, age 28–35, with a naturally square facial structure: a broad forehead, clear jawline, and balanced realistic proportions. The three panels present three equally valid hijab framing options, not a before/after and not a correction.

Use an identical warm-ivory studio, matte plaster wall, soft daylight, neutral gentle expression, posture, camera angle, focal length, crop, lighting, cream loose long-sleeve abaya, and matte opaque muted-rose hijab. Hair, ears, neck, shoulders, and chest are fully covered.

- Panel 1 — soft curve: gently rounded front edge following the forehead and cheek area, smooth low-volume drape.
- Panel 2 — clean line: neat, slightly straighter front edge, symmetrical structure, controlled folds.
- Panel 3 — relaxed frame: softly loosened face frame with subtle side drape and natural movement, still secure and modest.

Premium Indonesian modest-fashion editorial photography, natural skin texture, realistic textile weave, believable folds and gravity, accurate anatomy and hands. Vertical triptych with narrow ivory gutters; chest-up portrait; negative space for mobile text.

The only intentional variable is the hijab framing. Preserve exact face, outfit, hijab color/material, pose, camera, crop, and lighting. All options should look polished and equally attractive.

Avoid text, letters, numbers, logo, watermark, exposed hair/ears/neck/chest, tight or transparent clothing, altered face shape, face slimming, jaw reshaping, beauty-filter transformation, makeup changes, malformed hands, extra fingers, duplicated limbs, floating fabric, impossible folds, plastic skin, exaggerated jaw, distressed expression, clutter, and hyper-saturated AI appearance.

## Image-to-video / deterministic motion prompt

Animate each selected panel as a short editorial portrait while preserving the subject exactly. Use only a restrained 0–2.5% camera push-in. Preserve face shape, identity, skin tone, hijab framing, hijab color/material, outfit, body proportions, crop, and background.

Do not morph the face, reshape the jaw, change the front edge, reveal hair/ears/neck/chest, animate hands independently, alter folds, add accessories, change lighting, or introduce background movement.

## Implementation note

The final production uses the still source plus deterministic Pillow/FFmpeg camera movement. The prompt above records the intended motion boundary; no filmed model motion or image-to-video generation is claimed.

