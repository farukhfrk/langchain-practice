"""Python code-aware text splitter example.

This splitter divides Python code while respecting Python syntax (functions, classes).
Useful for: source code files, Python documentation, code examples.
"""

from langchain_text_splitters import (
    PythonCodeTextSplitter,
    RecursiveCharacterTextSplitter,
    Language,
)


python_code = """def add(a, b):
    '''Add two numbers together.'''
    return a + b

def subtract(a, b):
    '''Subtract two numbers.'''
    return a - b

def multiply(a, b):
    '''Multiply two numbers together.'''
    return a * b

def divide(a, b):
    '''Divide two numbers.'''
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class Calculator:
    '''A simple calculator class with basic arithmetic operations.'''

    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
"""

# Example 1: Using PythonCodeTextSplitter
# This splitter is optimized for Python code structure
print("=== Python Code Splitter (Specialized) ===")
code_splitter = PythonCodeTextSplitter(chunk_size=120, chunk_overlap=20)
code_chunks = code_splitter.split_text(python_code)

for i, chunk in enumerate(code_chunks, 1):
    print(f"Chunk {i}:\n{chunk}\n")
    print("-" * 50)


# Example 2: Using RecursiveCharacterTextSplitter with PYTHON language
# This is more flexible and respects Python syntax better
print("\n=== Recursive Splitter (Language-aware) ===")
recursive_splitter = RecursiveCharacterTextSplitter.from_language(
    chunk_size=300,
    chunk_overlap=20,
    language=Language.PYTHON
)

recursive_chunks = recursive_splitter.split_text(python_code)

for i, chunk in enumerate(recursive_chunks, 1):
    print(f"Recursive Chunk {i} ({len(chunk)} chars):\n{chunk}\n")
    print("-" * 50)

print(f"\nSummary:")
print(f"- Code Splitter produced {len(code_chunks)} chunks")
print(f"- Recursive Splitter produced {len(recursive_chunks)} chunks")
