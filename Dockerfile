# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python dependency files into the container
COPY Pipfile Pipfile.lock /app/

# Install dependencies using Pipenv
RUN pip install pipenv && pipenv install --deploy --system

# Copy the Flask app code and static assets into the container
COPY app.py .
COPY templates templates

# Expose the port the Flask app runs on
EXPOSE 5000

# Define the command to run the Flask application
CMD ["python", "app.py"]
