# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the main Python script into the container
COPY lsdk.py .

# Install the Lightning AI SDK
RUN pip install --no-cache-dir lightning-sdk

# Run the script when the container launches
CMD ["python", "lsdk.py"]
