import google.generativeai as genai
import os
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def explain_concept(topic):
    model = genai.GenerativeModel("gemini-1.5-pro")
    prompt = f"Explain the concept '{topic}' in very simple, easy to understand language for beginners. Use examples."
    response = model.generate_content(prompt)
    return response.text