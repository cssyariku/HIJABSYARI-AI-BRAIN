# DAY 14 — Visual and Motion Prompts

## ImageGen source prompt

**Use case:** `photorealistic-natural`  
**Asset type:** controlled source image for a 9:16 Instagram Color Lab Reel  
**Primary request:** one vertical editorial contact sheet divided into five equal horizontal panels showing the exact same adult Indonesian/Southeast Asian Muslim woman; the only changing element is hijab color  
**Panel order:** soft ivory, warm taupe, dusty rose, muted olive, deep burgundy  
**Wardrobe:** loose opaque longline medium-wash blue denim overshirt over an ivory high-neck inner and modest full-length silhouette  
**Hijab:** fully opaque matte woven fabric with complete hair, ears, neck, and chest coverage  
**Controlled variables:** exact identity, expression, pose, crop, camera, denim, background, light, exposure, and white balance  
**Style:** premium Indonesian modest-fashion editorial, natural skin, realistic weave, denim seams, folds, gravity, 50 mm lens  
**Constraints:** adult model; only face and hands visible; no text, labels, logo, watermark, jewelry, or props  
**Avoid:** identity/pose/crop/light drift, denim shift, outfit mutation, transparency, plastic skin, malformed hands, extra fingers, warped face, floating cloth, impossible folds, typography

## Deterministic motion specification

- Composition: 1080 × 1920, 30 fps, 17.00 sec.
- Playhead is the only timing source.
- Exact scene duration: 60, 66, 66, 66, 66, 66, 60, 60 frames.
- Motion vocabulary: 1.2% linear push-in and 6-frame cross-dissolve.
- No random values, wall-clock state, synthesized facial motion, autoplay media, or network assets.
- Each scene reconstructs correctly at any requested frame from its PNG source.
- Text remains inside safe areas and readable without audio.

## HyperFrames/runtime note

The HyperFrames skill guided the composition contract, storyboard, timing, seekability, and verification plan. No HyperFrames CLI/browser runtime was installed in the production environment. `render.py` therefore implements the same deterministic playhead contract with Pillow and FFmpeg; no HyperFrames CLI render is claimed.
