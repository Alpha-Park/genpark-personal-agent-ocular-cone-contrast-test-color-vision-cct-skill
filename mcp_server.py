"""
MCP Server for Ocular Cone Contrast Test (CCT) Skill.
Conforms to Model Context Protocol (MCP) JSON-RPC 2.0 stdio specification.
"""

import sys
import json
from client import ConeContrastTestClient


def handle_request(line: str) -> None:
    try:
        req = json.loads(line)
    except Exception:
        return

    req_id = req.get("id")
    method = req.get("method")
    params = req.get("params", {})

    if method == "initialize":
        response = {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {
                    "name": "genpark-personal-agent-ocular-cone-contrast-test-color-vision-cct-skill",
                    "version": "1.0.0"
                }
            }
        }
        sys.stdout.write(json.dumps(response) + "\n")
        sys.stdout.flush()
    elif method == "tools/list":
        response = {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "evaluate_cct",
                        "description": "Calculate Rabin Cone Contrast Test (CCT) scores for L, M, and S cones to evaluate color vision and photoreceptor health.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "l_cone_contrast_threshold_pct": {"type": "number", "description": "L-cone contrast detection threshold (%)."},
                                "m_cone_contrast_threshold_pct": {"type": "number", "description": "M-cone contrast detection threshold (%)."},
                                "s_cone_contrast_threshold_pct": {"type": "number", "description": "S-cone contrast detection threshold (%)."},
                                "age_years": {"type": "integer", "description": "Subject age in years (default: 30)."}
                            },
                            "required": [
                                "l_cone_contrast_threshold_pct",
                                "m_cone_contrast_threshold_pct",
                                "s_cone_contrast_threshold_pct"
                            ]
                        }
                    }
                ]
            }
        }
        sys.stdout.write(json.dumps(response) + "\n")
        sys.stdout.flush()
    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})
        if tool_name == "evaluate_cct":
            client = ConeContrastTestClient()
            try:
                res = client.evaluate_cct(
                    l_cone_contrast_threshold_pct=float(args["l_cone_contrast_threshold_pct"]),
                    m_cone_contrast_threshold_pct=float(args["m_cone_contrast_threshold_pct"]),
                    s_cone_contrast_threshold_pct=float(args["s_cone_contrast_threshold_pct"]),
                    age_years=int(args.get("age_years", 30))
                )
                response = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "content": [{"type": "text", "text": json.dumps(res, indent=2)}]
                    }
                }
            except Exception as e:
                response = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": {"code": -32000, "message": str(e)}
                }
            sys.stdout.write(json.dumps(response) + "\n")
            sys.stdout.flush()
    else:
        response = {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {"code": -32601, "message": f"Method {method} not found"}
        }
        sys.stdout.write(json.dumps(response) + "\n")
        sys.stdout.flush()


def main():
    for line in sys.stdin:
        if line.strip():
            handle_request(line)


if __name__ == "__main__":
    main()
