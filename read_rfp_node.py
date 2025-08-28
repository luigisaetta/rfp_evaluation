"""
Generic node
"""

from langchain_core.runnables import Runnable
from eval_state import EvaluationState
from pdf_reader import extract_text_from_pdf
from utils import get_console_logger

logger = get_console_logger()


class RFPReaderNode(Runnable):
    """
    Does something
    """

    def invoke(self, state: EvaluationState, config=None, **kwargs) -> EvaluationState:
        """
        Does something... to be specified in subclasses
        """
        logger.info("Reading RFP...")

        if state.get("rfp_text"):
            # called from UI with text already read
            logger.info("RFP text already present in state, skipping read.")
        else:
            rfp_pathname = state["rfp_pathname"]

            rfp_text = extract_text_from_pdf(rfp_pathname)
            state["rfp_text"] = rfp_text

        return state
