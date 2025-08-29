"""
test the workflow structure
"""

from eval_state import EvaluationState
from workflow import create_workflow

initial_state: EvaluationState = {
    "rfp_pathname": "inputs/rfp01.pdf",
    "rfp_answer_pathname": "inputs/rfp01_answer.pdf",
    "results": [],
}

app = create_workflow()

print("")
print("Generating report...")
print("")

final_state = app.invoke(initial_state)

print("")
print("---- FINAL REPORT ----")
print(final_state["final_report"])
