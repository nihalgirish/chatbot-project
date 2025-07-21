# Step 1: Use the official Python 3.9 slim image as the base image
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the current directory (where the Dockerfile is located) into the /app directory in the container
COPY . /app

# Step 4: Install system dependencies (like libmupdf-dev and build-essential) to compile packages
RUN apt-get update && apt-get install -y build-essential libmupdf-dev

# Step 5: Install Python dependencies from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Expose port 80 (default HTTP port) for the app
EXPOSE 80

# Step 7: Define the command to run the FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
