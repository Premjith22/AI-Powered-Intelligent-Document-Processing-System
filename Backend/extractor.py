import json
import re

from ai_client import generate_response
from prompts import EXTRACTION_PROMPTS


def clean_json(text):

    text = text.strip()

    text = re.sub(r"^```json", "", text, flags=re.IGNORECASE)

    text = re.sub(r"^```", "", text)

    text = re.sub(r"```$", "", text)

    return text.strip()


def extract_fields(document_type, text):

    if document_type not in EXTRACTION_PROMPTS:

        return {

            "error": "Unsupported document type"

        }

    prompt = EXTRACTION_PROMPTS[
        document_type
    ].format(text=text)

    response = generate_response(prompt)

    cleaned = clean_json(response)

    try:

        return json.loads(cleaned)

    except Exception:

        return {

            "error": "Invalid JSON",

            "raw_response": cleaned

        }