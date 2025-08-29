"""
Streamlit UI
"""
import streamlit as st

from workflow import create_workflow
from eval_state import EvaluationState
from ui_utils import read_file, load_criteria
from config import MODEL_ID

#
# Main UI code
#
st.set_page_config(page_title="RFP Evaluation Agent", layout="wide")

st.title("📄 RFP Evaluation Agent")

# Sidebar inputs
st.sidebar.header("🔧 Configuration")
st.sidebar.markdown("### LLM Model in Use")
st.sidebar.info(f"🔍 **{MODEL_ID}**")

rfp_file = st.sidebar.file_uploader("Upload RFP File (PDF)", type=["pdf"])
rfp_answer_file = st.sidebar.file_uploader("Upload RFP Answer File (PDF)", type=["pdf"])
criteria_file = st.sidebar.file_uploader("Upload Criteria (JSON)", type=["json"])

run_button = st.sidebar.button("🚀 Run Evaluation")
# added the progress bar
progress_bar = st.sidebar.progress(0)

# Main UI
if run_button:
    if not rfp_file or not rfp_answer_file or not criteria_file:
        st.error("Please upload all three files before running the evaluation.")
        st.stop()

    # Read inputs
    with st.spinner("Reading input files..."):
        rfp_text = read_file(rfp_file)
        rfp_answer_text = read_file(rfp_answer_file)
        criteria_list = load_criteria(criteria_file)

    if not criteria_list:
        st.error("No criteria found in the provided JSON file.")
        st.stop()

    # Run the agent
    with st.spinner("Evaluating RFP Answer..."):
        # set the initial state
        initial_state: EvaluationState = {
            # path are set to empty since we're from UI, directly passing doc content
            "rfp_pathname": "",
            "rfp_answer_pathname": "",
            # we put the doc content directly in the state
            "rfp_text": rfp_text,
            "rfp_answer_text": rfp_answer_text,
            "criteria_list": criteria_list,
            "results": [],
        }

        app = create_workflow()
        
        # start the agent
        results = []
        # for the progress bar
        # eval steps + final report
        n_total_steps = len(criteria_list) + 1
        n_steps_completed = 0
        for event in app.stream(
            initial_state,
        ):
            for key, value in event.items():
                MSG = f"Completed: {key} step!"
                st.toast(MSG)

                # save the status after the step...
                # for now, we're using only the last one
                results.append(value)

                # update the progress bar only for eval steps and final generation
                if key in ("evaluate", "generate_report"):
                    n_steps_completed += 1
                    progress = n_steps_completed / n_total_steps
                    # update the bar
                    progress_bar.progress(progress)

        # get the final state from the list
        final_state = results[-1]

    # Show the final report
    st.success("✅ Evaluation Completed")
    st.subheader("📊 Final Report")
    st.markdown(final_state.get("final_report", ""), unsafe_allow_html=True)
