"""
Generic node
"""

from langchain_core.runnables import Runnable
from eval_state import EvaluationState
from pdf_reader import extract_text_from_pdf
from utils import get_console_logger

logger = get_console_logger()


class RFPAnswerReaderNode(Runnable):
    """
    Does something
    """

    def invoke(self, state: EvaluationState, config=None, **kwargs) -> EvaluationState:
        """
        Does something... to be specified
        """
        logger.info("Reading RFP answer...")

        if state.get("rfp_answer_text"):
            # called from UI with text already read
            logger.info("RFP answer text already present in state, skipping read.")
        else:
            rfp_answer_pathname = state["rfp_answer_pathname"]

            rfp_answer_text = extract_text_from_pdf(rfp_answer_pathname)
            state["rfp_answer_text"] = rfp_answer_text

        return state
