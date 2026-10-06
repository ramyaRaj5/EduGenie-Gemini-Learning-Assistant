import os, google.generativeai as genai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def summarize_text(text: str):
    prompt = f"Summarize this paragraph in short, keeping main points: {text}"
    response = model.generate_content(prompt)
    return response.text