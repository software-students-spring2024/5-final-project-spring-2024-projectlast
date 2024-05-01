# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependency files (Pipfile and Pipfile.lock) into the container
COPY Pipfile Pipfile.lock /app/

# Install dependencies using Pipenv
RUN pip install pipenv && \
    pipenv install --deploy --system

# Copy the rest of the application code into the container
COPY . /app/

# Expose port 5000 for Flask application
EXPOSE 5000

# Define the command to run your Flask application
CMD ["python", "app.py"]
