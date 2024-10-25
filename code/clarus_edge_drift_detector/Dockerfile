# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the requirements file into the image
COPY requirements.txt /app/

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the image
COPY . /app/
RUN mkdir -p reports 

# Expose the port the app runs on
EXPOSE 5001

# Run the application
CMD ["python", "run.py"]