# LangChain Practice and Learning Repository

A comprehensive collection of LangChain examples demonstrating core concepts including chains, runnables, embeddings, chat models, and output parsing. Perfect for learning and practicing generative AI with LangChain.

## 📚 Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage Examples](#usage-examples)
- [Module Documentation](#module-documentation)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This repository contains practical examples of LangChain implementations covering:

- **Document Loaders**: Ingesting data from various sources (PDFs, web, CSV, text files)
- **Chains**: Sequential and parallel composition of prompts and models
- **Runnables**: Advanced patterns for building complex LLM workflows
- **Embeddings**: Document embedding and semantic similarity search
- **Chat Models**: Integration with multiple LLM providers
- **Output Parsing**: Structured data extraction from LLM outputs

All examples are fully documented with docstrings and inline comments for easy understanding.

## 📁 Project Structure

```
langchain/
├── document-loaders/                # Data ingestion from multiple sources
│   ├── __init__.py
│   ├── README.md                    # Detailed documentation
│   ├── text_loader.py               # Load plain text files
│   ├── pypdf_loader.py              # Extract text from PDFs
│   ├── webbase_loader.py            # Scrape web content
│   ├── directory_loader.py          # Batch load multiple files
│   ├── csv_loader.py                # Process CSV data
│   ├── example.txt                  # Sample text file
│   ├── example.csv                  # Sample CSV data
│   └── sample-local-pdf.pdf         # Sample PDF document
│
├── chains/                          # Chain composition examples
│   ├── __init__.py
│   ├── simple_chain.py             # Basic prompt -> model -> parser
│   ├── sequential_chains.py        # Multi-step sequential chains
│   └── parallel_chains.py          # Parallel execution with multiple models
│
├── ChatModels/                      # LLM provider integrations
│   ├── __init__.py
│   └── hf_api.py                   # Hugging Face API integration
│
├── EmbeddingModels/                # Embedding and semantic search
│   ├── __init__.py
│   ├── 1_document_similarity.py    # Semantic similarity search
│   └── output/                      # Output parsing examples
│       ├── __init__.py
│       ├── pydanticOutputParser.py # Type-safe structured output
│       ├── jsonOutputParser.py     # JSON output parsing
│       ├── strOutput_parser.py     # String output parsing
│       ├── with_structured_output.py
│       └── with_structured_output_json.py
│
├── runnables/                       # Runnable patterns
│   ├── __init__.py
│   ├── NakliLLM.py                 # Mock LLM implementation
│   ├── NakliChain.py               # Custom chain implementation
│   ├── runnable_lambda.py          # Lambda functions as runnables
│   ├── runnable_sequence.py        # Sequential composition
│   ├── runnable_parallel.py        # Parallel execution
│   └── runnable_passthrough.py     # Pass-through operations
│
├── __init__.py                      # Package initialization
├── requirements.txt                 # Project dependencies
├── .gitignore                       # Git ignore rules
├── .env.example                     # Environment variables template
└── README.md                        # This file
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/langchain-practice.git
cd langchain
```

### Step 2: Create Virtual Environment

```bash
# Using venv
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root with your API keys:

```bash
# Copy the example file
cp .env.example .env

# Edit .env with your credentials
```

**Required environment variables:**

```env
# OpenAI API
OPENAI_API_KEY=your_openai_api_key

# Anthropic API (optional, for Claude models)
ANTHROPIC_API_KEY=your_anthropic_api_key

# Hugging Face API (optional)
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
HF_INFERENCE_ENDPOINT=your_inference_endpoint

# Other configurations
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_key
```

## 📖 Usage Examples

### 1. Simple Chain

```bash
cd chains
python simple_chain.py
```

**Output**: 5 interesting facts about 2026

### 2. Sequential Chains

```bash
python sequential_chains.py
```

**Process**:
1. Generate detailed report on "Unemployment in India"
2. Create 5-point summary of the report

### 3. Parallel Chains

```bash
python parallel_chains.py
```

**Process**:
1. Generate notes using OpenAI (parallel with...)
2. Generate quiz using Anthropic (parallel execution)
3. Merge notes and quiz into single document

### 4. Document Similarity Search

```bash
cd ../EmbeddingModels
python 1_document_similarity.py
```

**Purpose**: Find semantically similar documents using embeddings

### 5. Custom Mock LLM Chain

```bash
cd ../runnables
python NakliChain.py
```

**Purpose**: Demonstrates custom chain implementation without API calls

### 6. Runnable Patterns

```bash
# Lambda functions as runnables
python runnable_lambda.py

# Sequential composition
python runnable_sequence.py

# Parallel execution
python runnable_parallel.py

# Pass-through operations
python runnable_passthrough.py
```

### 7. Output Parsing

```bash
cd ../EmbeddingModels/output
python pydanticOutputParser.py      # Type-safe structured output
python jsonOutputParser.py          # JSON parsing
```

## 📚 Module Documentation

### Chains Module

| File | Purpose |
|------|---------|
| `simple_chain.py` | Basic prompt → model → parser chain |
| `sequential_chains.py` | Multi-step chains where output feeds to next step |
| `parallel_chains.py` | Multiple chains running simultaneously |

### ChatModels Module

| File | Purpose |
|------|---------|
| `hf_api.py` | Hugging Face Inference API integration |

### EmbeddingModels Module

| File | Purpose |
|------|---------|
| `1_document_similarity.py` | Semantic search using embeddings |
| `pydanticOutputParser.py` | Type-safe output parsing with Pydantic |
| `jsonOutputParser.py` | JSON output parsing |

### Runnables Module

| File | Purpose |
|------|---------|
| `NakliLLM.py` | Mock LLM and prompt template for learning |
| `NakliChain.py` | Custom chain combining LLM and prompt |
| `runnable_lambda.py` | Using Python functions as runnables |
| `runnable_sequence.py` | Sequential composition of runnables |
| `runnable_parallel.py` | Parallel execution of multiple runnables |
| `runnable_passthrough.py` | Pass-through with parallel processing |

## 🔑 Key Concepts

### Chains

Chains compose multiple components (prompts, models, parsers) using the pipe operator (`|`):

```python
chain = prompt | model | parser
result = chain.invoke({'variable': 'value'})
```

### Runnables

Advanced patterns for building complex workflows:
- **RunnableLambda**: Wrap Python functions
- **RunnableSequence**: Chain operations sequentially
- **RunnableParallel**: Execute multiple operations in parallel
- **RunnablePassthrough**: Preserve intermediate results

### Embeddings

Convert text to dense vectors for semantic understanding:

```python
embeddings = OpenAIEmbeddings()
doc_embeddings = embeddings.embed_documents(documents)
similarity = cosine_similarity([query_embedding], doc_embeddings)
```

### Output Parsers

Structure LLM outputs:
- **StrOutputParser**: Simple string output
- **JsonOutputParser**: JSON formatted output
- **PydanticOutputParser**: Type-safe structured output

## 💡 Learning Path

1. **Start here**: `chains/simple_chain.py` - Understand basic composition
2. **Next**: `chains/sequential_chains.py` - Learn sequential processing
3. **Then**: `chains/parallel_chains.py` - Parallel execution patterns
4. **Advanced**: `runnables/` - Complex workflow patterns
5. **Practice**: `EmbeddingModels/` - Semantic search and embeddings
6. **Specialize**: `EmbeddingModels/output/` - Output parsing techniques

## 🛠️ Common Issues and Solutions

### Issue: `OPENAI_API_KEY not set`

**Solution**: Add your API key to `.env` file

```env
OPENAI_API_KEY=sk-...
```

### Issue: `ModuleNotFoundError: No module named 'langchain'`

**Solution**: Install dependencies

```bash
pip install -r requirements.txt
```

### Issue: `ConnectionError` when calling LLM

**Solution**: Verify your internet connection and API key validity

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Add comments and docstrings to your code
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## 📝 Code Style Guidelines

- Use clear, descriptive variable names
- Add module-level docstrings explaining purpose
- Add function docstrings with Args, Returns, and Examples
- Include inline comments for complex logic
- Follow PEP 8 style guide

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🎓 Educational Resources

- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Anthropic Claude Documentation](https://docs.anthropic.com/)
- [Hugging Face Documentation](https://huggingface.co/docs)

## 📧 Contact and Support

For questions, suggestions, or issues:
- Open an issue on GitHub
- Create a discussion thread
- Check existing documentation

## 🙏 Acknowledgments

- LangChain team for the excellent framework
- OpenAI, Anthropic, and Hugging Face for their APIs
- Community contributors and feedback

---

**Happy Learning! 🚀**

*Last Updated: May 2026*
*Version: 1.0.0*
