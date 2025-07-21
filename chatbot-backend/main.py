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

# Optional: remove Markdown-style formatting
def clean_markdown(text):
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)  # Bold
    text = re.sub(r'\*(.*?)\*', r'\1', text)      # Italics
    text = re.sub(r'`(.*?)`', r'\1', text)        # Inline code
    text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)  # Links
    return text

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    # Save uploaded PDF to temp file
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
        "text_preview": "",     # Removed preview as requested
        "full_text": full_text  # Sent to frontend for question context
    }

@app.post("/ask/")
async def ask_ai(request: Request):
    data = await request.json()
    question = data.get("question")
    context = data.get("context")

    prompt = f"""
You are an educational assistant. Based on the following document, answer the user's question as clearly as possible.

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
        
        # Log the status code and response text
        print(f"Status Code: {res.status_code}")
        print(f"Response Text: {res.text}")

        # Try to parse the response
        response_json = res.json()
        print(f"Parsed JSON: {response_json}")

        # Check if 'candidates' exists in the response
        if "candidates" in response_json:
            text = response_json["candidates"][0]["content"]["parts"][0]["text"]
            return {"answer": text}
        else:
            return {"error": "Gemini API response is missing 'candidates'. Check response format."}

    except Exception as e:
        return {"error": f"Could not get a valid answer from Gemini. {str(e)}"}
