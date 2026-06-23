from pipeline.llm import generate_json


def extract_intent(user_prompt):

    prompt = f"""
Extract the software requirements.

Return ONLY valid JSON.

Schema:

{{
  "app_type": "",
  "features": [],
  "roles": []
}}

User Request:
{user_prompt}
"""

    return generate_json(
        prompt,
        {
            "app_type": "CRM",
            "features": [
                "login",
                "contacts",
                "dashboard"
            ],
            "roles": [
                "admin"
            ]
        }
    )