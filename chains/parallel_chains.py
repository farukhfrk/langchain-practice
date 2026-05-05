"""
Parallel Chain Example

This module demonstrates how to run multiple chains in parallel using RunnableParallel.
The same input is processed by different chains simultaneously, then the results
are merged.

The chain performs:
1. Generate notes from text (using OpenAI)
2. Generate quiz from text (using Anthropic) - in parallel
3. Merge notes and quiz into a single document

This pattern is useful for generating multiple perspectives or outputs from the
same input without sequential dependencies.

Example:
    python parallel_chains.py
"""

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

# Load environment variables
load_dotenv()

# Initialize models from different providers
# Model 1: OpenAI for general tasks
model1 = ChatOpenAI()

# Model 2: Anthropic Claude for alternative perspective
model2 = ChatAnthropic(model_name='claude-3-7-sonnet-20250219')

# Define prompt for generating notes
prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

# Define prompt for generating quiz questions and answers
prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)

# Define prompt for merging outputs
prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

# Initialize output parser
parser = StrOutputParser()

# Create parallel chains: both chains run with the same input
# 'notes' chain: generates notes using OpenAI
# 'quiz' chain: generates quiz using Anthropic
parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

# Create merge chain to combine results
merge_chain = prompt3 | model1 | parser

# Complete workflow: parallel execution followed by merge
chain = parallel_chain | merge_chain

# Sample text about Support Vector Machines
text = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
"""

# Execute the chain
result = chain.invoke({'text': text})

print(result)

# Visualize the chain structure
print("\n--- Chain Structure ---")
chain.get_graph().print_ascii()
