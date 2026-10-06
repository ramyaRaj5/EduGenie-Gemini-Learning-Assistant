from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

# MANUAL AH KEY EDUKKUREN DA - 100% WORK AAGUM DA!
GOOGLE_KEY = None
try:
    with open(".env", "r", encoding="utf-8") as f:
        for line in f:
            if "GOOGLE_API_KEY" in line and "=" in line:
                GOOGLE_KEY = line.split("=", 1)[1].strip().replace('"','').replace("'","")
                break
    print(f"KEY FOUND DA: {GOOGLE_KEY[:15]}...")
except Exception as e:
    print(f".env padikka mudila da: {e}")

try:
    from google import genai
    if GOOGLE_KEY:
        client = genai.Client(api_key=GOOGLE_KEY)
        MODEL_ID = "gemini-3.8-flash"
    else:
        client = None
        MODEL_ID = None
except Exception as e:
    print(f"GenAI error da: {e}")
    client = None
    MODEL_ID = None

def ask_gemini(prompt):
    if not client:
        return f"Key error da, key: {GOOGLE_KEY}"
    try:
        resp = client.models.generate_content(model=MODEL_ID, contents=prompt)
        return resp.text
    except Exception as e:
        return f"Gemini Error da: {e} | Key start: {GOOGLE_KEY[:10]}"

@app.get("/", response_class=HTMLResponse)
def home():
    return """<html><body style="text-align:center;padding:20px;font-family:Arial;background:#e8f5e9">
<div style="background:white;max-width:600px;margin:auto;padding:20px;border-radius:15px">
<h1>EduGenie 🎓</h1><p>Internal Error sari aayiduchu da!</p>
<select id="task"><option value="qa">Ask Question</option><option value="explain">Explain</option><option value="summarize">Summarize</option><option value="quiz">Quiz</option><option value="learn">Learning Path</option></select><br>
<textarea id="input" rows="4" style="width:90%;padding:10px;margin:10px" placeholder="Photosynthesis..."></textarea><br>
<button onclick="doTask()" style="padding:10px 20px;background:#1976d2;color:white;border:none;border-radius:8px">✨ Generate pannu da!</button>
<div id="result" style="background:#f1f8e9;padding:15px;margin-top:15px;border-radius:10px;text-align:left;white-space:pre-wrap">Result inga varum da...</div>
</div><script>async function doTask(){let task=document.getElementById('task').value;let text=document.getElementById('input').value;if(!text){alert('Type pannu da!');return;}document.getElementById('result').innerText='Loading da... ⏳';let form=new FormData();if(task=='qa')form.append('question',text);else if(task=='explain')form.append('topic',text);else if(task=='summarize')form.append('content',text);else if(task=='quiz')form.append('topic',text);else if(task=='learn')form.append('topic',text);let url=task=='learn'?'/learn/recommendations':'/'+task;let res=await fetch(url,{method:'POST',body:form});let data=await res.json();document.getElementById('result').innerText=data.result;}</script></body></html>"""

@app.post("/qa")
def qa(question: str = Form(...)): return {"result": ask_gemini(f"Answer clearly: {question}")}
@app.post("/explain")
def explain(topic: str = Form(...)): return {"result": ask_gemini(f"Explain simply for beginner: {topic}")}
@app.post("/summarize")
def summarize(content: str = Form(...)): return {"result": ask_gemini(f"Summarize: {content}")}
@app.post("/quiz")
def quiz(topic: str = Form(...)): return {"result": ask_gemini(f"Generate 3 MCQs for {topic} with answers")}
@app.post("/learn/recommendations")
def learn(topic: str = Form(...)): return {"result": ask_gemini(f"Give learning path for {topic}")}
