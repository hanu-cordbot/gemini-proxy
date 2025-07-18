FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY main.py .
ENV PORT=8080
CMD ["gunicorn", "-b", "0.0.0.0:8080", "main:app"]
