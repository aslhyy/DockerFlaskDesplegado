from flask import Flask, render_template
from flask_cors import CORS

sample = Flask(__name__)
CORS(sample)

@sample.route("/")
def main():
    return render_template("index.html")

@sample.route("/api")
def api():
    return {
        "mensaje": "Backend funcionando correctamente"
    }

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5050, debug=True)
