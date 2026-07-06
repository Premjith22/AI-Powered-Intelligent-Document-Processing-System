import os
import base64
import pdfplumber

from ai_client import client


def extract_text_from_pdf(file_path):

    text = ""

    with pdfplumber.open(file_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text.strip()


def extract_text_from_image(file_path):

    with open(file_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode("utf-8")

    ext = os.path.splitext(file_path)[1].lower()

    mime = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg"
    }.get(ext, "image/jpeg")

    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": """
Extract ALL text from this document.

Rules:
- Preserve line breaks.
- Do not summarize.
- Do not explain.
- Return only the extracted text.
"""
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:{mime};base64,{image_data}"
                        }
                    }
                ]
            }
        ]
    )

    return completion.choices[0].message.content


def extract_text(file_path):

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        return extract_text_from_pdf(file_path)

    elif extension in [".png", ".jpg", ".jpeg"]:
        return extract_text_from_image(file_path)

    else:
        raise Exception("Unsupported file format")