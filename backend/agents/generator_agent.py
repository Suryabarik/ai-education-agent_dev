

from groq import Groq
import json
from utils.prompt_templates import GENERATOR_PROMPT
from utils.json_utils import extract_json  # ✅ USE THIS
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class GeneratorAgent:
    @staticmethod
    def generate(grade: int, topic: str, feedback: str | None = None):
        prompt = GENERATOR_PROMPT.format(grade=grade, topic=topic)

        if feedback:
            prompt += f"\nFix the following issues:\n{feedback}"

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            response_format={"type": "json_object"}
        )

        raw_text = response.choices[0].message.content  # ✅ SAFE
        return extract_json(raw_text)  # ✅ YOUR CLEANER
