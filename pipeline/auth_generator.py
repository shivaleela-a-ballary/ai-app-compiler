import json
from pipeline.llm import generate_json


def generate_auth(intent):

    prompt = (
        "Generate realistic role-based access control.\n\n"
        + json.dumps(intent, indent=2)
        + """

Admin should have full permissions.
Users should have limited permissions.

Return ONLY valid JSON.

Format:

{
  "roles": {
    "admin": [],
    "user": []
  }
}
"""
    )

    return generate_json(
        prompt,
        {
            "roles": {
                "admin": [
                    "create",
                    "read",
                    "update",
                    "delete"
                ],
                "user": [
                    "read"
                ]
            }
        }
    )