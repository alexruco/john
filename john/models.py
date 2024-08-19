# john/models.py

from openai import OpenAI
import requests

def openai_model(prompt, organization_id, api_key, model, config=None):
    """Interact with OpenAI's API using the updated Python client."""
    
    # Initialize the OpenAI client
    client = OpenAI(api_key=api_key)
    
    # Send the request to the OpenAI API
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        **(config or {})
    )

    # Extract and return the message content from the response
    return response.choices[0].message.content

def other_model(prompt, api_key, config=None):
    """Interact with another AI model."""
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    data = {
        'input': prompt,
    }

    if config:
        data.update(config)

    response = requests.post('https://api.othermodel.com/v1/generate', headers=headers, json=data)

    if response.status_code != 200:
        raise Exception(f"Other Model API request failed with status code {response.status_code}: {response.text}")

    return response.json()