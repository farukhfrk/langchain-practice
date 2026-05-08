"""
Text File Loader Example

This example demonstrates how to load and process text files using LangChain's TextLoader.
It loads a document, then chains it with an LLM to analyze the content.

Requirements:
    - langchain-community
    - langchain-openai
    - python-dotenv
    - OpenAI API key in .env file

Usage:
    python text_loader.py
"""

from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# Load environment variables (OPENAI_API_KEY from .env file)
load_dotenv()

# Initialize the LLM model
model = ChatOpenAI()

# Define the analysis prompt template
prompt = PromptTemplate(
    input_variables=["text"],
    template="What is the main topic of the following text?\n\n{text}",
)

# Initialize the output parser
parser = StrOutputParser()

# TODO: Replace 'example.txt' with your file path
# Example paths:
#   - 'documents/report.txt'
#   - 'data/sample.txt'
#   - '../path/to/your/file.txt'
FILE_PATH = 'example.txt'

# Load the text document
loader = TextLoader(FILE_PATH, encoding='utf-8')
docs = loader.load()

# Display document information
print("=" * 60)
print("DOCUMENT INFORMATION")
print("=" * 60)
print(f"Document type: {type(docs)}")
print(f"Number of documents: {len(docs)}")
print(f"\nFirst document type: {type(docs[0])}")
print(f"File source: {docs[0].metadata['source']}")
print(f"\nContent preview (first 200 characters):")
print("-" * 60)
print(docs[0].page_content[:200] + "...")
print("-" * 60)

# Create the analysis chain: prompt -> model -> parser
chain = prompt | model | parser

# Invoke the chain to analyze the document
print("\nANALYSIS RESULT:")
print("=" * 60)
result = chain.invoke({'text': docs[0].page_content})
print(result)
print("=" * 60)