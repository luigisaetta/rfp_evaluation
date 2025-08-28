"""
PDF reader, used both for RFOP and RFP answer
"""

import warnings
from pypdf import PdfReader
from utils import get_console_logger
from config import DEBUG

warnings.filterwarnings("ignore", category=UserWarning)
logger = get_console_logger()


def extract_text_from_pdf(path: str) -> str:
    """
    Extract text from a PDF file
    """
    text = ""

    try:
        reader = PdfReader(path, strict=False)

        for i, page in enumerate(reader.pages):
            page_text = page.extract_text()
            text += f"\n\n--- Page {i + 1} ---\n"
            text += page_text or ""

        if DEBUG:
            logger.info("Extracted text from PDF file %s:", path)
            logger.info("Total pages: %d", len(reader.pages))

    except Exception as e:
        logger.info("Error reading PDF file %s: %s", path, e)

    return text
