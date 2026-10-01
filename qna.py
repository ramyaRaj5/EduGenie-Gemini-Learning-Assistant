import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_answer(question):
    model = genai.GenerativeModel("gemini-1.5-pro")
    prompt = f"Answer this educational question concisely: {question}"
    response = model.generate_content(prompt)
    return response.text