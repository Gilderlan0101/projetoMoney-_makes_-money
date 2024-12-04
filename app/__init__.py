from flask import Flask
from .routes.routes import main
from .utils import cache
import os
from dotenv import load_dotenv
# Carregando o cache e as variáveis de ambiente
load_dotenv()

def create_app():
    app = Flask(__name__)    
    app.config['DEBUG'] = True
    app.secret_key = os.getenv('KEY')
    
    # Registra o blueprint
    app.register_blueprint(main)

    # Inicializa o cache
    cache.init_app(app) 

  


    return app
