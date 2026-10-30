# DAY 23 — AI Visual Prompt

## Final ImageGen source prompt

**Use case:** `photorealistic-natural`  
**Asset type:** controlled editorial source for an Instagram carousel about hijab color pairing with a brown outfit.

Create one highly realistic five-panel fashion contact sheet with five equal vertical panels and narrow warm-ivory gutters. Show the exact same adult Southeast Asian Muslim woman, age 27–35, in every panel, photographed in the same warm-ivory studio with the same camera angle, pose, facial expression, lighting, and outfit. She wears a loose opaque cocoa-brown long-sleeve abaya with modest coverage. Only the hijab color changes: panel 1 soft warm cream; panel 2 muted dusty rose; panel 3 muted olive; panel 4 desaturated dusty slate blue; panel 5 deep burgundy.

Use natural skin texture, calm expression, anatomically correct hands, realistic matte woven fabric, believable folds and gravity. Each hijab must fully cover hair, ears, neck, shoulders, and chest. Preserve identical face, body proportions, pose, outfit, drape, crop, camera, and lighting across panels.

Avoid text, letters, logo, watermark, brand, labels, exposed hair/neck/chest, tight or transparent clothing, plastic skin, identity drift, malformed hands, extra fingers or limbs, floating fabric, impossible folds, dramatic makeup, jewelry, hyper-saturation, and synthetic AI appearance.

## Deterministic reuse rules

- Split the source into five equal vertical panels without stretching.
- Keep the cocoa-brown outfit visible in every crop.
- Do not recolor panels in the renderer; use the generated color variants as source evidence.
- Do not identify a shade as a specific commercial product.
- Add all text in the deterministic renderer, never in ImageGen.
- No small category, series, production, day, or experiment label appears above a public headline.

## Claim boundary

The five directions are editorial observations from a controlled visual. They are not proof of current trends, universal undertone suitability, exact product colors, or guaranteed real-world appearance. Screens, cameras, lighting, dye lots, weave, and finishing can affect perceived color.
