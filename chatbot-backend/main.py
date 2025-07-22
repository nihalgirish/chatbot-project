from fastapi import FastAPI, File, UploadFile, Request
from fastapi.middleware.cors import CORSMiddleware
import fitz  # PyMuPDF
import tempfile
import httpx
import re

app = FastAPI()

# Enable frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set your Gemini API key here
GEMINI_API_KEY = "AIzaSyCPgZTkDG0JcloEOE5g7By5VSWUk48Tzvs"

def clean_markdown(text):
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)  # Bold
    text = re.sub(r'\*(.*?)\*', r'\1', text)      # Italics
    return text

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        contents = await file.read()
        tmp.write(contents)
        tmp_path = tmp.name

    try:
        doc = fitz.open(tmp_path)
        full_text = ""
        for page in doc:
            full_text += page.get_text()
        doc.close()
    except Exception as e:
        return {"error": str(e)}

    return {
        "filename": file.filename,
        "length": len(full_text),
        "text_preview": "",
        "full_text": full_text
    }

@app.post("/ask/")
async def ask_ai(request: Request):
    data = await request.json()
    question = data.get("question")
    context = data.get("context")
    language_code = data.get("language", "en-US")

    # Mapping of language codes to language names (for prompt clarity)
    language_names = {
        "en-US": "English",
        "hi-IN": "Hindi",
        "mr-IN": "Marathi",
        "ar-SA": "Arabic"
    }

    user_language = language_names.get(language_code, "English")

    prompt = f"""
You are an educational assistant. The user will ask a question in {user_language}.
Please respond in {user_language} based strictly on the content of the following document.

Document:
\"\"\"
{context}
\"\"\"

Question:
{question}
"""

    headers = {
        "Content-Type": "application/json"
    }

    body = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        async with httpx.AsyncClient() as client:
            res = await client.post(
                "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent",
                headers=headers,
                params={"key": GEMINI_API_KEY},
                json=body
            )
        
        print(f"Status Code: {res.status_code}")
        print(f"Response Text: {res.text}")

        response_json = res.json()
        print(f"Parsed JSON: {response_json}")

        if "candidates" in response_json:
            text = response_json["candidates"][0]["content"]["parts"][0]["text"]
            return {"answer": text}
        else:
            return {"error": "Gemini API response is missing 'candidates'. Check response format."}

    except Exception as e:
        return {"error": f"Could not get a valid answer from Gemini. {str(e)}"}
