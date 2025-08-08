FROM python:3.13-slim

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire 'app' folder content into /app in container
COPY app/ .

# Set PYTHONPATH so Python finds your modules (important for imports like 'from src.utils...')
ENV PYTHONPATH=/venv

# Expose port 5000 to host
EXPOSE 5000

# Run the Flask app, listening on 0.0.0.0 so container accepts external connections
CMD ["python", "-m", "src.app"]

