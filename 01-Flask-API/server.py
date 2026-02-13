from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Servidor API Activo. Sistema de comunicacion funcionando."

@app.route('/status')
def get_status():
    # Simulamos datos de estado
    return jsonify({
        "status": "online",
        "buffer": "24MB",
        "mensaje": "Conexion exitosa con el servidor"
    })

if __name__ == '__main__':
    # Escucha en todas las IPs en el puerto 5000
    app.run(host='0.0.0.0', port=5000)
