"""
RunnablePassthrough and RunnableParallel with Explanation Example

This module demonstrates how RunnablePassthrough is used to preserve
intermediate results in a pipeline.

The workflow:
1. Generate a joke about a topic
2. In parallel:
   - Pass through the joke (using RunnablePassthrough)
   - Generate an explanation of the joke
3. Return both the joke and its explanation

This pattern is useful when you need to preserve intermediate results
and perform multiple operations on them.

Example:
    python runnable_passthrough.py
"""

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnablePassthrough
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Define prompt for generating jokes
prompt = PromptTemplate(
    template='write a joke on the {topic}',
    input_variables=['topic']
)

# Define prompt for explaining jokes
prompt2 = PromptTemplate(
    template='explain the following joke {text}',
    input_variables=['text']
)

# Initialize language model
model = ChatOpenAI()

# Initialize output parser
parser = StrOutputParser()

# Create chain for joke generation: prompt -> model -> parser
# This produces a joke string
joke_gen_chain = RunnableSequence(prompt, model, parser)

# Create chain for joke explanation: prompt -> model -> parser
# This takes a joke and explains it
joke_explain_chain = RunnableSequence(prompt2, model, parser)

# Create parallel chain that:
# - 'printjoke': RunnablePassthrough() passes the joke through unchanged
# - 'explanation': joke_explain_chain processes the joke to generate explanation
parallel_chain = RunnableParallel({
    'printjoke': RunnablePassthrough(),
    'explanation': joke_explain_chain
})

# Create final chain: generate joke first, then process it in parallel
# 1. joke_gen_chain generates the joke
# 2. parallel_chain receives the joke and:
#    - Passes it through as 'printjoke'
#    - Generates explanation as 'explanation'
final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

# Execute the complete workflow
result = final_chain.invoke({'topic': 'chicken'})

# Display results
print("=== Generated Joke ===")
print(result['printjoke'])

print("\n=== Explanation ===")
print(result['explanation'])
