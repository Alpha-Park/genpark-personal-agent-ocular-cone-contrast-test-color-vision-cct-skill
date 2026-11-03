---
name: genpark-personal-agent-ocular-cone-contrast-test-color-vision-cct-skill
description: Cone Contrast Test (CCT) color vision analyzer based on Rabin cone contrast psychophysics. Computes isolated L-cone, M-cone, and S-cone contrast sensitivity thresholds and color contrast indices.
version: 1.0.0
author: GenPark Ecosystem
license: Apache-2.0
tags:
  - personal-agent
  - optometry
  - color-vision
  - cone-contrast
  - cct
  - photoreceptors
  - openclaw
  - genpark
  - mcp
---

# Ocular Cone Contrast Test (CCT) Skill

## Overview
This skill computes isolated cone photoreceptor contrast thresholds using Rabin psychophysical principles:
- **Cone Isolation**: Stimuli are modulated along cone-isolating directions in LMS color space, exciting one cone class while holding excitation of the other two constant.
- **Three Chromatic Pathways**:
  - **L-cone (Protan)**: Long-wavelength photoreceptors ($\approx 560\text{ nm}$).
  - **M-cone (Deutan)**: Medium-wavelength photoreceptors ($\approx 530\text{ nm}$).
  - **S-cone (Tritan)**: Short-wavelength photoreceptors ($\approx 420\text{ nm}$).
- **Early Disease Sensitivity**: Tritan defects occur early in ocular hypertension, glaucoma, diabetic retinopathy, and toxic retinopathies before high-contrast visual acuity is affected.

## Mathematical Formulation
1. **Cone Contrast Metric (Weber Contrast)**:
   $$C = \frac{L_{\text{stim}} - L_{\text{bg}}}{L_{\text{bg}}} \times 100\%$$
2. **CCT Score Transformation**:
   $$\text{Score} = \max\left(0, \min\left(100, 100 - 55 \times \log_{10}\left(\frac{\text{Threshold}}{\text{Threshold}_{\text{ideal}}}\right)\right)\right)$$

## Usage
```python
from client import ConeContrastTestClient

client = ConeContrastTestClient()
res = client.evaluate_cct(
    l_cone_contrast_threshold_pct=1.1,
    m_cone_contrast_threshold_pct=1.3,
    s_cone_contrast_threshold_pct=3.2
)
print(res["scores"]["mean_cct_composite_score"])
```
