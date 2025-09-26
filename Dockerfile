FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY Functions/ Functions/

EXPOSE 8888

CMD ["python", "app.py"]