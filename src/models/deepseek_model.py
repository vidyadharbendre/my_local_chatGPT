#!/Users/vidyadharbendre/miniforge3/envs/nndl_env/bin/python


"""
#! /usr/bin/env python3
"""

__all__ = [
    'DeepSeekModel'
]
__version__ = "1.0.0.0"
__author__ = "Vidyadhar Bendre"
__maintainers__ = [
    "Vidyadhar<vidyadhar.bendre@gmail.com>"
] 

import sys
import os
import requests

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.models.base_model import BaseModel 

class DeepSeekModel(BaseModel):
    def generate_text(self, prompt: str) -> str:
        """Call Ollama API and return response"""
        data = {"model": "deepseek-r1:8b", "prompt": prompt, "stream": False}

        try:
            response = requests.post(self.api_url, json=data)
            response.raise_for_status()
            return response.json().get("response", "No response from Ollama API.")
        except requests.exceptions.RequestException as e:
            return f"Error calling Ollama API: {e}"    
    
