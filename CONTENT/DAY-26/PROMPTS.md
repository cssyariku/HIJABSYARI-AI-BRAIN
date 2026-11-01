# DAY 26 — AI Visual and Motion Prompts

## Final ImageGen prompt

**Use case:** `photorealistic-natural`  
**Asset type:** controlled triptych for a vertical Instagram Reel about monochrome modest outfits.

Create one cohesive wide triptych containing three equal vertical full-body editorial panels. Show the exact same adult Southeast Asian Muslim woman, age 27–35, with identical facial identity, height, body proportions, relaxed front-facing stance, camera height, focal length, studio, and lighting. Each panel is a complete modest monochrome look with intentional tonal layering; only the palette and garment styling change.

- Panel 1 — LIGHT MONOCHROME: opaque warm-ivory hijab with full hair/neck/chest coverage; loose oat-cream ankle-length abaya with subtle woven texture; minimal warm-beige structured tote; cream closed-toe flats.
- Panel 2 — SOFT MONOCHROME: opaque mushroom-taupe hijab with full coverage; loose taupe long tunic and flowing wide-leg trousers with non-clinging silhouette; small matte cocoa bag; taupe closed-toe flats.
- Panel 3 — DEEP MONOCHROME: opaque charcoal hijab with full coverage; loose graphite ankle-length abaya with subtle layering and matte fabric; minimal black structured bag; black closed-toe flats.

Seamless warm ivory studio, soft diffused daylight, neutral white balance, realistic natural Indonesian modest-fashion editorial photography. Equal vertical panels separated by narrow ivory gutters; full body visible head to shoes. Believable woven hijab and garment fabric, folds, gravity, seams, hems, footwear, bags, and natural hands.

Constraints: adult Muslim woman; fully modest loose wardrobe; hair, ears, neck, shoulders, chest, arms, and legs covered; same identity in all panels; no brands; no text, labels, logo, or watermark.

Avoid tight/transparent clothing, exposed hair/neck/ankles, malformed hands, extra fingers/limbs, inconsistent identity, duplicated accessories, floating fabric, impossible folds, plastic skin, mirror-like shine, excessive retouching, random jewelry, text, and watermark.

## Image-to-video / composition prompt

Create a deterministic 15-second 1080 × 1920 composition at 30 fps from the verified still triptych. Follow six scenes with frame counts 72, 81, 81, 81, 72, and 63. Use restrained 0–2.4% push-ins only. Present hook, light look, soft look, deep look, two-point formula, and CTA. Use warm cream text cards, dark brown typography, dusty-rose/taupe accents, safe margins, and exact on-screen copy from `COPYWRITING.md`.

## Motion boundary

- Camera motion over a still image only.
- Do not synthesize walking, lip movement, garment movement, or changing fabric state.
- Motion does not imply filmed testimony or product performance.
- Playhead-driven, deterministic, and seekable.
- No wall-clock animation, autoplay state, randomness, or network-dependent assets.
- Do not claim a HyperFrames CLI render unless a real runtime output is produced and verified.

## Reuse rules

- Split the source into three equal panels without stretching.
- Preserve face, coverage, anatomy, garment silhouettes, accessories, fabric colors, and lighting.
- Add text only in the deterministic renderer.
- Keep planning labels out of public visuals.
