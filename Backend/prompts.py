CLASSIFICATION_PROMPT = """
You are an intelligent document classification system.

Classify the given document into ONLY ONE of these categories:

- Invoice
- Resume
- Purchase Order
- Contract

Rules:
- Return ONLY the document type.
- Do not explain.
- Do not add punctuation.
- Do not add extra text.

Document:

{text}
"""


EXTRACTION_PROMPTS = {

    "Invoice": """
You are an invoice information extraction assistant.

Extract the following fields.

Return ONLY valid JSON.

{{
    "invoice_number":"",
    "vendor":"",
    "date":"",
    "amount":"",
    "gst":""
}}

Document:

{text}
""",

    "Resume": """
You are a resume extraction assistant.

Extract the following fields.

Return ONLY valid JSON.

{{
    "name":"",
    "email":"",
    "phone":"",
    "skills":[],
    "education":"",
    "experience":""
}}

Document:

{text}
""",

    "Purchase Order": """
You are a purchase order extraction assistant.

Return ONLY valid JSON.

{{
    "po_number":"",
    "supplier":"",
    "items":[],
    "total_amount":""
}}

Document:

{text}
""",

    "Contract": """
You are a contract extraction assistant.

Return ONLY valid JSON.

{{
    "party_a":"",
    "party_b":"",
    "start_date":"",
    "end_date":""
}}

Document:

{text}
"""
}