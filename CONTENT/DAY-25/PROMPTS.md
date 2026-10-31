# DAY 25 — AI Prompt Record

## ImageGen final prompt

**Use case:** photorealistic-natural  
**Asset type:** source editorial comparison for an Instagram hijab material guide

Create one cohesive five-panel vertical editorial comparison, presented as five equal side-by-side full-height panels in a single wide image. The same adult Southeast Asian Muslim woman (late 20s) appears in every panel with identical facial identity, body proportions, neutral front-facing pose, camera height, framing, taupe hijab color, and modest cream abaya. Only the hijab textile surface and drape changes.

1. Matte, lightly crisp, structured plain-weave voal-like fabric with subtle fine weave.
2. Lightweight airy chiffon-like fabric, softly flowing, slightly translucent at the loose outer edge but fully opaque over hair, neck, chest, and shoulders using a matching opaque inner layer.
3. Soft stretch jersey knit, smooth matte surface, gentle rounded drape, no cling revealing body contours.
4. Satin-surface fabric with refined low-to-medium sheen, smooth elegant drape, never mirror-like or plastic.
5. Fine pebbled crepe texture, matte, softly weighted drape.

Seamless warm ivory studio; no props. Highly realistic natural fashion editorial photography. Five equal panels; waist-up; breathing room around head and shoulders; independent vertical crops. Identical soft diffused daylight and neutral white balance. Believable textile weave, seams, folds, gravity, weight, and edge behavior. Adult Muslim woman; fully modest coverage; hair, neck, chest, and shoulders covered; anatomically correct; natural hands preferably outside frame. No text, labels, logo, or watermark.

Avoid exposed hair or neck, tight clothing, transparent coverage zones, malformed anatomy, inconsistent identity, duplicate face, floating cloth, impossible folds, plastic sheen, excessive retouching, jewelry, random accessories, text, and watermark.

## Reuse boundary

- Use the source as editorial visualization only.
- Do not identify any panel as a verified product sample or exact fiber composition.
- Do not reuse for claims about breathability, temperature, allergies, durability, or care performance.
- Crop each panel independently; do not recolor in ways that alter the material comparison.

## Renderer

`render.py` deterministically composes the source into eight carousel PNGs, three Stories PNGs, and two contact sheets.
