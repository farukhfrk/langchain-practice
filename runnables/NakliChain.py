"""
Custom Mock Chain Implementation

This module demonstrates a simplified chain implementation by combining
a mock prompt template with a mock LLM.

Classes:
    NakLiLLMChain: A custom chain combining NakliLLM and NakliPromptTemplate

This shows how LangChain chains work at a fundamental level:
1. Format the prompt with input variables
2. Pass formatted prompt to LLM
3. Return the LLM's response

Note: "Nakli" means "fake" or "mock" in Hindi.
"""

from NakliLLM import NakliLLM
from NakliLLM import NakliPromptTemplate


class NakLiLLMChain:
    """
    A custom chain combining a prompt template and an LLM.
    
    This is a simplified version of LangChain's LLMChain that demonstrates
    the core pattern: template -> format -> model -> predict.
    
    Attributes:
        llm: The language model to use for predictions
        prompt: The prompt template to format inputs
        
    Methods:
        run(input_dict): Execute the chain with given inputs
    """
    
    def __init__(self, llm, prompt):
        """
        Initialize the chain with an LLM and prompt template.
        
        Args:
            llm: Language model instance (e.g., NakliLLM)
            prompt: Prompt template instance (e.g., NakliPromptTemplate)
        """
        self.llm = llm
        self.prompt = prompt
    
    def run(self, input_dict):
        """
        Execute the chain with given input variables.
        
        Process:
        1. Format the prompt template with input variables
        2. Pass formatted prompt to LLM
        3. Extract and return the response
        
        Args:
            input_dict (dict): Dictionary of input variables for the prompt
            
        Returns:
            str: The LLM's response to the formatted prompt
        """
        # Step 1: Format the prompt template with input variables
        final_prompt = self.prompt.format(input_dict)
        
        # Step 2: Get prediction from the LLM
        result = self.llm.predict(final_prompt)
        
        # Step 3: Extract and return the response
        return result['response']
    

# Example usage demonstrating the chain
if __name__ == "__main__":
    # Initialize the mock LLM
    llm = NakliLLM()

    # Create a prompt template asking for country's capital and currency
    prompt = NakliPromptTemplate(
        template='What is the capital of {country}?, what is the country\'s {currency}?',
        input_variables=['country', 'currency']
    )
    
    # Create the chain
    chain = NakLiLLMChain(llm, prompt)
    
    # Execute the chain with example input
    result = chain.run(input_dict={'country': 'America', 'currency': 'dollars'})
    
    print(result)