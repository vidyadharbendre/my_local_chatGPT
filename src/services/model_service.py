#! /usr/bin/env python3
"""
"""

__all__ = [
    'ModelService'
]
__version__ = "1.0.0.0"
__author__ = "Vidyadhar Bendre"
__maintainers__ = [
    "Vidyadhar<vidyadhar.bendre@gmail.com>",
]

import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
#sys.path.insert(0, os.getcwd())

from src.models.mistral_model import MistralModel
from src.models.deepseek_model import DeepSeekModel

class ModelService:
    """Handles AI Model Selection"""

    def __init__(self, model_type="mistral"):
        if model_type.lower() == "mistral":
            self.model = MistralModel()
        elif model_type.lower() == "deepseek":
            self.model = DeepSeekModel()
        else:
            raise ValueError("Unsupported model type. Choose 'mistral' or 'deepseek'.")

    def generate_response(self, prompt: str) -> str:
        return self.model.generate_text(prompt)

