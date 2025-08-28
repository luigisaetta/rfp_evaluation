"""
Read evaluation criteria node
"""

from langchain_core.runnables import Runnable
from eval_state import EvaluationState
from utils import get_console_logger, load_criteria_from_json
from config import CRITERIA_JSON_PATH

logger = get_console_logger()


class CriteriaReaderNode(Runnable):
    """
    Does something
    """

    def invoke(self, state: EvaluationState, config=None, **kwargs) -> EvaluationState:
        """
        Does something... to be specified in subclasses
        """
        logger.info("Reading evaluation criteria...")

        if state.get("criteria_list"):
            # called from UI with criteria already read
            logger.info("Criteria list already present in state, skipping read.")
        else:
            state["criteria_list"] = load_criteria_from_json(CRITERIA_JSON_PATH)

        # start with the first criteria
        state["current_index"] = 0

        return state
