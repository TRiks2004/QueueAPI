# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory to /code
WORKDIR /code

# Update package lists and install required packages
RUN apt-get update && apt-get install -y python3-dev

# Upgrade pip and install pipenv
RUN pip install --upgrade pip && pip install poetry

# Copy pyproject.toml separately to leverage Docker cache
COPY pyproject.toml .

# Configure Poetry to not create a virtualenv (we're using the system Python)
RUN poetry config virtualenvs.create false

# Install dependencies (do not install root package)
RUN poetry install --no-root --no-interaction --no-ansi

# Expose port 8000
EXPOSE 8000

# Copy the entire project into the container
COPY . .
