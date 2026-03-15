# Use an official lightweight Python image as the base stage for building
FROM python:3.12-slim AS builder

# Set the working directory in the container
WORKDIR /app

# Install application dependencies first to leverage Docker's build cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port your app runs on (e.g., 5000 for Flask or 8000 for FastAPI)
EXPOSE 5000

# Define the command to run the application when the container starts
CMD ["python3", "app.py"]
