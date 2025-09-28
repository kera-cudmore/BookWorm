# Use a Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code
COPY . .

# Expose the default port for Dokploy/Traefik
# Dokploy will manage the external port, but the container must listen on a port.
# The default port for Dokploy is 3000, but 8000 is common for Gunicorn.
EXPOSE 8000

# Command to run the application using Gunicorn (production WSGI server)
# 'app:app' assumes your main file is 'app.py' and your Flask instance is named 'app'.
# '-b 0.0.0.0:8000' binds Gunicorn to all interfaces on port 8000.
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"] 