# RFP Evaluation Agent
This repository contains the code for a prototype of an AI agent to evaluate
answers to a RFP document.

## Design and implementation
The agent has been implemented using:
* **OCI Generative AI**
* **Langgraph**
* Streamlit UI

# Features
* Totally modular
* All the files (RFP, answer, criteria list) can be uploaded from the UI
* The LLM model used can be changed from the config
* [Prompts](./prompts.py) used to evaluate criteria and to generate the final report saved in a dedicated file 
* UI interface + batch provided
* Report saved in **Markdown** format
