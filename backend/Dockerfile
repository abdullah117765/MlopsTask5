# Use official Python image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file
COPY requirements.txt .

# Install dependencies
RUN pip3 install -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose port 5000 to the outside world
EXPOSE 5000

# Command to run the Flask server
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
