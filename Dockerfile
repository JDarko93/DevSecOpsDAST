FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ .

# Create directory for database
RUN mkdir -p /app/data

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]