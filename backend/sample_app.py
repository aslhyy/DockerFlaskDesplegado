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
    return {"mensaje": "API funcionando correctamente"}

if __name__ == "__main__":
    debug_mode = os.getenv("FLASK_DEBUG", "false").lower() in ("true", "1", "t")
    host_ip = os.getenv("FLASK_HOST", "127.0.0.1")
    port_num = int(os.getenv("FLASK_PORT", 5050))

    sample.run(host=host_ip, port=port_num, debug=debug_mode) # nosec