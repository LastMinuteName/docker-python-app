# Use an official Python runtime as a parent image
FROM python:3.9.18-slim-bullseye

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Run app.py when the container launches 
CMD ["python", "app.py"]