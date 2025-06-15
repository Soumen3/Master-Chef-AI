# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Set working directory in the container
WORKDIR /app

# Install production dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project code into the container
COPY . .

# Collect static files (if using GCS, this will push them to GCS)
RUN python manage.py collectstatic --noinput

# Expose the port (Cloud Run expects applications to listen on the PORT env var)
ENV PORT 8080
EXPOSE $PORT

# Run Gunicorn
CMD exec gunicorn myproject.wsgi:application --bind :$PORT --workers 2 --threads 4 --timeout 60
# Replace 'myproject' with your actual project name