"""
Ocular Cone Contrast Test (CCT) Photoreceptor Sensitivity Client.
Zero-mock pure Python standard library implementation.
Calculates isolated L-cone (protan), M-cone (deutan), and S-cone (tritan)
contrast thresholds and CCT score indices based on Rabin psychophysical cone isolation principles.
"""

import math
from typing import Dict, Any, Optional


class ConeContrastTestClient:
    """
    Evaluates isolated cone photoreceptor contrast sensitivity:
    - L-cone (Long-wavelength / Red / Protan axis)
    - M-cone (Medium-wavelength / Green / Deutan axis)
    - S-cone (Short-wavelength / Blue / Tritan axis)
    Standard CCT Score: Normal healthy score is >= 75 - 100 on each cone axis.
    """

    def __init__(self):
        pass

    def evaluate_cct(
        self,
        l_cone_contrast_threshold_pct: float,
        m_cone_contrast_threshold_pct: float,
        s_cone_contrast_threshold_pct: float,
        age_years: Optional[int] = 30
    ) -> Dict[str, Any]:
        """
        Calculates CCT score (0 - 100 scale) for each cone class.
        Thresholds in percent Weber contrast (0.5% - 25.0%).
        Higher contrast needed to detect stimulus -> Lower CCT Score.
        Standard Rabin CCT score formula:
        CCT_Score = max(0, min(100, 100 - (log10(Threshold / Threshold_ideal) * 50)))
        """
        if l_cone_contrast_threshold_pct <= 0 or m_cone_contrast_threshold_pct <= 0 or s_cone_contrast_threshold_pct <= 0:
            raise ValueError("Cone contrast thresholds must be strictly positive.")

        # Ideal thresholds in young healthy trichromats:
        # L-cone: ~1.0% contrast
        # M-cone: ~1.2% contrast
        # S-cone: ~3.0% contrast (due to lower foveal S-cone density)
        ideal_l = 1.0
        ideal_m = 1.2
        ideal_s = 3.0

        score_l = max(0.0, min(100.0, 100.0 - (math.log10(l_cone_contrast_threshold_pct / ideal_l) * 75.0)))
        score_m = max(0.0, min(100.0, 100.0 - (math.log10(m_cone_contrast_threshold_pct / ideal_m) * 75.0)))
        score_s = max(0.0, min(100.0, 100.0 - (math.log10(s_cone_contrast_threshold_pct / ideal_s) * 75.0)))

        mean_cct_score = (score_l + score_m + score_s) / 3.0

        # Clinical evaluation of cone dysfunctions:
        # CCT score >= 75: Normal trichromatic color vision
        # CCT score 60 - 74: Mild cone contrast deficiency / subclinical photoreceptor fatigue
        # CCT score < 60: Clinically significant dyschromatopsia (hereditary or acquired)
        def classify_cone(score: float, name: str) -> str:
            if score >= 75.0:
                return f"Normal {name} Sensitivity"
            elif score >= 60.0:
                return f"Mild {name} Contrast Attenuation"
            else:
                return f"Significant {name} Deficiency"

        l_status = classify_cone(score_l, "L-cone (Protan)")
        m_status = classify_cone(score_m, "M-cone (Deutan)")
        s_status = classify_cone(score_s, "S-cone (Tritan)")

        # Pattern identification:
        # Isolated S-cone drop: Early glaucoma, macular degeneration, diabetes, optic neuritis
        # L/M cone drop: Congenital protan/deutan deficiency or high-altitude/toxic exposure
        # Diffuse drop: Severe retinal toxicity, advanced maculopathy
        if score_l >= 75.0 and score_m >= 75.0 and score_s >= 75.0:
            overall_diagnosis = "Normal Trichromatic Photoreceptor Integrity"
            suspected_etiology = "Optimal cone opsin density and foveal signaling."
        elif score_s < 60.0 and score_l >= 70.0 and score_m >= 70.0:
            overall_diagnosis = "Isolated Tritan (S-Cone) Deficiency / Acquired Dyschromatopsia"
            suspected_etiology = "Early macular stress, elevated IOP / glaucoma, or retinal metabolic strain."
        elif score_l < 60.0 and score_m >= 70.0:
            overall_diagnosis = "Protan (L-Cone) Selective Defect"
            suspected_etiology = "Protanomaly / protanopia or red-channel photoreceptor fatigue."
        elif score_m < 60.0 and score_l >= 70.0:
            overall_diagnosis = "Deutan (M-Cone) Selective Defect"
            suspected_etiology = "Deuteranomaly / deuteranopia or green-channel photoreceptor fatigue."
        else:
            overall_diagnosis = "Pancromatic Cone Photoreceptor Attenuation"
            suspected_etiology = "Generalized foveal photoreceptor degradation or optic neuropathy."

        return {
            "status": "success",
            "scores": {
                "l_cone_protan_score": round(score_l, 1),
                "m_cone_deutan_score": round(score_m, 1),
                "s_cone_tritan_score": round(score_s, 1),
                "mean_cct_composite_score": round(mean_cct_score, 1)
            },
            "thresholds_pct": {
                "l_cone": l_cone_contrast_threshold_pct,
                "m_cone": m_cone_contrast_threshold_pct,
                "s_cone": s_cone_contrast_threshold_pct
            },
            "evaluation": {
                "overall_diagnosis": overall_diagnosis,
                "suspected_etiology": suspected_etiology,
                "cone_breakdown": {
                    "protan": l_status,
                    "deutan": m_status,
                    "tritan": s_status
                }
            }
        }
