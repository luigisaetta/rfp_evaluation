"""
All public configs here
"""

DEBUG = False

# can be also INSTANCE_PRINCIPAL
AUTH_TYPE = "API_KEY"

# for LLMs
REGION = "us-chicago-1"
# REGION = "eu-frankfurt-1"
SERVICE_ENDPOINT = f"https://inference.generativeai.{REGION}.oci.oraclecloud.com"

# this is the default model used
# MODEL_ID = "meta.llama-3.3-70b-instruct"
MODEL_ID = "xai.grok-3"

# these are the parameters used for the model
TEMPERATURE = 0.0
MAX_TOKENS = 2048

# inputs
CRITERIA_JSON_PATH = "inputs/criteria_list.json"
