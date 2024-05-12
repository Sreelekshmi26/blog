
FROM python:3.10.12-alpine

# Set unbuffered output for python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create app directory
WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

# Expose port
EXPOSE 8000

RUN chmod +x scripts/django.sh
# RUN chmod +x scripts/worker-entrypoint.sh

