from flask import Flask, request, jsonify
from consulta import Consulta

app = Flask(__name__)

@app.route('/consulta', methods=['GET'])
def consultar_rut():
    rut = request.args.get('rut')
    if not rut:
        return jsonify({'error': 'Falta el parámetro rut'}), 400

    consulta = Consulta(rut)

    if not consulta.validate():
        return jsonify({'error': 'RUT inválido'}), 400

    try:
        resultado = consulta.resultado()
        return resultado, 200, {'Content-Type': 'application/json; charset=utf-8'}
    except Exception as e:
        return jsonify({'error': str(e)}), 500
