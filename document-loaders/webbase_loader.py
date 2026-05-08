"""
Web Content Loader Example

This example demonstrates how to load and process web content using LangChain's WebBaseLoader.
It fetches content from a URL, cleans HTML, and chains with an LLM for analysis.

Requirements:
    - langchain-community
    - langchain-openai
    - beautifulsoup4
    - lxml
    - python-dotenv
    - OpenAI API key in .env file

Installation:
    pip install beautifulsoup4 lxml langchain-community langchain-openai

Usage:
    python webbase_loader.py

Note:
    WebBaseLoader uses BeautifulSoup to parse HTML and extract main content.
    Some websites may have robots.txt restrictions or require headers.
"""

from langchain_community.document_loaders import WebBaseLoader
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
    input_variables=["text", "question"],
    template="Answer the following question using the provided text:\n\n"
             "Question: {question}\n\n"
             "Text: {text}",
)

# Initialize the output parser
parser = StrOutputParser()

# TODO: Replace with your target URL
# Example URLs:
#   - 'https://en.wikipedia.org/wiki/Artificial_intelligence'
#   - 'https://docs.python.org/3/'
#   - 'https://example-blog.com/article'
#
# Note: Ensure you have permission to scrape the website and respect robots.txt
WEB_URL = 'https://en.wikipedia.org/wiki/Artificial_intelligence'

# Load content from the web URL
print(f"Fetching content from: {WEB_URL}")
loader = WebBaseLoader(WEB_URL)
docs = loader.load()

# Display document information
print("=" * 60)
print("WEB CONTENT INFORMATION")
print("=" * 60)
print(f"Number of documents: {len(docs)}")
print(f"Source URL: {docs[0].metadata['source']}")
print(f"\nContent preview (first 400 characters):")
print("-" * 60)
print(docs[0].page_content[:400] + "...")
print("-" * 60)

# Create the analysis chain
chain = prompt | model | parser

# Ask a question about the content
question = 'What is Artificial Intelligence?'
print(f"\nQUESTION: {question}")
print("=" * 60)
result = chain.invoke({
    'text': docs[0].page_content,
    'question': question
})
print(result)
print("=" * 60)