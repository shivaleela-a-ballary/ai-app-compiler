import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


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

    try:
        response = model.generate_content(prompt)

        text = response.text.strip()

        text = text.replace("```json", "")
        text = text.replace("```", "")

        return json.loads(text)

    except Exception as e:

        print("Gemini Error:", e)

        # Fallback response
        return {
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