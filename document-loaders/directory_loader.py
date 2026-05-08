"""
Directory Loader Example

This example demonstrates how to load multiple documents from a directory using DirectoryLoader.
It uses glob patterns to filter specific file types and processes them in batch.

Requirements:
    - langchain-community
    - langchain-openai
    - python-dotenv
    - OpenAI API key in .env file

Usage:
    python directory_loader.py

Features:
    - Load multiple files matching a glob pattern
    - Recursive directory traversal
    - Progress display during loading
    - Batch processing of documents
"""

from langchain_community.document_loaders import DirectoryLoader, TextLoader
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

# TODO: Replace '.' with your directory path
# The glob pattern controls which files are loaded:
#   - '**/*.txt'  -> All .txt files recursively
#   - '*.txt'     -> Only .txt files in top directory
#   - '**/*.md'   -> All markdown files
#   - '**/*'      -> All files
#
# Common directory paths:
#   - '.'                    -> Current directory
#   - 'documents'
#   - '../data/documents'
#   - '/absolute/path/to/documents'
DIRECTORY_PATH = '.'
GLOB_PATTERN = '**/*.txt'

# Load all matching documents from the directory
loader = DirectoryLoader(
    DIRECTORY_PATH,
    glob=GLOB_PATTERN,
    loader_cls=TextLoader,
    show_progress=True,  # Display loading progress
    # silent_errors=True   # Uncomment to skip files with loading errors
)

print(f"Loading files from: {DIRECTORY_PATH}")
print(f"Pattern: {GLOB_PATTERN}")
print("=" * 60)

docs = loader.load()

# Display directory information
print("=" * 60)
print("DIRECTORY LOADING RESULTS")
print("=" * 60)
print(f"Total documents loaded: {len(docs)}")
print(f"Document type: {type(docs)}")
print(f"First document type: {type(docs[0])}")

# Display information about each loaded document
print("\nLoaded files:")
print("-" * 60)
for i, doc in enumerate(docs, 1):
    source = doc.metadata.get('source', 'Unknown')
    content_preview = doc.page_content[:100].replace('\n', ' ')
    print(f"{i}. {source}")
    print(f"   Preview: {content_preview}...")

print("=" * 60)

# Create the analysis chain
chain = prompt | model | parser

# Analyze the first document
if docs:
    print(f"\nANALYZING FIRST DOCUMENT: {docs[0].metadata['source']}")
    print("=" * 60)
    result = chain.invoke({'text': docs[0].page_content})
    print(result)
    print("=" * 60)