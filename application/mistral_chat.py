from transformers import AutoModelForCausalLM, AutoTokenizer
from dotenv import load_dotenv
import os

import torch
from transformers import pipeline

# Load environment variables from .env file
load_dotenv()

# Retrieve the Hugging Face token
access_token = os.getenv("HF_TOKEN")
print(access_token)

# Define model name
model_name = "meta-llama/Meta-Llama-3-8B-Instruct"

# Load model and tokenizer with authentication
tokenizer = AutoTokenizer.from_pretrained(model_name, token=access_token)
model = AutoModelForCausalLM.from_pretrained(model_name, token=access_token)