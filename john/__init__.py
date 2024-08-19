# my_python_module/__init__.py

"""
John
================

A brief description of what your module does.

Submodules
----------
module
    Description of what the submodule does.
"""

__version__ = "0.1.0"

from .models import openai_model, llamma3_model


__all__ = [
    "send_prompt"
]
