import os
from flask import Flask
from .routes import main

def create_app():
    app = Flask(__name__)
    
    # Corrigindo o caminho para o config.py dentro do venv
    app.config.from_pyfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../.promodia/config.py'))

    # Registra o blueprint
    app.register_blueprint(main)

    return app
