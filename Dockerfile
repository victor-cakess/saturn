# Use an official Python runtime
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your code
COPY . .

# Expose port
EXPOSE 8501

# Default command 
CMD ["python", "app.py"]
