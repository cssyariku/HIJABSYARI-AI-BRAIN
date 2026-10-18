# Prompts — Day 13

## ImageGen source prompt

Create one vertical editorial fashion photograph, 1024x1536, for an Indonesian modest-fashion educational carousel. No text, no logos, no watermark.

Subject: one adult Indonesian/Southeast Asian Muslim woman, approximately late 20s, wearing an elegant fully modest cream abaya and a white hijab. A fully opaque warm-beige inner cap and neck covering must completely cover hair, ears, neck, upper chest and all skin beneath the outer hijab; only face and hands visible. Outer white hijab drapes to mid-chest with realistic woven fabric texture and gravity, loose and non-form-fitting.

Composition: three-quarter portrait, subject placed on the RIGHT half of frame, leaving generous clean negative space on the LEFT for typography. Bright minimal studio with warm ivory plaster wall. Strong diffused window light comes from behind-right, making the edge and one single-layer fold of the outer white hijab subtly luminous so the beige inner layer is faintly visible as a soft tone—educationally showing sheerness while preserving complete modest coverage. Front fill light keeps face natural and readable. The effect must be subtle, tasteful, realistic, and not expose hair, neck, chest, or body silhouette.

Style: premium Indonesian modest fashion editorial, photorealistic, calm, airy, neutral palette, fine fabric weave, realistic hands and anatomy, natural skin texture, 50mm lens, soft shadows, high dynamic range, no exaggerated beauty retouching.

Avoid: child or teen, transparent clothing over bare skin, visible hair, visible neck, tight clothing, cleavage, body outline, incorrect anatomy, extra fingers, duplicated limbs, warped face, floating fabric, plastic texture, text, labels, product packaging, jewelry clutter, black hijab, busy background.

## Reproduction notes

- Generated source: `assets/white-hijab-source.png`.
- Deterministic layout source: `render.py`.
- Final raster files are rendered directly from the source image and vector-like Pillow shapes/text.
- Do not add a category, series, or production label above the cover headline.

## Research sources and claim boundary

1. Datacolor, “What Are Light Blocking and Sheerness in Textiles and How Are They Measured?” — distinguishes transmitted light from perceived sheerness and lists construction, yarn density, color, stretching, viewing conditions, and background contrast as factors: https://www.datacolor.com/business-solutions/blog/measure-lightblocking-sheerness-textiles/
2. Ray et al. (2022), “Solar Radiation Transmittance Characteristics of Textile Fabrics Used for Greenhouse,” notes relationships between woven-fabric areal density, thickness, cover factor, and transmittance: https://link.springer.com/article/10.1007/s40034-021-00223-3
3. Kostajnšek et al. (2021), “Optical Assessment of Porosity Parameters in Transparent Woven Fabrics,” studies fabric pore structure using light penetration: https://pmc.ncbi.nlm.nih.gov/articles/PMC7865968/

These sources support the general explanation, not a performance claim about a specific hijab product or named fabric. Practical tests in the carousel are editorial guidance, not laboratory measurements.
