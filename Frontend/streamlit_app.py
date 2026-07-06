import streamlit as st
import requests
import json

st.set_page_config(
    page_title="AI-Powered Intelligent Document Processing",
    page_icon="📄",
    layout="wide"
)

# ---------------- Sidebar ---------------- #

st.sidebar.title("📄 AI Document Processor")

st.sidebar.markdown("---")

st.sidebar.subheader("Supported Documents")

st.sidebar.success("✅ Invoice")
st.sidebar.success("✅ Resume")
st.sidebar.success("✅ Purchase Order")
st.sidebar.success("✅ Contract")

st.sidebar.markdown("---")

st.sidebar.subheader("Processing Pipeline")

st.sidebar.write("""
📤 Upload Document

⬇

🤖 AI Classification

⬇

📝 AI Extraction

⬇

✔ Validation

⬇

👤 Human Review

⬇

📥 JSON Output
""")

# ---------------- Main Page ---------------- #

st.title("📄 AI-Powered Intelligent Document Processing System")

st.caption("AI-first Product Engineering Assignment")

st.markdown("---")

uploaded_file = st.file_uploader(
    "Upload Business Document",
    type=["pdf"]
)

# ---------------- Process Button ---------------- #

if uploaded_file is not None:

    st.success(f"Selected File: **{uploaded_file.name}**")

    if st.button("🚀 Process Document", use_container_width=True):

        with st.spinner("Processing document..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file,
                    "application/pdf"
                )
            }

            response = requests.post(
                "http://127.0.0.1:8000/process-document",
                files=files
            )

            result = response.json()

            if result["status"] == "success":

                st.session_state["result"] = result

            else:

                st.error(result["message"])

# ---------------- Display Result ---------------- #

if "result" in st.session_state:

    result = st.session_state["result"]

    st.success("✅ Document Processed Successfully")

    st.markdown("---")

    st.subheader("📊 Processing Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Document Type",
        result.get("document_type", "-")
    )

    col2.metric(
        "Confidence",
        result.get("confidence", "High")
    )

    col3.metric(
        "Needs Review",
        "Yes" if result.get("needs_review", False) else "No"
    )

    col4.metric(
        "Processing Time",
        str(result.get("processing_time_seconds", 0)) + " sec"
    )

    st.markdown("---")

    st.subheader("📝 Human Review")

    validation = result.get("validation", {})

    edited_fields = {}

    for key, value in result["fields"].items():

        label = key.replace("_", " ").title()

        edited_fields[key] = st.text_input(
            label,
            value=str(value),
            key=f"edit_{key}"
        )

        if key in validation:

            if validation[key]["valid"]:

                st.success(f"✅ {label} is Valid")

            else:

                st.warning(f"⚠ Please review {label}")

    st.markdown("---")

    if st.button("💾 Save Changes", use_container_width=True):

        result["fields"] = edited_fields

        st.session_state["result"] = result

        st.success("✅ Changes Saved Successfully!")

    # Always keep JSON updated with latest values
    st.session_state["result"]["fields"] = edited_fields

    st.markdown("---")

    st.subheader("📦 JSON Output")

    st.json(st.session_state["result"])

    st.download_button(
        label="⬇ Download Updated JSON",
        data=json.dumps(
            st.session_state["result"],
            indent=4
        ),
        file_name="processed_document.json",
        mime="application/json",
        use_container_width=True
    )

st.markdown("---")

st.caption(
    "Built with ❤️ using FastAPI • Streamlit • Groq • Python"
)