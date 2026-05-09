"""Character-based text splitter example.

This splitter divides text into chunks of a specified character length.
Useful for: simple text, basic preprocessing, non-language-specific tasks.
"""

from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


# Example 1: Split plain text by character count
text = (
    "This is a long text that needs to be split into smaller chunks. "
    "The character splitter will split the text based on a specified character limit. "
    "It is useful for processing large documents or texts that exceed certain limits. "
    "The character splitter can be configured to split the text at specific characters, "
    "such as spaces or punctuation marks, to ensure that the chunks are meaningful and easy to read."
)

# chunk_size: Maximum number of characters per chunk
# chunk_overlap: Number of overlapping characters between consecutive chunks (helps preserve context)
# separator: Character to split on (empty string = split by exact character count)
splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=20, separator="")
chunks = splitter.split_text(text)

print("=== Character Splitter - Plain Text ===")
for i, chunk in enumerate(chunks, 1):
    print(f"Chunk {i} ({len(chunk)} chars):\n{chunk}\n")


# Example 2: Split PDF documents
# NOTE: Replace with your actual PDF path or file
print("\n=== Character Splitter - PDF Documents ===")
try:
    pdf_path = "path/to/your/sample.pdf"  # Update with your PDF file path
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    print(f"Total documents loaded: {len(documents)}")

    doc_splitter = splitter.split_documents(documents)
    for i, doc in enumerate(doc_splitter[:3], 1):  # Show first 3 chunks
        print(f"Document Chunk {i}:\n{doc.page_content[:200]}...\n")
except FileNotFoundError:
    print(f"PDF file not found at '{pdf_path}'. Please update the path with your PDF file.")
