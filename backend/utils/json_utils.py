import json
import re

def clean_json_text(text: str) -> str:
    """
    Cleans common LLM JSON issues.
    """
    # Remove markdown fences
    text = re.sub(r"```json|```", "", text)

    # Remove smart quotes
    text = text.replace("“", '"').replace("”", '"')

    # Remove control characters except newline
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", text)

    return text.strip()


def extract_json(text: str):
    """
    Safely extracts and parses JSON from LLM output.
    """
    text = clean_json_text(text)

    # First attempt: direct parse
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Second attempt: regex extract
    match = re.search(r"\{[\s\S]*\}", text)
    if not match:
        raise ValueError("No JSON object found in LLM response")

    json_text = clean_json_text(match.group())

    try:
        return json.loads(json_text)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON after cleaning: {e}")
