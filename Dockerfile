# Use an official Python 3.8 slim image based on Debian Buster
FROM python:3.8-slim-buster


# Update the package lists and install the AWS CLI
RUN apt update -y && apt install awscli -y


# Set the working directory inside the container to /app
WORKDIR /app

# Copy the local contents into the container at /app
COPY . /app

# Install Python dependencies listed in requirements.txt
RUN pip install -r requirements.txt

RUN pip install --upgrade accelerate
RUN pip uninstall -y transformers accelerate
RUN pip install transformers accelerate

# Specify the default command to run when the container starts
CMD ["python3", "app.py"]