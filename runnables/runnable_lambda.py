"""
RunnableLambda, RunnableParallel, and RunnableSequence Examples

This module demonstrates different runnable patterns in LangChain:

1. RunnableLambda: Wraps a Python function as a runnable component
2. RunnableParallel: Runs multiple runnables in parallel
3. RunnableSequence: Chains multiple runnables sequentially
4. RunnablePassthrough: Passes data through unchanged

These patterns enable complex LLM workflows by composing simple components.

Example:
    python runnable_lambda.py
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnableSequence, RunnablePassthrough
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def word_counter(text):
    """
    Count the number of words in a given text.
    
    Args:
        text (str): The input text
        
    Returns:
        int: The number of words in the text
    """
    return len(text.split())


# Initialize language model and parser
model = ChatOpenAI(model='gpt-4o')
parser = StrOutputParser()

# Define prompt template
template = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

# Convert the word_counter function into a runnable component
# This allows us to use it in chains and parallel workflows
runnable_counter = RunnableLambda(word_counter)

# Example 1: Test the word counter runnable directly
print("=== RunnableLambda Example ===")
print(f"Word count: {runnable_counter.invoke('This is a test joke.')}")  # Should print 5

# Example 2: Create a parallel runnable that:
# - Counts words in output (lambdaResult)
# - Passes through the original text (printJoke)
print("\n=== RunnableParallel and RunnableSequence Example ===")
runnable_parallel = RunnableParallel({
    'lambdaResult': lambda word: len(word.split()),  # Count words
    'printJoke': RunnablePassthrough()  # Pass through unchanged
})

# Create sequence: template -> model -> parser -> parallel
# The parser output (string) goes into the parallel runnable
chain1 = RunnableSequence(template, model, parser, runnable_parallel)

# Execute the chain
result = chain1.invoke({'topic': 'chickens'})
print(result)