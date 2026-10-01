import google.generativeai as genai, os
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def summarize_text(text):
    model = genai.GenerativeModel("gemini-1.5-pro")
    prompt = f"Summarize this educational passage concisely retaining key points:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text