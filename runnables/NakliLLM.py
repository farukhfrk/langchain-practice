"""
Custom Mock LLM and Prompt Template Implementation

This module provides simplified, mock implementations of LangChain components
for educational purposes. These can be used as templates for understanding
how LangChain works internally.

Classes:
    NakliLLM: A mock language model that returns predefined responses
    NakliPromptTemplate: A simplified prompt template implementation

Note: "Nakli" means "fake" or "mock" in Hindi.
This is intentionally a simplified implementation for learning purposes.
"""

import random


class NakliLLM:
    """
    A mock Language Model that simulates LLM behavior.
    
    Instead of making actual API calls, it returns randomly selected
    responses from a predefined list. Useful for testing chains without
    incurring API costs.
    
    Attributes:
        None
        
    Methods:
        predict(prompt): Returns a random response wrapped in a dict
    """
    
    def __init__(self):
        """Initialize the mock LLM."""
        print('LLM Created')

    def predict(self, prompt):
        """
        Generate a mock prediction based on input prompt.
        
        Args:
            prompt (str): The input prompt (not actually used in the mock)
            
        Returns:
            dict: A dictionary with 'response' key containing the output
        """
        # Predefined responses
        response_list = [
            'Delhi is the capital of India.',
            'IPL is the most popular cricket league in the world.',
            'Python is a popular programming language.'
        ]
        
        # Return a random response
        return {'response': random.choice(response_list)}


class NakliPromptTemplate:
    """
    A simplified prompt template that formats text with variables.
    
    This demonstrates the core functionality of PromptTemplate:
    storing a template string and filling in variables.
    
    Attributes:
        template (str): The template string with placeholders like {variable}
        input_variables (list): List of variable names to be filled
        
    Methods:
        format(input_dict): Fill template variables with provided values
    """
    
    def __init__(self, template, input_variables):
        """
        Initialize the prompt template.
        
        Args:
            template (str): Template string with {variable} placeholders
            input_variables (list): List of variable names in the template
        """
        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict):
        """
        Format the template by replacing variables with values.
        
        Args:
            input_dict (dict): Dictionary mapping variable names to values
            
        Returns:
            str: The formatted template string with variables replaced
        """
        return self.template.format(**input_dict)