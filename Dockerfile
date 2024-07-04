# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the main Python script and Flask app into the container
COPY lsdk.py app.py ./

# Install the Lightning AI SDK and Flask
RUN pip install --no-cache-dir lightning-sdk flask

# Define the port as an environment variable
ENV PORT=8070

# Expose the port defined in the environment variable
EXPOSE $PORT

# Run the Flask app when the container launches
CMD ["python", "app.py"]
