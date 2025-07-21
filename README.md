# PDF AI Chatbot

This project allows users to upload a PDF document and interact with an AI-powered chatbot. The backend is built with **FastAPI**, and the frontend is built with **React**. Users can ask questions based on the contents of the uploaded PDF.
Table of Contents
Installation

Backend Setup

Frontend Setup

Running the App

How It Works

License

Installation
bash
1. **Clone the Repository**:

   Start by cloning the repository to your local machine:

   git clone https://github.com/yourusername/pdf-ai-chatbot.git
bash
Navigate into the Project Directory:

cd pdf-ai-chatbot
Backend Setup (FastAPI)
bash
1. Set up the Python environment
Navigate to the chatbot-backend directory:

cd chatbot-backend
bash
Create a Python virtual environment:

python3 -m venv venv
bash
Activate the virtual environment:

On macOS/Linux:

source venv/bin/activate
bash
On Windows:

venv\Scripts\activate
bash
2. Install the required dependencies
With the virtual environment active, run the following command to install the necessary dependencies:

pip install -r requirements.txt
bash
3. Run the FastAPI backend
Start the backend by running:

uvicorn main:app --reload --host 0.0.0.0 --port 8000
The backend will now be running at http://localhost:8000.

Frontend Setup (React)
bash
1. Set up the frontend environment
Navigate to the my-chatbot directory:

cd ../my-chatbot
bash
Install the required dependencies:

npm install
bash
2. Run the React frontend
Start the frontend by running:

npm run dev
The frontend will be available at http://localhost:5173.

Running the App
Start the backend (FastAPI) by following the Backend Setup section.

Start the frontend (React) by following the Frontend Setup section.

Once both are running, open http://localhost:5173 in your browser to interact with the PDF AI chatbot. You can upload a PDF file and ask questions based on its content.

How It Works
Upload a PDF: The frontend allows you to upload a PDF document.

Backend Processing: The FastAPI backend processes the PDF and extracts the text using PDF parsing libraries (like PyMuPDF or pdfplumber).

AI Interaction: The extracted text is sent to an AI model (or any reasoning model like OpenAI, etc.) to provide meaningful answers to user questions.

License
This project is licensed under the MIT License - see the LICENSE file for details.


