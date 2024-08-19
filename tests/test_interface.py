# tests/test_interface.py

import pytest
from john.interface import AIInterface

def test_interface_initialization():
    interface = AIInterface()
    assert interface.config is not None

def test_add_model():
    interface = AIInterface()
    interface.add_model('openai', 'fake-api-key')
    assert interface.config.get_api_key('openai') == 'fake-api-key'

def test_send_prompt_to_openai(monkeypatch):
    def mock_openai_model(prompt, api_key, config):
        return {'response': 'mocked response'}

    from john.models import openai_model
    monkeypatch.setattr('john.models.openai_model', mock_openai_model)

    interface = AIInterface()
    interface.add_model('openai', 'fake-api-key')
    response = interface.send_prompt('Hello, world!', 'openai')
    assert response['response'] == 'mocked response'
