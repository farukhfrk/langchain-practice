"""
RunnableParallel with Multiple Models Example

This module demonstrates generating multiple outputs from a single input
using RunnableParallel with different prompts and models.

The workflow:
1. Input topic: "AI in 2024"
2. Generate tweet (social media post)
3. Generate LinkedIn post (professional content)
4. Both run in parallel for efficiency

This pattern is useful for:
- Multi-channel content generation
- Generating different perspectives on the same topic
- Parallel processing for performance

Example:
    python runnable_parallel.py
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define prompt for Twitter/X content
# Twitter has character limits and requires engaging, concise language
prompt1 = PromptTemplate(
    template='generate a tweet on the topic {topic}',   
    input_variables=['topic']
)

# Define prompt for LinkedIn content
# LinkedIn requires professional, detailed posts with industry insights
prompt2 = PromptTemplate(
    template='generate a linkedin post on the topic {topic}',
    input_variables=['topic']   
)

# Initialize language model
model = ChatOpenAI()

# Initialize output parser to convert model output to string
parser = StrOutputParser()

# Create parallel chains for both platforms
# Each chain: prompt -> model -> parser
# Both chains receive the same input but use different prompts
# parallel_chain = {
#     'tweet': RunnableSequence(prompt1, model, parser),      # Generate tweet
#     'linkedin': RunnableSequence(prompt2, model, parser)    # Generate LinkedIn post
# }

# LCEL version - using pipe operator
parallel_chain = RunnableParallel({
    'tweet': prompt1 | model | parser,
    'linkedin': prompt2 | model | parser
})

# Execute the parallel chain with a topic
result = parallel_chain.invoke({'topic': 'AI in 2024'})

# Display results from both channels
print("=== TWITTER/X POST ===")
print(result['tweet'])

print("\n=== LINKEDIN POST ===")
print(result['linkedin'])