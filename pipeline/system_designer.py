import json
from pipeline.llm import generate_json


def design_system(intent):

    prompt = (
        "You are a software architect.\n\n"
        "Given this application intent:\n\n"
        + json.dumps(intent, indent=2)
        + """

Generate ONLY valid JSON.

Return JSON in this format:

{
  "app_type": "",
  "entities": [
    {
      "name": "",
      "fields": []
    }
  ],
  "relationships": [
    {
      "source": "",
      "target": "",
      "type": ""
    }
  ]
}
"""
    )

    return generate_json(
        prompt,
        {
            "app_type": intent.get("app_type", "CRM"),
            "entities": [
                {
                    "name": "User",
                    "fields": [
                        "id",
                        "email",
                        "password",
                        "role"
                    ]
                }
            ],
            "relationships": []
        }
    )