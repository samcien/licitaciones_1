from flask import Flask
from app.routes import api_bp

app = Flask(__name__)

# Registrar las rutas de la API
app.register_blueprint(api_bp, url_prefix='/api')

# Ruta para la página de inicio
@app.route('/')
def home():
    return "Bienvenido a la aplicación de Licitaciones"

if __name__ == '__main__':
    app.run(debug=True)
