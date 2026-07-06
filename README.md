<div align="center">

# 📄 AI-Powered Intelligent Document Processing System

### AI-powered document classification, information extraction, validation, and human review using Large Language Models.

![Python](https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit)
![Groq](https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge)

</div>

---

# 📖 Overview

This project is an **AI-powered Intelligent Document Processing System** that automatically classifies business documents, extracts structured information using a Large Language Model (LLM), validates extracted data using deterministic Python rules, and provides a Human Review interface before exporting structured JSON.

The project demonstrates how AI and rule-based systems can work together to build reliable enterprise document-processing workflows.

---

# ✨ Features

- 📄 Automatic Document Classification
- 🤖 AI-powered Information Extraction
- ✔ Rule-based Data Validation
- 👤 Human Review & Correction
- 📊 Confidence Score
- ⚡ FastAPI REST API
- 🖥 Interactive Streamlit Dashboard
- 📦 Download Structured JSON

---

# 📂 Supported Document Types

| Document | Supported |
|----------|-----------|
| Invoice | ✅ |
| Resume | ✅ |
| Purchase Order | ✅ |
| Contract | ✅ |

---

# 🏗 System Architecture

```text
                Upload Document
                       │
                       ▼
             Document Reader
                       │
                       ▼
         AI Document Classifier
                       │
                       ▼
      AI Information Extractor
                       │
                       ▼
      Deterministic Validator
                       │
                       ▼
      Human Review & Correction
                       │
                       ▼
        Structured JSON Output
```

---

# 🛠 Technology Stack

## Backend

- Python
- FastAPI
- Groq API
- pdfplumber

## Frontend

- Streamlit

## AI Model

- Llama 3.3 70B Versatile (Groq)

---

# 📂 Project Structure

```text
AI-Powered-Intelligent-Document-Processing-System
│
├── Backend
│   ├── ai_client.py
│   ├── app.py
│   ├── classifier.py
│   ├── extractor.py
│   ├── validator.py
│   ├── document_reader.py
│   ├── document_processor.py
│
├── Frontend
│   └── streamlit_app.py
│
├── Sample_Documents
│
├── screenshots
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📸 Application Screenshots

## 🏠 Home Page

<p align="center">
<img src="screenshots/home.png" width="900">
</p>

---

## 📊 Processing Summary

<p align="center">
<img src="screenshots/processing_summary.png" width="900">
</p>

---

## 📦 Structured JSON Output

<p align="center">
<img src="screenshots/JSON.png" width="900">
</p>

---

## 🚀 FastAPI Swagger API

<p align="center">
<img src="screenshots/swagger_api.png" width="900">
</p>

---

# ⚙ Workflow

1. Upload a document.
2. AI classifies the document type.
3. AI extracts structured fields.
4. Python validates extracted information.
5. User reviews and edits extracted fields.
6. Updated JSON is generated and downloaded.

---

# ▶ Running the Project

## Clone Repository

```bash
git clone https://github.com/Premjith22/AI-Powered-Intelligent-Document-Processing-System.git
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment

Create a `.env` file:

```text
GROQ_API_KEY=YOUR_API_KEY
```

## Run Backend

```bash
cd Backend
uvicorn app:app --reload
```

## Run Frontend

```bash
cd Frontend
streamlit run streamlit_app.py
```

---

# 📡 API Endpoint

### POST

```
/process-document
```

Example Response

```json
{
  "status": "success",
  "document_type": "Invoice",
  "confidence": "98% (High)",
  "needs_review": false,
  "fields": {},
  "validation": {}
}
```

---

# 🧠 Design Decisions

## Why use AI?

AI is responsible for:

- Document Classification
- Information Extraction
- Understanding different document layouts

Traditional rule-based approaches struggle with varying document structures, whereas an LLM generalizes across multiple layouts.

---

## Why Deterministic Validation?

Validation is implemented using Python because it is:

- Faster
- Less expensive
- More predictable
- Easier to maintain

---

## Human-in-the-Loop

Instead of blindly trusting AI output, the system allows users to:

- Review extracted information
- Edit incorrect fields
- Download corrected JSON

This approach improves reliability and mirrors real-world enterprise document processing systems.

---

# 🔮 Future Enhancements

- OCR for scanned PDFs
- Image (JPG/PNG) support
- Batch document processing
- Database integration
- User authentication
- Docker deployment
- Excel export
- Per-field confidence scores

---

# 👨‍💻 Author

**Premjith P M**

Computer Science Engineer | Python Developer | AI Enthusiast

GitHub: https://github.com/Premjith22

---

<div align="center">

⭐ If you found this project interesting, consider giving it a star.

</div>