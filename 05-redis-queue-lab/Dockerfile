FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY queue_lab ./queue_lab
CMD ["uvicorn", "queue_lab.main:app", "--host", "0.0.0.0", "--port", "8000"]
