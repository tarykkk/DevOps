# Use official Python runtime as base image
FROM python:3.11-slim-bullseye

# Set maintainer label
LABEL maintainer="devops-student"
LABEL description="Notes application with PostgreSQL"

# Set working directory in container
WORKDIR /application

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc postgresql-client && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY src/ ./src/

# Create non-root user for security
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /application

USER appuser

# Expose application port
EXPOSE 5000

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=src/app.py

# Run application with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--timeout", "60", "src.app:app"]