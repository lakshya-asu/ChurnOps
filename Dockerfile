FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port on which the app will run
EXPOSE 5000

# Use Gunicorn as the production server for Flask
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "src.app:app"]
