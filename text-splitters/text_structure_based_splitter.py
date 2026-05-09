"""Text structure-aware splitter example.

This splitter uses RecursiveCharacterTextSplitter with various separator strategies
to split text while respecting document structure (paragraphs, sentences, words).
Useful for: generic text, mixed-format content, fallback chunking strategy.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter


text = """This is a long text that needs to be split into smaller chunks. The recursive character splitter will split
the text based on a specified character limit and overlap. It is useful for processing large documents or texts that exceed certain limits.

The recursive character splitter can be configured to split the text at specific characters, such as spaces or punctuation marks,
to ensure that the chunks are meaningful and easy to read. The recursive character splitter will split the text based on a specified
character limit and overlap.

It is useful for processing large documents or texts that exceed certain limits. The recursive character splitter can be configured to split
the text at specific characters, such as spaces or punctuation marks, to ensure that the chunks are meaningful and easy to read.

The recursive character splitter will split the text based on a specified character limit and overlap. It is useful for processing large
documents or texts that exceed certain limits. The recursive character splitter can be configured to split the text at specific characters,
such as spaces or punctuation marks, to ensure that the chunks are meaningful and easy to read.

It is useful for processing large documents or texts that exceed certain limits.
The recursive character splitter can be configured to split the text at specific characters, such as spaces or punctuation marks,
to ensure that the chunks are meaningful and easy to read.
"""

# RecursiveCharacterTextSplitter with custom separators
# Separators are tried in order: first match wins
# This creates a hierarchy: paragraphs -> sentences -> words -> characters
print("=== Text Structure-Based Splitter ===")
print("(Tries separators in order: double newline → newline → space → character)\n")

# Configuration explained:
# chunk_size: 200 characters per chunk
# chunk_overlap: 20 characters of overlap (preserves context between chunks)
# separators: List of separators to try in order
#   - "\n\n": Paragraph separator (highest priority)
#   - "\n": Line separator
#   - " ": Word separator
#   - "": Character level fallback (lowest priority)
splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20,
    separators=["\n\n", "\n", " ", ""]
)

chunks = splitter.split_text(text)

print(f"Total chunks created: {len(chunks)}\n")

for i, chunk in enumerate(chunks, 1):
    # Display chunk index, size, and content
    print(f"Chunk {i} ({len(chunk)} chars):")
    print(f"{chunk}")
    print("-" * 60)


# Example 2: More aggressive chunking (smaller chunks)
print("\n=== Smaller Chunks Example ===")
aggressive_splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=10
)

small_chunks = aggressive_splitter.split_text(text)
print(f"Total smaller chunks: {len(small_chunks)}")
for i, chunk in enumerate(small_chunks[:5], 1):  # Show first 5
    print(f"Chunk {i}: {chunk[:50]}...")
