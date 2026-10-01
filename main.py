from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import google.generativeai as genai
import os

# Un modules import pannrom
from qna import get_qna_answer
from explanation_module import get_explanation
from quiz_module import get_quiz
from summary_module import get_summary
from learning_path import get_learning_path

app = FastAPI()

# Gemini API Key setup
# Render la deploy panna env var la key vachikanum
genai.configure(api_key=os.getenv("GEMINI_API_KEY", "YOUR_API_KEY_HERE"))

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})

@app.post("/", response_class=HTMLResponse)
async def handle_task(request: Request, task: str = Form(...), user_input: str = Form(...)):
    result = ""
    
    if task == "qna":
        result = get_qna_answer(user_input)
    elif task == "explain":
        result = get_explanation(user_input)
    elif task == "quiz":
        result = get_quiz(user_input)
    elif task == "summary":
        result = get_summary(user_input)
    elif task == "learning_path":
        result = get_learning_path(user_input)
    
    return templates.TemplateResponse("index.html", {"request": request, "result": result})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)