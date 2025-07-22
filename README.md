# 📚 PDF AI Chatbot (Multilingual + Voice Support)

An AI-powered chatbot that lets you upload a PDF and ask questions about its content using text or speech — now supporting **English, Hindi, Marathi, and Arabic**. Built with **React**, **FastAPI**, and **Gemini AI**.

---

## ✨ Features

- 📄 Upload any PDF document
- 💬 Ask questions about the content via chat
- 🎤 Use voice input in your preferred language
- 🔊 AI responds with speech in the selected language
- 🌐 Multilingual support: **English**, **Hindi**, **Marathi**, **Arabic**
- 🧠 Powered by **Gemini 2.5 Flash** for context-aware reasoning

---

## 📁 Project Structure

pdf-ai-chatbot/
├── chatbot-backend/ # FastAPI server (Python)
└── my-chatbot/ # React frontend (JavaScript)

yaml
Copy
Edit

---

## 🚀 Getting Started (Local Setup)

### 🧱 Prerequisites

- Node.js (v18+ recommended)
- Python 3.10 or higher
- `pip` (Python package installer)
- Git

---

## 🛠️ Backend Setup (FastAPI)

### 1. Navigate to backend folder

```bash
cd chatbot-backend
```
2. Create and activate a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate
# On Windows: venv\Scripts\activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Set your Gemini API key
Edit main.py and replace the placeholder with your Gemini API key:
```bash
GEMINI_API_KEY = "your-api-key-here"
```
5. Run the FastAPI server
```bash
uvicorn main:app --reload
```
FastAPI will be running at: http://localhost:8000

💻 Frontend Setup (React)
1. Navigate to frontend folder
```bash
cd ../my-chatbot
```
2. Install Node modules
```bash
npm install
```
4. Start the development server
```bash
npm start
```
React app will open at: http://localhost:3000

🌐 Language & Voice Features

Select your language from the dropdown.

Use 🎤 to speak your question — the AI will recognize your voice in that language.

Use 🔊 to hear the AI's response in your selected language.

Gemini will answer in the same language based on PDF context.

🧪 Supported Languages

Language	Code	Supported in Speech

English	✅

Hindi	✅

Marathi ✅

Arabic ✅


📦 Dependencies

Backend:

FastAPI

PyMuPDF (fitz)

httpx

Uvicorn

Frontend:

React

Tailwind CSS

Web Speech API (browser native)


💡 Tips

Make sure your microphone is enabled in your browser settings.

PDFs should contain selectable text (not scanned images). OCR support can be added with Tesseract.

For production, update CORS and restrict API keys.


📃 License

MIT License

🧑‍💻 Author

Nihal Girish
github.com/nihalgirish
