from flask import Flask, render_template
from flask_cors import CORS
import os

sample = Flask(__name__)
CORS(sample)

@sample.route("/")
def main():
    return render_template("index.html")

@sample.route("/api")
def api():
    return {"mensaje": "API ROTA"}, 500  # Código 500 para Pytest

# backend/sample_app.py
MYSQL_PASSWORD = "super_secret_123"  # Clave hardcodeada para Bandit

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5050, debug=True)  # debug=True para Bandit