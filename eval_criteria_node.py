"""
Generic node
"""

from langchain_core.runnables import Runnable
from langchain.prompts import PromptTemplate
from eval_state import EvaluationState
from prompts import PROMPT_EVAL_TEMPLATE
from oci_models import get_chat_model
from utils import get_console_logger
from config import DEBUG

logger = get_console_logger()


class EvalCriteriaNode(Runnable):
    """
    Eval the answer to RFP based on the criteria
    """

    def invoke(self, state: EvaluationState, config=None, **kwargs) -> EvaluationState:
        """
        Does something... to be specified in subclasses
        """
        criteria = state["criteria_list"][state["current_index"]]

        logger.info("")
        logger.info("--------------------------------")
        logger.info("Evaluating criteria: %s", criteria)
        logger.info("...")

        rfp_text = state["rfp_text"]
        rfp_answer_text = state["rfp_answer_text"]

        prompt_eval = PromptTemplate(
            input_variables=["criteria", "rfp_text", "rfp_answer_text"],
            template=PROMPT_EVAL_TEMPLATE,
        ).format(criteria=criteria, rfp_text=rfp_text, rfp_answer_text=rfp_answer_text)

        llm = get_chat_model()

        response = llm.invoke([{"role": "user", "content": prompt_eval}])

        logger.info("... done.")

        if DEBUG:
            logger.info("Evaluation result:\n%s", response.content)

        # store the result
        state["results"].append(f"Criteria: {criteria}\n{response.content}")

        # go to next step
        state["current_index"] += 1

        return state
