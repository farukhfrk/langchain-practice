# LangChain Text Splitters

Educational examples demonstrating different text splitting strategies for document processing and chunking using LangChain.

## 📚 Overview

Text splitting is a crucial preprocessing step when working with large documents in large language models (LLMs). This repository provides practical examples of various splitting strategies, each optimized for different use cases.

## 🎯 Splitter Types

### 1. **Character Splitter** (`character_splitter.py`)
**Purpose:** Split text into chunks by character count, with optional overlap.

**When to use:**
- Simple text processing
- When no special structure exists
- Basic preprocessing
- Language-agnostic tasks

**Key Parameters:**
- `chunk_size`: Maximum characters per chunk
- `chunk_overlap`: Overlapping characters between chunks (preserves context)
- `separator`: Character to split on

**Example:**
```python
from langchain_text_splitters import CharacterTextSplitter

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separator=" "
)
chunks = splitter.split_text(text)
```

**Tradeoff:** Simple and fast, but doesn't respect document structure or semantics.

---

### 2. **Markdown Splitter** (`markdown_splitter.py`)
**Purpose:** Split markdown documents while respecting markdown structure (headers, sections).

**When to use:**
- Markdown documentation
- README files
- Technical documentation with structure
- Articles with hierarchical organization

**Key Parameters:**
- `chunk_size`: Maximum characters per chunk
- `chunk_overlap`: Overlapping characters
- `language`: Set to `Language.MARKDOWN`

**Example:**
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

splitter = RecursiveCharacterTextSplitter.from_language(
    chunk_size=500,
    chunk_overlap=20,
    language=Language.MARKDOWN
)
chunks = splitter.split_text(markdown_text)
```

**Tradeoff:** Preserves structure but may create larger chunks to keep sections together.

---

### 3. **Python Code Splitter** (`python_code_splitter.py`)
**Purpose:** Split Python code while preserving function and class definitions.

**When to use:**
- Source code files
- Python documentation with code examples
- Code-based tutorials
- API documentation

**Key Parameters:**
- `chunk_size`: Maximum characters per chunk
- `chunk_overlap`: Overlapping characters
- `language`: Set to `Language.PYTHON`

**Example:**
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

splitter = RecursiveCharacterTextSplitter.from_language(
    chunk_size=300,
    chunk_overlap=20,
    language=Language.PYTHON
)
chunks = splitter.split_text(python_code)
```

**Tradeoff:** Respects syntax but may create uneven chunk sizes.

---

### 4. **Semantic Splitter** (`semantic_splitter.py`)
**Purpose:** Split text based on semantic meaning using embeddings.

**When to use:**
- Long-form content (articles, blog posts)
- Preserving semantic coherence
- Topic-based document division
- When context and meaning matter most

**Key Parameters:**
- `embeddings`: Embedding model (e.g., OpenAIEmbeddings)
- `breakpoint_threshold_type`: `"standard_deviation"` or `"percentile"`
- `breakpoint_threshold_amount`: Sensitivity (higher = fewer, larger chunks)

**Example:**
```python
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_experimental.text_splitter import SemanticChunker

splitter = SemanticChunker(
    OpenAIEmbeddings(),
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1.0
)
chunks = splitter.split_text(text)
```

**Requirements:** OpenAI API key (set `OPENAI_API_KEY` environment variable)

**Tradeoff:** Most accurate but slower and requires API calls for embeddings.

---

### 5. **Text Structure-Based Splitter** (`text_structure_based_splitter.py`)
**Purpose:** Split text using a hierarchy of separators (paragraphs → sentences → words → characters).

**When to use:**
- Mixed-format content
- Generic text without special structure
- Fallback strategy
- Flexible chunking needs

**Key Parameters:**
- `chunk_size`: Maximum characters per chunk
- `chunk_overlap`: Overlapping characters
- `separators`: List of separators tried in order

**Example:**
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20,
    separators=["\n\n", "\n", " ", ""]
)
chunks = splitter.split_text(text)
```

**Tradeoff:** Flexible and balanced; good general-purpose choice.

---

## 📊 Comparison Table

| Splitter | Speed | Structure Aware | Semantic | Best For |
|----------|-------|-----------------|----------|----------|
| Character | ⚡⚡⚡ | ❌ | ❌ | Simple text |
| Markdown | ⚡⚡ | ✅ | ❌ | Documentation |
| Python Code | ⚡⚡ | ✅ | ❌ | Source code |
| Semantic | 🐢 | ⚠️ | ✅ | Long-form content |
| Structure-Based | ⚡⚡ | ✅ | ❌ | Mixed content |

---

## 🔧 Installation

### Prerequisites
- Python 3.8+
- pip

### Install Dependencies

```bash
pip install langchain langchain-community langchain-text-splitters
```

**For Semantic Splitter (optional):**
```bash
pip install langchain-experimental openai
export OPENAI_API_KEY="your-api-key-here"  # On Windows: set OPENAI_API_KEY=your-api-key-here
```

---

## 🚀 Quick Start

### 1. Basic Character Splitting
```bash
python character_splitter.py
```

### 2. Markdown Splitting
```bash
python markdown_splitter.py
```

### 3. Python Code Splitting
```bash
python python_code_splitter.py
```

### 4. Semantic Splitting (requires OpenAI API key)
```bash
python semantic_splitter.py
```

### 5. Structure-Based Splitting
```bash
python text_structure_based_splitter.py
```

---

## 📖 Understanding Chunk Parameters

### `chunk_size`
The maximum number of characters in each chunk.
- **Larger chunks**: More context, fewer API calls, better for embeddings
- **Smaller chunks**: More granular control, better for retrieval

**Recommendation:** 500-1000 for typical use cases

### `chunk_overlap`
Number of characters that overlap between consecutive chunks.
- **Purpose**: Preserve context to avoid losing important information at chunk boundaries
- **Typical value**: 10-20% of chunk_size

**Example:**
```
chunk_size=100, chunk_overlap=20

