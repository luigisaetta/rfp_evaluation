"""
Utils only for the UI
"""

import json
from pathlib import Path
from typing import List
import streamlit as st
from pypdf import PdfReader


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
