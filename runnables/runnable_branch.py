from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnableBranch, RunnableSequence, RunnablePassthrough
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize language model and parser
model = ChatOpenAI(model='gpt-4o')
parser = StrOutputParser()

# Define prompt template
template = PromptTemplate(
    template='Write a report about {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='summarize the report {text}',
    input_variables=['text']
)

report_gen_chain = RunnableSequence(template, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>500, RunnableSequence(template2, model, parser)),
    RunnablePassthrough()
)
final_chain = RunnableSequence(report_gen_chain, branch_chain)

# Example 1: Test the final chain with a topic that generates a long report
print("=== RunnableBranch Example with Long Report ===")
result = final_chain.invoke({'topic': 'The history of artificial intelligence and its impact on society'})
print("Final Result:", result)
