"""
Hugging Face Chat Model Integration

This module demonstrates how to integrate Hugging Face models with LangChain
using the ChatHuggingFace wrapper.

The example uses an open-source model (GPT-oss-120b) from Hugging Face's
inference API for generating responses to queries.

Requirements:
    - HUGGINGFACE_API_KEY environment variable must be set
    - OR HF_INFERENCE_ENDPOINT environment variable

Example:
    python hf_api.py
"""

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve Hugging Face API key from environment
# The key is used for authentication with Hugging Face inference endpoints
api_key = os.getenv("HF_INFERENCE_ENDPOINT")

# Validate that the API key is set
if not api_key:
    raise ValueError(
        "Hugging Face API key is missing. "
        "Set it in your .env file as HF_INFERENCE_ENDPOINT."
    )

print('Initializing Hugging Face model...')

# Initialize the Hugging Face endpoint
# repo_id specifies which model to use from Hugging Face Hub
# task specifies the type of task (text-generation, text2text-generation, etc.)
llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation"
)

# Wrap the LLM with ChatHuggingFace for better chat interface
model = ChatHuggingFace(llm=llm)

# Generate a response to a query
# The model will generate text based on the input prompt
result = model.invoke("What is the capital of India")

# Extract and print the content from the response
print(result.content)