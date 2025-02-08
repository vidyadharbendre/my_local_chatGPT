#! /usr/bin/env python3
"""
"""

__all__ = [
    ''
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

import streamlit as st
from src.services.model_service import ModelService

# Streamlit UI
st.title("My Local Chatbot")

# Select Model
model_choice = st.selectbox("Choose Model:", ["Mistral", "DeepSeek"])

# Initialize Model
model_service = ModelService(model_type=model_choice.lower())

# Input Prompt
user_prompt = st.text_area("Enter your prompt:")

if st.button("Generate Text"):
    if user_prompt:
        response = model_service.generate_response(user_prompt)
        st.write(response)
    else:
        st.warning("Please enter a prompt!")
