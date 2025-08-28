"""
Streamlit UI
"""

import json
from pathlib import Path
from typing import List
from pypdf import PdfReader
import streamlit as st

from workflow import create_workflow
from eval_state import EvaluationState


# Helper:
# read PDF or TXT file
def read_file(file) -> str:
    """Reads a PDF or TXT file and returns its content."""
    file_type = Path(file.name).suffix.lower()
    if file_type == ".pdf":
        reader = PdfReader(file)
        return "\n".join([page.extract_text() or "" for page in reader.pages])
    if file_type in [".txt", ".md"]:
        return file.read().decode("utf-8")

    st.error("Unsupported file type. Please upload a PDF or TXT file.")
    return ""


# read JSON
def load_criteria(file) -> List[str]:
    """Load criteria from an uploaded JSON file."""
    try:
        data = json.load(file)
        return data.get("criteria_list", [])
    except Exception as e:
        st.error(f"Error reading criteria JSON: {e}")
        return []


#
# Main UI code
#
st.set_page_config(page_title="RFP Evaluation Agent", layout="wide")

st.title("📄 RFP Evaluation Agent")

# Sidebar inputs
st.sidebar.header("🔧 Configuration")
rfp_file = st.sidebar.file_uploader("Upload RFP File (PDF)", type=["pdf"])
rfp_answer_file = st.sidebar.file_uploader("Upload RFP Answer File (PDF)", type=["pdf"])
criteria_file = st.sidebar.file_uploader("Upload Criteria JSON", type=["json"])

run_button = st.sidebar.button("🚀 Run Evaluation")

# Main UI
if run_button:
    if not rfp_file or not rfp_answer_file or not criteria_file:
        st.error("Please upload all three files before running the evaluation.")
        st.stop()

    # Read inputs
    with st.spinner("Reading input files..."):
        rfp_text = read_file(rfp_file)
        rfp_answer_text = read_file(rfp_answer_file)
        criteria_list = load_criteria(criteria_file)

    if not criteria_list:
        st.error("No criteria found in the provided JSON file.")
        st.stop()

    # Run the agent
    with st.spinner("Evaluating RFP Answer..."):
        # set the initial state
        initial_state: EvaluationState = {
            # path are set to empty since we're from UI, directly passing doc content
            "rfp_pathname": "",
            "rfp_answer_pathname": "",
            # we put the doc content directly in the state
            "rfp_text": rfp_text,
            "rfp_answer_text": rfp_answer_text,
            "criteria_list": criteria_list,
            "results": [],
        }

        app = create_workflow()
        # start the agent

        results = []
        for event in app.stream(
            initial_state,
        ):
            for key, value in event.items():
                MSG = f"Completed: {key} step!"
                st.toast(MSG)

                results.append(value)

        # get the final state from the list
        final_state = results[-1]

    # Show report
    st.success("✅ Evaluation Completed")
    st.subheader("📊 Final Report")
    st.markdown(final_state.get("final_report", ""), unsafe_allow_html=True)
