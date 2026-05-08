"""
PDF Document Loader Example

This example demonstrates how to load and process PDF documents using LangChain's PyPDFLoader.
It extracts text from each page and chains with an LLM for content analysis.

Requirements:
    - langchain-community
    - langchain-openai
    - pypdf
    - python-dotenv
    - OpenAI API key in .env file

Installation:
    pip install pypdf langchain-community langchain-openai

Usage:
    python pypdf_loader.py

Note:
    PyPDFLoader processes one page per document. For multi-page PDFs, iterate through docs.
"""

from langchain_community.document_loaders import PyPDFLoader
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
    template="What is the main topic of the following text?\n\n{text}",
)

# Initialize the output parser
parser = StrOutputParser()

# TODO: Replace 'sample-local-pdf.pdf' with your PDF file path
# Example paths:
#   - 'documents/research_paper.pdf'
#   - 'data/report.pdf'
#   - '../path/to/your/document.pdf'
PDF_FILE_PATH = 'sample-local-pdf.pdf'

# Load the PDF document
loader = PyPDFLoader(PDF_FILE_PATH)
docs = loader.load()

# Display document information
print("=" * 60)
print("PDF DOCUMENT INFORMATION")
print("=" * 60)
print(f"Total pages loaded: {len(docs)}")
print(f"File source: {docs[0].metadata['source']}")
print(f"\nFirst page metadata: {docs[0].metadata}")
print(f"\nFirst page content preview (first 300 characters):")
print("-" * 60)
print(docs[0].page_content[:300] + "...")
print("-" * 60)

# Create the analysis chain
chain = prompt | model | parser

# Analyze the first page
print("\nANALYZING FIRST PAGE:")
print("=" * 60)
result = chain.invoke({'text': docs[0].page_content})
print(result)
print("=" * 60)

# Example: Process all pages (commented out for brevity)
# print("\nProcessing all pages...")
# for i, doc in enumerate(docs[:3], 1):  # Process first 3 pages
#     print(f"\nPage {doc.metadata['page']}: {doc.page_content[:100]}...")

