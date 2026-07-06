import re
from datetime import datetime


def validate_email(email):

    if not email:
        return False

    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    return re.match(pattern, email) is not None


def validate_phone(phone):

    if not phone:
        return False

    digits = re.sub(r"\D", "", phone)

    return len(digits) >= 10


def validate_amount(amount):

    if amount is None:
        return False

    try:
        amount = str(amount)

        amount = amount.replace("₹", "")

        amount = amount.replace(",", "")

        float(amount)

        return True

    except:

        return False


def validate_date(date):

    if not date:
        return False

    formats = [

        "%d/%m/%Y",

        "%d-%m-%Y",

        "%d %B %Y",

        "%Y-%m-%d"

    ]

    for fmt in formats:

        try:

            datetime.strptime(date.strip(), fmt)

            return True

        except:

            pass

    return False


def validate_gst(gst):

    if not gst:

        return False

    pattern = r'^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][A-Z0-9]Z[A-Z0-9]$'

    return re.match(pattern, gst.upper()) is not None


def validate_data(document_type, fields):

    validation = {}

    if document_type == "Invoice":

        validation["amount"] = {

            "value": fields.get("amount"),

            "valid": validate_amount(fields.get("amount"))

        }

        validation["date"] = {

            "value": fields.get("date"),

            "valid": validate_date(fields.get("date"))

        }

        validation["gst"] = {

            "value": fields.get("gst"),

            "valid": validate_gst(fields.get("gst"))

        }

    elif document_type == "Resume":

        validation["email"] = {

            "value": fields.get("email"),

            "valid": validate_email(fields.get("email"))

        }

        validation["phone"] = {

            "value": fields.get("phone"),

            "valid": validate_phone(fields.get("phone"))

        }

    elif document_type == "Purchase Order":

        validation["total_amount"] = {

            "value": fields.get("total_amount"),

            "valid": validate_amount(fields.get("total_amount"))

        }

    elif document_type == "Contract":

        validation["start_date"] = {

            "value": fields.get("start_date"),

            "valid": validate_date(fields.get("start_date"))

        }

        validation["end_date"] = {

            "value": fields.get("end_date"),

            "valid": validate_date(fields.get("end_date"))

        }

    return validation