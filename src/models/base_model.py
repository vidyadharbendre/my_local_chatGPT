#! /usr/bin/env python3
"""
"""

__all__ = [
    'BaseModel'
]
__version__ = "1.0.0.0"
__author__ = "Vidyadhar Bendre"
__maintainers__ = [
    "Vidyadhar<vidyadhar.bendre@gmail.com>",
]

from abc import ABC, abstractmethod


class BaseModel(ABC):
    """Abstract base class for all models."""
    def __init__(self):
        """Initialize API URL"""
        self.api_url = "http://localhost:11434/api/generate"  # Adjust if hosted remotely

    @abstractmethod
    def generate_text(self, prompt: str) -> str:
        """Generate text given a prompt."""
        pass