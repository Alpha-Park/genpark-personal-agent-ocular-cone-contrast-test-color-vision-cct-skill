"""
Example usage of Ocular Cone Contrast Test (CCT) Skill.
Demonstrates normal trichromacy vs isolated acquired S-cone (tritan) macular defect.
"""

import json
from client import ConeContrastTestClient


def main():
    print("=== Testing Ocular Cone Contrast Test (CCT) Skill ===")
    client = ConeContrastTestClient()

    # 1. Normal young trichromat (L=1.1%, M=1.3%, S=3.2% contrast thresholds -> Scores ~ 95-98)
    res_normal = client.evaluate_cct(
        l_cone_contrast_threshold_pct=1.1,
        m_cone_contrast_threshold_pct=1.3,
        s_cone_contrast_threshold_pct=3.2,
        age_years=28
    )
    print("\n[Case 1: Normal Trichromatic Cone Sensitivity]")
    print(json.dumps(res_normal, indent=2))

    # 2. Acquired tritan defect / early maculopathy (L and M normal ~ 1.2%, but S threshold severely elevated to 15.0% -> Score < 55)
    res_tritan = client.evaluate_cct(
        l_cone_contrast_threshold_pct=1.2,
        m_cone_contrast_threshold_pct=1.3,
        s_cone_contrast_threshold_pct=15.0,
        age_years=62
    )
    print("\n[Case 2: Isolated Acquired Tritan (S-Cone) Deficiency]")
    print(json.dumps(res_tritan, indent=2))

    # Assertions
    assert res_normal["scores"]["mean_cct_composite_score"] >= 75.0
    assert res_tritan["scores"]["s_cone_tritan_score"] < 60.0
    assert "Tritan" in res_tritan["evaluation"]["overall_diagnosis"]
    print("\n[SUCCESS] Cone Contrast Test (CCT) tests passed!")


if __name__ == "__main__":
    main()
