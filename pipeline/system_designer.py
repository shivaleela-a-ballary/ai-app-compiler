import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


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

    response = model.generate_content(prompt)

    text = response.text.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")

    try:
        return json.loads(text)

    except Exception as e:
        print("JSON Parse Error:", e)
        print("Gemini Output:", text)

        return {
            "app_type": intent.get("app_type", "Unknown"),
            "entities": [],
            "relationships": []
        }