# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables to prevent Python from writing .pyc files and to force stdout and stderr to be unbuffered.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Update and install dependencies.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy project to the container.
COPY ./backend /app/

# Upgrade pip and install python dependencies from requirements.txt.
COPY ../requirements.txt /app/
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

# Run server on port 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
