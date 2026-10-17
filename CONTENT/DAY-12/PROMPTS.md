# DAY 12 — Visual and Motion Prompts

## ImageGen source prompt

**Use case:** `photorealistic-natural`  
**Asset type:** controlled source image for an Instagram Reel comparing hijab colors near the face  
**Primary request:** one vertical editorial contact sheet showing the same adult Indonesian/Southeast Asian Muslim woman in four equal stacked portrait panels  
**Scene:** warm ivory minimalist studio  
**Wardrobe:** identical cream long-sleeved abaya and opaque, full-coverage hijab  
**Colors from top:** muted peach/apricot, dusty rose, muted teal, soft ivory  
**Controlled variables:** exact same identity, pose, crop, expression, outfit, camera, lighting, exposure, and background; only hijab color changes  
**Style:** natural editorial photography, realistic skin, textile weave, folds, and gravity  
**Constraints:** adult model, modest coverage, no text, labels, logo, or watermark  
**Avoid:** identity drift, beauty-filter skin, exposed hair/neck, transparent fabric, malformed anatomy, lighting drift, garment mutation, floating fabric, impossible folds, props, typography

## Motion prompt / production direction

Create a 16-second vertical Reel at 1080 × 1920 and 30 fps. Use subtle 1–1.2% push-ins and short crossfades. Keep the first frame legible in under two seconds. Preserve the same model and do not synthesize facial movement. Text must remain readable without sound.

HyperFrames/Chrome was unavailable in the production runtime. The final video was rendered deterministically with `render.py`, Pillow, and FFmpeg from the approved stills; no HyperFrames output is claimed.
