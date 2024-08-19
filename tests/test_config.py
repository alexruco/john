# john/config.py

import os

class Config:
    def __init__(self):
        self.api_keys = {}
        self.configs = {}

    def add_api_key(self, model_name, api_key):
        """Add an API key for a specific model."""
        self.api_keys[model_name] = api_key

    def get_api_key(self, model_name):
        """Retrieve the API key for a specific model."""
        return self.api_keys.get(model_name)

    def add_config(self, model_name, config):
        """Add configuration for a specific model."""
        self.configs[model_name] = config

    def get_config(self, model_name):
        """Retrieve the configuration for a specific model."""
        return self.configs.get(model_name)
