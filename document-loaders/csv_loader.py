"""
CSV Data Loader Example

This example demonstrates how to load and process CSV files using LangChain's CSVLoader.
It converts each row into a document and chains with an LLM for analysis.

Requirements:
    - langchain-community
    - langchain-openai
    - python-dotenv
    - OpenAI API key in .env file

Usage:
    python csv_loader.py

Features:
    - Load structured CSV data
    - Each row becomes a document
    - Preserves column headers and values
    - Useful for tabular data analysis
"""

from langchain_community.document_loaders import CSVLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the LLM model
model = ChatOpenAI()

# Define the analysis prompt template
prompt = PromptTemplate(
    input_variables=["text"],
    template="What is the main topic of the following data record?\n\n{text}",
)

# Initialize the output parser
parser = StrOutputParser()

# TODO: Replace 'example.csv' with your CSV file path
# Example paths:
#   - 'data/employees.csv'
#   - 'survey_responses.csv'
#   - '../data/records.csv'
CSV_FILE_PATH = 'example.csv'

# Load the CSV file
# Note: CSVLoader creates one document per row
loader = CSVLoader(CSV_FILE_PATH)
docs = loader.load()

# Display CSV information
print("=" * 60)
print("CSV DATA INFORMATION")
print("=" * 60)
print(f"Total rows loaded: {len(docs)}")
print(f"File source: {docs[0].metadata['source']}")
print(f"\nSample rows:")
print("-" * 60)

# Show first 3 rows as samples
for i, doc in enumerate(docs[:3], 1):
    print(f"\nRow {i}:")
    print(f"Content:\n{doc.page_content}")
    print(f"Metadata: {doc.metadata}")

print("-" * 60)

# Create the analysis chain
chain = prompt | model | parser

# Analyze the first data record
if docs:
    print(f"\nANALYZING FIRST RECORD:")
    print("=" * 60)
    result = chain.invoke({'text': docs[0].page_content})
    print(result)
    print("=" * 60)

# Example: Process multiple rows (commented out for brevity)
# print("\nProcessing all records...")
# for i, doc in enumerate(docs, 1):
#     if i > 5:  # Limit to 5 for demo
#         break
#     result = chain.invoke({'text': doc.page_content})
#     print(f"Row {i} analysis: {result[:100]}...")
