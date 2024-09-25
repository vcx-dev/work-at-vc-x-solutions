# Use Python official image as a base
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y libpq-dev gcc

# Install Python dependencies from requirements.txt
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files to container
COPY . /app/

# Expose port 8000
EXPOSE 8000

# Command to run Django's development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]