"""
Simple Chain Example

This module demonstrates the simplest form of a LangChain chain:
Prompt Template -> Model -> Output Parser

The chain generates 5 interesting facts about a given year using the pipe (|)
operator to compose the components together.

Example:
    python simple_chain.py
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# Load environment variables (e.g., OPENAI_API_KEY)
load_dotenv()

# Initialize the language model
# Using GPT-4 optimized for advanced reasoning
model = ChatOpenAI(model='gpt-4o')

# Initialize output parser to convert model output to string
parser = StrOutputParser()

# Create a prompt template with a variable for the year
template = PromptTemplate(
    template='Give 5 facts about year {year}',
    input_variables=['year']
)

# Compose the chain using the pipe operator
# This creates a sequential composition: prompt -> model -> parser
chain = template | model | parser

# Execute the chain with a specific year
result = chain.invoke({'year': '2026'})

# Display the results
print(result)