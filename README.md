# Ocular Cone Contrast Test (CCT) Skill

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-brightgreen.svg)](https://www.python.org/)
[![OpenClaw](https://img.shields.io/badge/ecosystem-OpenClaw-orange.svg)](https://openclaw.org/)
[![GenPark](https://img.shields.io/badge/sovereign-GenPark-purple.svg)](https://alphapark.ai/)
[![MCP](https://img.shields.io/badge/protocol-MCP-success.svg)](https://modelcontextprotocol.io/)

Cone Contrast Test (CCT) and Photoreceptor Contrast Sensitivity Analyzer based on Rabin cone isolation psychophysics.

```mermaid
flowchart TD
    A[Cone-Isolating Contrast Thresholds: L, M, S] --> B[Logarithmic Score Transformation: 0 - 100]
    B --> C[Compute Individual L, M, S Scores]
    C --> D{Score Threshold >= 75?}
    D -- All >= 75 --> E[Normal Trichromatic Photoreceptor Integrity]
    D -- S-cone < 60 --> F[Acquired Tritan / Macular / Glaucoma Defect]
    D -- L-cone < 60 --> G[Protan Selective Defect]
    D -- M-cone < 60 --> H[Deutan Selective Defect]
```

## Features
- **Zero PIP Dependencies**: Implemented strictly with Python Standard Library (`math`, `json`, `sys`, `typing`).
- **LMS Psychophysics**: Separates L, M, and S photoreceptor channels to detect subclinical maculopathies.
- **Rabin CCT Standardization**: Maps raw thresholds to calibrated 0-100 diagnostic scores.
- **Dual Architecture**: Native Python import and Model Context Protocol (MCP) JSON-RPC 2.0 stdio server.

## Quickstart
```bash
python example_usage.py
```

## License
Apache-2.0
