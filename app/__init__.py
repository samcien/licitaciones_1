from flask import Flask
from .routes import api_bp  # Importa el Blueprint desde routes.py

def create_app():
    app = Flask(__name__)

    # Registrar el Blueprint de las rutas
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
