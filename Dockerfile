# Use the python3.7.2 container image
FROM python:3

ENV PYTHONUNBUFFERED 1

#set the working directory to app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install the Dependencies
RUN pip install -r requirements.txt


