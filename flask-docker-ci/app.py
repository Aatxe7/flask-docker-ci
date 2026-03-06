from flask import Flask

app = Flask(__name__)

@app.get("/")
def hello():
    # Requisito: un mensaje de saludo al acceder a la raíz (/)
    return "Hola 👋. Entregable 4 funcionando (Flask + Docker + CI).", 200

# Para ejecución local sin Docker:
#   python app.py
if __name__ == "__main__":
    # Importante: 0.0.0.0 para que Docker pueda exponerlo hacia fuera
    app.run(host="0.0.0.0", port=5000, debug=True)
