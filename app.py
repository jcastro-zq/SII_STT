from flask import Flask, jsonify
from main import run

app = Flask(__name__)

@app.route("/consulta/<rut>")
def consulta(rut):
    try:
        data = run(rut)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
