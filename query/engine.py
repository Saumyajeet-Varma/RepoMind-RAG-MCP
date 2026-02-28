import os
import google.generativeai as genai
from config.settings import GEMINI_API_KEY, GEMINI_MODEL

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(GEMINI_MODEL)

def generate_answer(query, retrieved_chunk):
    
    context = "\n\n".join(
        [chunk["content"][:500] for chunk in retrieved_chunk]
    )

    prompt = f"""
        
        You are an expert software engineer.

        Use the following code context to answer the question.

        Code Context: {context}

        Query: {query}

        Explain clearly and mention file names if possible.

    """

    response = model.generate_content(prompt)

    return response.text