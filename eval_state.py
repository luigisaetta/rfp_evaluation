"""
State

Here we define the state of the graph

"""

from typing import TypedDict


class EvaluationState(TypedDict):
    """
    The State of the graph
    """

    rfp_pathname: str
    rfp_answer_pathname: str

    rfp_text: str
    rfp_answer_text: str

    # to loop through all the criteria
    criteria_list: list[str]
    current_index: int
    # eval for each criteria
    results: list[str]

    #
    final_report: str
