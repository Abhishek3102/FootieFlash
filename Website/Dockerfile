# Use an official Python runtime as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt to the working directory
COPY Flask/requirements.txt /app/

# Install any necessary dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the application code into the container
COPY Flask /app/

# Expose the port the app runs on
EXPOSE 80
# Set environment variable to make sure Flask runs in production mode
ENV FLASK_ENV=production

# Set the default command to run your Flask app
CMD ["python", "main.py"]
