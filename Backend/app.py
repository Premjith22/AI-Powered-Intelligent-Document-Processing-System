from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os

from document_reader import extract_text
from document_processor import process_document

app = FastAPI(
    title="AI Document Processing API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():

    return {
        "message": "AI Document Processing API is Running"
    }


@app.post("/process-document")
async def process_document_api(file: UploadFile = File(...)):

    try:

        allowed = [".pdf", ".png", ".jpg", ".jpeg"]

        extension = os.path.splitext(file.filename)[1].lower()

        if extension not in allowed:

            return {
                "status": "error",
                "message": "Only PDF, PNG, JPG and JPEG are supported."
            }

        file_path = os.path.join(
            UPLOAD_FOLDER,
            file.filename
        )

        with open(file_path, "wb") as buffer:

            shutil.copyfileobj(file.file, buffer)

        text = extract_text(file_path)

        result = process_document(
            text,
            file.filename
        )

        return result

    except Exception as e:

        return {
            "status": "error",
            "message": str(e)
        }