FROM python:3.12-slim

WORKDIR /app

# Actualiza las herramientas de empaquetado a versiones seguras y limpia la caché
RUN pip install --no-cache-dir --upgrade pip "setuptools>=78.1.1" "msgpack>=1.2.1" wheel

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5050

CMD ["gunicorn", "--bind", "0.0.0.0:5050", "sample_app:sample"]