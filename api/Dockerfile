# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory.
WORKDIR /ci-cd

# Copy requirements and install dependencies
COPY ../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code into the container
COPY ./api /ci-cd/api
COPY .flake8 /ci-cd/.flake8

# Expose the port
EXPOSE 8000

# Run the FastAPI application
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]