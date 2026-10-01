# EduGenie: Google Gemini Powered Learning Assistant 🎓

> A lightweight AI-powered educational assistant that simplifies learning through generative AI.

## 📌 Project Description
EduGenie is designed for students of all academic levels. It enables users to:
- Ask questions and receive smart, concise answers
- Understand complex concepts through simplified explanations
- Generate quizzes from topics or text
- Receive personalized learning recommendations
- Summarize large educational passages

Built with **FastAPI** for the backend and simple **HTML + CSS** frontend, EduGenie leverages both lightweight local models and cloud-based AI models. Works well on devices like Mac M1, making it accessible for all learners.

## ✨ Key Features & Modules

### 1. Explanation Module
Uses **LaMini-Flan-T5-783M** (lightweight, CPU-compatible) to break down complex topics into easily understandable language for beginners.

### 2. QnA Module
Powered by **Gemini 1.5 Pro** for accurate, context-aware academic question-answering across diverse subjects.

### 3. Quiz Module
Generates 3 MCQs from any passage, each with 4 options. Output is structured in JSON format with auto-correction if answered wrong.

### 4. Summary Module
Leverages Gemini to summarize long paragraphs into concise versions for quick revision while retaining core information.

### 5. Learning Path Module
`get_learning_recommendations` function generates a structured, beginner-to-advanced learning path with timelines and resources (videos, articles, books).

## 🏗️ Architecture
- **AI Models:** Gemini 1.5 Pro (Cloud) for Q&A, Quiz, Summary, Learning Path | LaMini-Flan-T5-783M (Local) for Explanation
- **Backend:** FastAPI - RESTful Endpoints
- **Frontend:** HTML, CSS, Jinja2 Templating
- **Server:** Uvicorn (ASGI Server)

### API Endpoints
- `/qa` - Question Answering
- `/explain` - Concept Explanation
- `/quiz` - Quiz Generation
- `/summarize` - Text Summarization
- `/learn/recommendations` - Personalized Learning Path

## 🛠️ Tech Stack
- Python 3.10+
- FastAPI Framework
- Google Gemini API (Gemini 1.5 Pro)
- LaMini-Flan-T5-783M
- HTML & CSS
- Uvicorn
- Jinja2

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.10+
- Google Gemini API Key from [Google AI Studio](https://aistudio.google.com/)

### Steps
1. Clone the repo:
   ```bash
   git clone https://github.com/YOUR_USERNAME/EduGenie-Gemini-Learning-Assistant.git
   cd EduGenie-Gemini-Learning-Assistant
