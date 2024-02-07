# Start from a Python 3.12 image
FROM python:3.12

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    # graphviz \
    # graphviz-dev \
    curl

# Install Node.js
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs

# Install Python dependencies
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Install Node.js dependencies
# WORKDIR /usr/src/app
# COPY ./frontend/package*.json ./
# RUN npm install

# Add Django project code
ADD . /MasterEvent
WORKDIR /MasterEvent

# Expose port
EXPOSE 8000

# Run Django server
ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
