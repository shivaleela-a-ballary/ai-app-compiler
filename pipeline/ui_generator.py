import json
from pipeline.llm import generate_json


def generate_ui(architecture):

    prompt = (
        "Generate UI schema.\n\nArchitecture:\n\n"
        + json.dumps(architecture, indent=2)
        + """

Return ONLY valid JSON.

Format:

{
  "pages": [
    {
      "name": "",
      "components": []
    }
  ]
}
"""
    )

    return generate_json(
        prompt,
        {
            "pages": [
                {
                    "name": "Dashboard",
                    "components": [
                        "Navbar",
                        "Sidebar",
                        "Table"
                    ]
                }
            ]
        }
    )