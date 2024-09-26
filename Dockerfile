# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app1

# Copy the current directory contents into the container at /app
COPY . /app1

# Install any necessary dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on (Flask default is 5000)
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=hello.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the application
CMD ["flask", "run"]