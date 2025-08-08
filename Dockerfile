FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

ENV PYTHONPATH=/venv

EXPOSE 5000

CMD ["python", "-m", "src.app"]
