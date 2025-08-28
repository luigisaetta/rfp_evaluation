"""
Prompt used by LLM are defined here
"""

PROMPT_EVAL_TEMPLATE = """
You are a highly experienced RFP evaluator.
You are provided an RFP document and a response to that RFP.

Your task: Evaluate the RFP response **specifically** against **the provided criteria**.

**Criteria to evaluate:**  
{criteria}

**Context — RFP Document:**  
{rfp_text}

**RFP Response:**  
{rfp_answer_text}

---

**Instructions:**  
1. Provide a **Score** between 0 and 5 for how well the response meets the criteria (0 = not at all; 5 = fully aligned).  
2. Write a **rating rationale** —cite specific parts of the answer that illustrate strengths or gaps.  
3. Summarize the **single most critical improvement** needed to strengthen performance on this criterion.
4. Keep your evaluation concise and focused on the criterion.
"""

PROMPT_REPORT_TEMPLATE = """
You are a highly experienced RFP evaluator.

Review all the evaluations provided for the RFP response and summarize them into a comprehensive final report.
Remove any duplicate information and ensure the report flows logically.
For each criteria report the score, rationale and suggested improvement.

**Criteria to evaluate:**  
{all_criteria}

**The draft of the report:**  
{draft_report}
"""
