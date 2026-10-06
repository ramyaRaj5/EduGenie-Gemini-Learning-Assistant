import os, json, re, google.generativeai as genai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def clean_json_block(text):
    text = re.sub(r'```json|```', '', text).strip()
    return text

def generate_quiz(topic: str):
    prompt = f"""Generate 3 MCQs about {topic}. 
    Return ONLY valid JSON array like:
    [{{"question": "...", "options": ["A","B","C","D"], "answer": "A"}}]"""
    response = model.generate_content(prompt)
    cleaned = clean_json_block(response.text)
    return json.loads(cleaned)