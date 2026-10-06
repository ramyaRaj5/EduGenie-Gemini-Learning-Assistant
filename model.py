import os, google.generativeai as genai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def explain_topic(topic: str):
    prompt = f"Explain {topic} in simple words for beginners, easy to understand, with example."
    response = model.generate_content(prompt)
    return response.text