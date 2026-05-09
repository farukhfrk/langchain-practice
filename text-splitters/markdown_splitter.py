"""Markdown-aware text splitter example.

This splitter divides markdown text while respecting markdown structure (headers, sections).
Useful for: documentation, markdown files, structured text with headings.
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter, Language


markdown_text = """# Main Title

## Introduction

This is a long text that needs to be split into smaller chunks. The recursive character
splitter will split the text based on a specified character limit and overlap. It is useful
for processing large documents or texts that exceed certain limits.

The recursive character splitter can be configured to split the text at specific characters,
such as spaces or punctuation marks, to ensure that the chunks are meaningful and easy to read.

## Key Concepts

The recursive character splitter will split the text based on a specified character limit
and overlap. It is useful for processing large documents or texts that exceed certain limits.

### Subsection 1

Additional details about the first concept.

### Subsection 2

Additional details about the second concept.

## Conclusion

The recursive character splitter will split the text based on a specified character limit
and overlap. It is useful for processing large documents or texts that exceed certain limits.

The recursive character splitter can be configured to split the text at specific characters,
such as spaces or punctuation marks, to ensure that the chunks are meaningful and easy to read.
"""

# chunk_size: Maximum number of characters per chunk
# chunk_overlap: Number of overlapping characters to preserve context between chunks
# language: Specifies Language.MARKDOWN for markdown-aware splitting
# The splitter respects markdown structure (headers, sections) when splitting
splitter = RecursiveCharacterTextSplitter.from_language(
    chunk_size=500,
    chunk_overlap=20,
    language=Language.MARKDOWN
)

chunks = splitter.split_text(markdown_text)

print("=== Markdown Splitter ===")
print(f"Total chunks created: {len(chunks)}\n")

for i, chunk in enumerate(chunks, 1):
    print(f"Chunk {i} ({len(chunk)} chars):")
    print(f"{chunk}\n")
    print("-" * 50)
