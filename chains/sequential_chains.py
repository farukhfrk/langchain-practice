"""
Sequential Chain Example

This module demonstrates how to chain multiple prompts and models in sequence.
Each output from one stage becomes the input to the next stage.

The chain performs:
1. Generate detailed report on a topic
2. Create 5-point summary from the generated report

This is useful for multi-step processing where each step builds on the previous.

Example:
    python sequential_chains.py
"""

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Define the first prompt: Generate detailed report
prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

# Define the second prompt: Create summary from text
# Note: {text} will receive the output from the first chain
prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

# Initialize the language model
model = ChatOpenAI()

# Initialize output parser
parser = StrOutputParser()

# Compose the sequential chain:
# 1. Start with prompt1 (takes 'topic' as input)
# 2. Pass to model for generation
# 3. Parse output as string
# 4. Pass parsed text to prompt2
# 5. Pass prompt2 to model again
# 6. Parse final output
chain = prompt1 | model | parser | prompt2 | model | parser

# Execute the chain with a topic
result = chain.invoke({'topic': 'Unemployment in India'})

print(result)

# Visualize the chain structure
print("\n--- Chain Structure ---")
chain.get_graph().print_ascii()