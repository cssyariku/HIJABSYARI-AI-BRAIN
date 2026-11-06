# DAY 28 — AI Prompt Record

## ImageGen source prompt

Use case: photorealistic-natural. Asset type: controlled editorial source image for a 1080 × 1920 Instagram Reel about daily versus formal hijab styling. Create one high-resolution photorealistic editorial diptych with two equal vertical panels showing the same adult Southeast Asian Muslim woman, late 20s to early 30s, as two equally valid modest styling directions. Use an identical warm off-white seamless studio, soft neutral daylight, camera distance, full-body three-quarter standing pose, realistic identity, skin tone, expression, hand placement, body proportions, scale, and background.

Panel A — DAILY: simple relaxed opaque oatmeal-beige hijab with a soft matte woven appearance, clean uncomplicated front framing, long chest coverage, loose sage-grey ankle-length tunic over matching wide-leg trousers, flat closed shoes, minimal practical styling, no jewelry.

Panel B — FORMAL: refined opaque deep-cocoa hijab with a smooth satin-matte appearance (not glossy), slightly more structured clean front fold and long chest coverage, loose warm-taupe floor-length abaya with subtle tailored seam detail, closed low-heel shoes, small plain clutch, no jewelry.

Both outfits cover all hair, ears, neck, shoulders, chest, arms, and legs. Garments are loose, opaque, and non-bodycon. Preserve realistic facial detail, skin, hands, anatomy, textile weave, folds, gravity, hems, footwear, and clutch. Keep the styling contemporary, practical, premium, and approachable.

## Negative constraints

No embedded text, letters, numbers, logos, watermark, product packaging, sheer fabric, tight clothing, uncovered hair, ears, neck or chest, childlike model, beauty-filter skin, warped hands, duplicated limbs, impossible folds, floating fabric, glamour pose, excessive accessories, bridal styling, gala gown, extreme shine, or inconsistent identity, exposure, scale, light, or camera between panels.

## Image-to-video / motion boundaries

- Apply only restrained 0–1.8% push-in motion to the still source.
- Do not animate the model, face, hands, fabric, clutch, shoes, or background independently.
- Do not imply filmed movement, real product use, a testimonial, or a before/after result.
- All typography and scene changes are created deterministically in `render.py`.

## Composition note

The HyperFrames skill defines the deterministic, seekable composition contract. If the current CLI/runtime is unavailable, Pillow and FFmpeg may implement the same frame-indexed contract; no HyperFrames CLI result may be claimed without evidence.
