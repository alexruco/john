# example_usage_llama3.py

from john.interface import AIInterface

# Initialize the interface
ai_interface = AIInterface()

# Send a prompt to LLaMA 3
response = ai_interface.send_prompt('Hello, world!', 'llamma3')
print(response)
