# example_usage.py

from john.interface import AIInterface

# Initialize the interface; it automatically loads the organization ID, API keys, and project IDs from config.json
ai_interface = AIInterface()

# Define the OpenAI model you want to use
model_name = "gpt-3.5-turbo"

# Send a prompt to OpenAI and print the response
response = ai_interface.send_prompt('Hello, world!', 'openai', model_name)
print(response)
