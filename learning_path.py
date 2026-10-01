import google.generativeai as genai, os
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_learning_recommendations(topic):
    model = genai.GenerativeModel("gemini-1.5-pro")
    prompt = f"Create a structured learning path for '{topic}' from beginner to advanced with timelines and resources like videos, articles, books."
    response = model.generate_content(prompt)
    return response.text