from ai_client import generate_response
from prompts import CLASSIFICATION_PROMPT


VALID_DOCUMENTS = [

    "Invoice",

    "Resume",

    "Purchase Order",

    "Contract"

]


def classify_document(text):

    prompt = CLASSIFICATION_PROMPT.format(
        text=text
    )

    response = generate_response(prompt).strip()

    for doc in VALID_DOCUMENTS:

        if doc.lower() == response.lower():

            return doc

    return "Unknown"