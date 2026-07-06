import time

from classifier import classify_document
from extractor import extract_fields
from validator import validate_data


def process_document(document_text, filename="Unknown"):

    start_time = time.time()

    try:

        # Step 1 - Classify Document
        document_type = classify_document(document_text)

        if document_type == "Unknown":

            return {
                "status": "error",
                "message": "Unable to classify document.",
                "needs_review": True
            }

        # Step 2 - Extract Fields
        extracted_fields = extract_fields(
            document_type,
            document_text
        )

        if "error" in extracted_fields:

            return {
                "status": "error",
                "message": extracted_fields["error"],
                "needs_review": True
            }

        # Step 3 - Validate
        validation = validate_data(
            document_type,
            extracted_fields
        )

        # -----------------------------
        # Confidence Score Calculation
        # -----------------------------

        total_fields = len(extracted_fields)

        filled_fields = sum(
            1 for value in extracted_fields.values()
            if str(value).strip() != ""
        )

        total_validation = len(validation)

        valid_fields = sum(
            1 for value in validation.values()
            if value["valid"]
        )

        if total_validation == 0:
            validation_score = 100
        else:
            validation_score = (valid_fields / total_validation) * 100

        extraction_score = (filled_fields / total_fields) * 100

        confidence_score = round(
            (validation_score + extraction_score) / 2
        )

        if confidence_score >= 90:
            confidence = f"{confidence_score}% (High)"
        elif confidence_score >= 70:
            confidence = f"{confidence_score}% (Medium)"
        else:
            confidence = f"{confidence_score}% (Low)"

        needs_review = confidence_score < 100

        processing_time = round(
            time.time() - start_time,
            2
        )

        return {

            "status": "success",

            "filename": filename,

            "document_type": document_type,

            "confidence": confidence,

            "needs_review": needs_review,

            "processing_time_seconds": processing_time,

            "fields": extracted_fields,

            "validation": validation

        }

    except Exception as e:

        return {

            "status": "error",

            "message": str(e),

            "needs_review": True

        }