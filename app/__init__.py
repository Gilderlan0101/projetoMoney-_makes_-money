import os
from flask import Flask
from .routes import main
from .utils import cache, config

def create_app():
    app = Flask(__name__)

    # Caminho absoluto para o arquivo config.py dentro do diretório .promodia (venv)
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../.promodia/config.py')
    
    # Carregando a configuração a partir do arquivo config.py
    app.config.from_pyfile(config_path)

    # Registra o blueprint
    app.register_blueprint(main)

    app.config.from_mapping(config)
    cache.init_app(app) 

    return app
