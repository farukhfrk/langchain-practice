"""
RunnableSequence Example

This module demonstrates RunnableSequence for chaining multiple operations
in a specific order.

The workflow:
1. Generate a joke about a topic (chain1)
2. Explain the generated joke (chain2)

The output from chain1 (the joke) becomes the input to chain2.

This is similar to the pipe operator (|) but explicitly shows the
RunnableSequence class.

Example:
    python runnable-sequence.py
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define prompt for joke generation
prompt = PromptTemplate(
    template='write a joke on the {topic}',
    input_variables=['topic']
)

# Define prompt for joke explanation
# Note: {text} will receive the output from the first chain
prompt2 = PromptTemplate(
    template='explain the following joke {text}',
    input_variables=['text']
)

# Initialize language model
model = ChatOpenAI()

# Initialize output parser
parser = StrOutputParser()

# Method 1: Using the pipe operator (more idiomatic in LangChain)
# This creates a sequence: prompt -> model -> parser
chain1 = prompt | model | parser

# Second sequence: prompt2 -> model -> parser
chain2 = prompt2 | model | parser

# Method 2: Explicitly using RunnableSequence
# (Commented out - equivalent to the pipe operator method)
# finalchain = RunnableSequence(prompt, model, parser, prompt2, model, parser)

# Combine chain1 and chain2 into a sequence
# The output from chain1 becomes input to chain2
finalchain = RunnableSequence(chain1, chain2)

# Execute the sequence
# 1. chain1 generates a joke about 'chicken'
# 2. chain2 explains the joke from chain1
result = finalchain.invoke({'topic': 'chicken'})

print("=== Result ===")
print(result)