import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


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

    response = model.generate_content(prompt)

    text = response.text.strip()
    text = text.replace("```json", "")
    text = text.replace("```", "")

    try:
        return json.loads(text)

    except Exception:
        return {"pages": []}