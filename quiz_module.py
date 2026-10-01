import google.generativeai as genai, os, json, re
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def clean_json_block(text):
    text = re.sub(r'```json|```', '', text).strip()
    return text

def generate_quiz(topic):
    model = genai.GenerativeModel("gemini-1.5-pro")
    prompt = f"""Generate 3 MCQs from topic '{topic}'. Each with 4 options and correct answer.
    Return ONLY valid JSON like: [{{"question":"...","options":["A","B","C","D"],"answer":"A"}}]"""
    response = model.generate_content(prompt)
    try:
        cleaned = clean_json_block(response.text)
        data = json.loads(cleaned)
        # format nicely
        out = ""
        for i,q in enumerate(data,1):
            out+= f"Q{i}: {q['question']}\nOptions: {', '.join(q['options'])}\nAnswer: {q['answer']}\n\n"
        return out
    except Exception as e:
        return response.text