# Use the official Python image as base
FROM python:3.8.0

# Set the working directory inside the container
WORKDIR "D:\sampath"

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose port 5000 to the outside world
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=newflask.py

# Run the Flask application
CMD ["python","./newflask.py"]
