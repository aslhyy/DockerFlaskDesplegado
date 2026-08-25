# Cambiar de python:3.8-slim-buster a python:3.12-slim
FROM python:3.12-slim

WORKDIR /app

# Copiar e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5050

CMD ["gunicorn", "--bind", "0.0.0.0:5050", "sample_app:sample"]