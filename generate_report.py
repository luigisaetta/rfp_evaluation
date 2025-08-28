"""
Generate the final report based on all criteria evaluations
"""

from langchain_core.runnables import Runnable
from eval_state import EvaluationState
from oci_models import get_chat_model
from prompts import PROMPT_REPORT_TEMPLATE
from utils import get_console_logger

logger = get_console_logger()


class GenerateReportNode(Runnable):
    """
    Does something
    """

    def invoke(self, state: EvaluationState, config=None, **kwargs) -> EvaluationState:
        """
        Does something... to be specified in subclasses
        """
        logger.info("")
        logger.info("Generating Final Report...")

        all_criteria = "\n".join(state["criteria_list"])
        draft_report = "\n\n".join(state["results"])

        # bigger output allowed than for single criteria
        llm = get_chat_model(max_tokens=4000)

        prompt_report = PROMPT_REPORT_TEMPLATE.format(
            input_variables=["all_criteria", "draft_report"],
            all_criteria=all_criteria,
            draft_report=draft_report,
        )
        response = llm.invoke([{"role": "user", "content": prompt_report}])

        state["final_report"] = response.content

        # save in a md file
        with open("outputs/final_report.md", "w", encoding="utf-8") as f:
            f.write(state["final_report"])

        return state
