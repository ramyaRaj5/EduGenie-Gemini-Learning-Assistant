import os, google.generativeai as genai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def get_learning_recommendations(topic: str):
    prompt = f"""Create a learning path for {topic} from beginner to advanced. 
    Include topics, timeline, and resources (videos, books, articles)."""
    response = model.generate_content(prompt)
    return response.text