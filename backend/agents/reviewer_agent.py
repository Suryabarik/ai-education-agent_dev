
from groq import Groq
import json
from utils.prompt_templates import REVIEWER_PROMPT
from utils.json_utils import extract_json  # ✅ USE THIS
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class ReviewerAgent:
    @staticmethod
    def review(grade: int, content: dict):
        prompt = REVIEWER_PROMPT.format(
            grade=grade,
            content=json.dumps(content)
        )

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            response_format={"type": "json_object"}
        )

        raw_text = response.choices[0].message.content
        return extract_json(raw_text)
