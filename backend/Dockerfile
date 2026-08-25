FROM python:3.12-slim

WORKDIR /app

# Forzar actualización de librerías vulnerables en el entorno global
RUN pip install --no-cache-dir --upgrade pip "setuptools>=78.1.1" "msgpack>=1.2.1" wheel

COPY requirements.txt .
# --ignore-installed obliga a pip a sobreescribir cualquier paquete previo
RUN pip install --no-cache-dir --ignore-installed -r requirements.txt

COPY . .

EXPOSE 5050

CMD ["gunicorn", "--bind", "0.0.0.0:5050", "sample_app:sample"]