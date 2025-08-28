"""
Here we define the overall structure of the Agent class.

"""

from langgraph.graph import StateGraph, START, END
from eval_state import EvaluationState
from read_rfp_node import RFPReaderNode
from read_rfp_answer_node import RFPAnswerReaderNode
from read_criterias_node import CriteriaReaderNode
from eval_criteria_node import EvalCriteriaNode
from generate_report import GenerateReportNode


def create_workflow():
    """
    Create the graph
    """

    # define the conditional node
    def next_step(state: EvaluationState) -> str:
        if state["current_index"] + 1 <= len(state["criteria_list"]):
            return "evaluate"

        return "generate_report"

    workflow = StateGraph(EvaluationState)
    # Add nodes and edges to the workflow graph
    # Example:
    workflow.add_node("rfp_reader", RFPReaderNode())
    workflow.add_node("rfp_answer_reader", RFPAnswerReaderNode())
    workflow.add_node("criterias_reader", CriteriaReaderNode())
    workflow.add_node("evaluate", EvalCriteriaNode())
    workflow.add_node("generate_report", GenerateReportNode())

    workflow.add_edge(START, "rfp_reader")
    workflow.add_edge("rfp_reader", "rfp_answer_reader")
    workflow.add_edge("rfp_answer_reader", "criterias_reader")

    # loop through all the criteria
    workflow.add_edge("criterias_reader", "evaluate")
    workflow.add_conditional_edges("evaluate", next_step)
    # end loop
    workflow.add_edge("generate_report", END)

    # ---- Build Graph and Save ----
    app = workflow.compile()

    return app
