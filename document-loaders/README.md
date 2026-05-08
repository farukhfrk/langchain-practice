# Document Loaders Examples

This directory contains practical examples demonstrating LangChain's document loading capabilities. Learn how to load and process different document formats and integrate them with language models.

## 📋 Overview

Document loaders are essential components for ingesting data from various sources into LangChain applications. These examples show how to:
- Load documents from different file formats
- Process and parse document content
- Chain loaders with LLMs for analysis
- Handle metadata and document properties

## 📁 Files

### 1. **text_loader.py** - Text File Loading
Load and analyze plain text files using `TextLoader`.

```bash
python text_loader.py
```

**What it does:**
- Loads a single text file
- Extracts document content and metadata
- Sends content to an LLM for topic analysis

**Use cases:**
- Processing logs, reports, and documentation
- Batch processing multiple text files

---

### 2. **directory_loader.py** - Batch Directory Loading
Load multiple files from a directory using `DirectoryLoader`.

```bash
python directory_loader.py
```

**What it does:**
- Loads all `.txt` files from the current directory
- Demonstrates recursive file discovery with glob patterns
- Shows progress during loading
- Processes multiple documents in sequence

**Use cases:**
- Batch processing entire directories
- Multi-document analysis pipelines
- Building document corpora

**Customization:**
```python
# Load different file types
glob='**/*.md'  # Markdown files
glob='**/*.json'  # JSON files
glob='*.txt'  # Only top-level files
```

---

### 3. **pypdf_loader.py** - PDF Document Loading
Extract and analyze PDF documents using `PyPDFLoader`.

```bash
python pypdf_loader.py
```

**What it does:**
- Loads PDF documents page by page
- Extracts text content and metadata
- Preserves page numbers and source information
- Integrates with LLM for content analysis

**Dependencies:**
```bash
pip install pypdf
```

**Use cases:**
- Processing research papers and reports
- Extracting text from scanned documents
- Building searchable document indexes

---

### 4. **webbase_loader.py** - Web Content Loading
Scrape and analyze web pages using `WebBaseLoader`.

```bash
python webbase_loader.py
```

**What it does:**
- Fetches content from web URLs
- Cleans HTML and extracts main content using BeautifulSoup
- Preserves source metadata
- Enables web-based document analysis

**Dependencies:**
```bash
pip install beautifulsoup4 lxml
```

**Use cases:**
- Analyzing blog posts and articles
- Extracting information from websites
- Building knowledge bases from web sources

---

### 5. **csv_loader.py** - CSV Data Loading
Load and process structured CSV data using `CSVLoader`.

```bash
python csv_loader.py
```

**What it does:**
- Loads CSV files with structured data
- Converts each row into a document
- Preserves column headers and data
- Enables analysis of tabular data

**Use cases:**
- Processing survey responses
- Analyzing datasets
- Structured data ingestion pipelines

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- OpenAI API key (for LLM analysis)
- Required libraries

### Installation

```bash
# Install dependencies
pip install -r ../requirements.txt

# Set up environment variables
cp ../.env.example ../.env
# Edit .env and add your API keys
```

### Run Examples

```bash
# Run individual examples
python text_loader.py
python directory_loader.py
python pypdf_loader.py
python webbase_loader.py
python csv_loader.py
```

## 📝 Sample Data

The directory includes sample files for testing:
- `example.txt` - Sample text file
- `example.csv` - Sample CSV data
- `sample-local-pdf.pdf` - Sample PDF document

## 🔧 Common Patterns

### Load and Chain with LLM

```python
from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load document
loader = TextLoader('path/to/file.txt', encoding='utf-8')
docs = loader.load()

# Create LLM chain
model = ChatOpenAI()
prompt = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text:\n\n{text}",
)
chain = prompt | model | StrOutputParser()

# Process document
result = chain.invoke({'text': docs[0].page_content})
print(result)
```

### Process Multiple Documents

```python
from langchain_community.document_loaders import DirectoryLoader, TextLoader

loader = DirectoryLoader(
    'path/to/documents',
    glob='**/*.txt',
    loader_cls=TextLoader,
    show_progress=True
)
docs = loader.load()

for doc in docs:
    print(f"File: {doc.metadata['source']}")
    print(f"Content: {doc.page_content[:200]}...")
```

## 🌐 Environment Variables

Create a `.env` file with required API keys:

```env
OPENAI_API_KEY=your_openai_key_here
HUGGINGFACEHUB_API_TOKEN=your_hf_token_here
```

**Never commit the `.env` file to version control!**

## 📚 Learning Resources

- [LangChain Documentation](https://python.langchain.com/docs/)
- [Document Loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/)
- [PyPDF Documentation](https://github.com/py-pdf/PyPDF)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## 🤝 Contributing

To extend these examples:

1. Create a new loader file: `my_loader.py`
2. Follow the existing pattern with clear comments
3. Include sample data
4. Add documentation in this README
5. Test the example before submitting

## 📄 License

Part of the LangChain Practice repository. See main LICENSE file.
