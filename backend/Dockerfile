FROM python:3.12-slim

WORKDIR /app

# Forzar actualización de librerías vulnerables en el entorno global
RUN pip install --no-cache-dir --upgrade pip "setuptools>=78.1.1" "msgpack>=1.2.1" wheel

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && rm -rf /usr/local/lib/python3.12/site-packages/pip \
              /usr/local/lib/python3.12/site-packages/pip-*.dist-info \
              /usr/local/bin/pip \
              /usr/local/bin/pip3 \
              /usr/local/bin/pip3.12

COPY . .

EXPOSE 5050

CMD ["gunicorn", "--bind", "0.0.0.0:5050", "sample_app:sample"]