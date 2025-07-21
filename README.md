# PDF AI Chatbot

This project allows users to upload a PDF document and interact with an AI-powered chatbot. The backend is built with **FastAPI**, and the frontend is built with **React**. Users can ask questions based on the contents of the uploaded PDF.

## Table of Contents
- [Installation](#installation)
- [Backend Setup](#backend-setup)
- [Frontend Setup](#frontend-setup)
- [Running the App](#running-the-app)
- [How It Works](#how-it-works)
- [License](#license)

## Installation

1. **Clone the Repository**:

   Start by cloning the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/pdf-ai-chatbot.git
Navigate into the Project Directory:

bash
Copy
cd pdf-ai-chatbot
Backend Setup (FastAPI)
1. Set up the Python environment
Navigate to the chatbot-backend directory:

bash
Copy
cd chatbot-backend
Create a Python virtual environment:

bash
Copy
python3 -m venv venv
Activate the virtual environment:

On macOS/Linux:

bash
Copy
source venv/bin/activate
On Windows:

bash
Copy
venv\Scripts\activate
2. Install the required dependencies
With the virtual environment active, run the following command to install the necessary dependencies:

bash
Copy
pip install -r requirements.txt
3. Run the FastAPI backend
Start the backend by running:

bash
Copy
uvicorn main:app --reload --host 0.0.0.0 --port 8000
The backend will now be running at http://localhost:8000.

Frontend Setup (React)
1. Set up the frontend environment
Navigate to the my-chatbot directory:

bash
Copy
cd ../my-chatbot
Install the required dependencies:

bash
Copy
npm install
2. Run the React frontend
Start the frontend by running:

bash
Copy
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
