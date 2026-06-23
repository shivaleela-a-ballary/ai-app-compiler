import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


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

    response = model.generate_content(prompt)

    text = response.text.strip()
    text = text.replace("```json", "")
    text = text.replace("```", "")

    try:
        return json.loads(text)

    except:
        return {"roles": {}}