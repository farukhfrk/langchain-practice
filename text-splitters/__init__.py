"""LangChain Text Splitters - Educational Examples

This package contains implementations and examples of various text splitting strategies
used in LangChain for document processing and chunking.

Examples:
    - Character Splitter: Split by character count
    - Markdown Splitter: Split while respecting markdown structure
    - Python Code Splitter: Split Python code while preserving syntax
    - Semantic Splitter: Split based on semantic meaning using embeddings
    - Text Structure-Based Splitter: Split using hierarchical separators

Each module contains standalone examples that demonstrate:
    1. How to initialize the splitter
    2. Configuration parameters
    3. Usage patterns
    4. Output handling
"""

__version__ = "0.1.0"
__author__ = "Your Name"

# Import commonly used splitters for convenience
try:
    from langchain_text_splitters import (
        CharacterTextSplitter,
        RecursiveCharacterTextSplitter,
        Language,
    )
    from langchain_experimental.text_splitter import SemanticChunker

    __all__ = [
        "CharacterTextSplitter",
        "RecursiveCharacterTextSplitter",
        "Language",
        "SemanticChunker",
    ]
except ImportError:
    pass