Text: "The quick brown fox jumps over the lazy dog. The dog is very lazy."

Chunk 1: "The quick brown fox jumps over the lazy dog. The"
Chunk 2: "lazy dog. The dog is very lazy."
           ^^^^^^    (20-char overlap)
```

### `separator`
Character or pattern to split on:
- `" "` (space): Split by words
- `"\n"` (newline): Split by lines
- `""` (empty): Character-by-character
- Custom: Any string pattern

---

## 💡 Chunking Strategy Guide

### Choose Based On:

1. **Document Type:**
   - Markdown/Docs → Use Markdown Splitter
   - Code → Use Python Code Splitter
   - Long-form → Use Semantic Splitter
   - Generic → Use Structure-Based Splitter

2. **Performance Requirements:**
   - Need speed → Use Character or Structure-Based
   - Can wait → Use Semantic

3. **Use Case:**
   - RAG (Retrieval-Augmented Generation) → Semantic
   - Search indexing → Structure-Based
   - Quick preprocessing → Character

---

## 🔍 Common Patterns

### Pattern 1: Document + Vector Store
```python
# Split document
splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
chunks = splitter.split_documents(documents)

# Store in vector database
for chunk in chunks:
    embedding = embedding_model.embed(chunk.page_content)
    vector_store.add(chunk, embedding)
```

### Pattern 2: Split for LLM Context Window
```python
# GPT-4: 8K tokens ≈ 32K characters
# Claude: 100K tokens ≈ 400K characters

splitter = RecursiveCharacterTextSplitter(
    chunk_size=2000,  # Conservative: stays under token limit
    chunk_overlap=200
)
chunks = splitter.split_documents(documents)
```

### Pattern 3: Hierarchical Chunking
```python
# First pass: split by section
section_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
sections = section_splitter.split_documents(documents)

# Second pass: split sections further if needed
chunk_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = chunk_splitter.split_documents(sections)
```

---

## 🧪 Testing Your Splitter

```python
def test_splitter(splitter, text, min_chars=50, max_chars=1000):
    """Test a splitter configuration."""
    chunks = splitter.split_text(text)
    
    print(f"Chunks created: {len(chunks)}")
    print(f"Average chunk size: {sum(len(c) for c in chunks) // len(chunks)}")
    print(f"Min chunk size: {min(len(c) for c in chunks)}")
    print(f"Max chunk size: {max(len(c) for c in chunks)}")
    
    # Check overlap
    if len(chunks) > 1:
        overlap = len(set(chunks[0]) & set(chunks[1]))
        print(f"Average overlap with next chunk: ~{overlap} chars")
    
    return chunks
```

---

## 📝 Best Practices

1. **Start simple**: Use Character or Structure-Based splitter first
2. **Measure quality**: Test with your specific use case
3. **Balance tradeoffs**: Speed vs. quality
4. **Monitor chunk distribution**: Avoid very large or very small chunks
5. **Use overlap**: Always include 10-20% overlap
6. **Test retrieval**: For RAG, test actual search quality

---

## 🤝 Contributing

To add new splitter examples:
1. Create a new file: `name_splitter.py`
2. Add docstring explaining the splitter
3. Include multiple examples
4. Update this README
5. Follow the same code structure as existing examples

---

## 📚 Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Text Splitters Guide](https://python.langchain.com/docs/modules/data_connection/document_transformers/text_splitters/)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)

---

## ⚠️ Security Notes

- Store API keys in environment variables (never commit to git)
- Test with sample data before production use
- Monitor API usage for cost management
- Validate file paths before processing

---

## 📄 License

This repository is for educational purposes. Refer to the main LangChain repository for license information.

---

## 🎓 Learning Outcomes

By working through these examples, you'll understand:
- ✅ Different text splitting strategies
- ✅ When to use each splitter type
- ✅ How to configure chunk size and overlap
- ✅ Real-world tradeoffs
- ✅ Performance considerations
- ✅ Integration with LLM workflows

Happy learning! 🚀
