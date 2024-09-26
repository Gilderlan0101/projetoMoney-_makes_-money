from flask import Flask
from .routes import main
from .utils import cache
import os
from dotenv import load_dotenv
load_dotenv()

def create_app():
    app = Flask(__name__)

    # Carregando o cache e as variáveis de ambiente
    
    app.config['DEBUG'] = os.getenv('DEBUG')
    app.secret_key = os.getenv('KEY')

    # Registra o blueprint
    app.register_blueprint(main)

    # Inicializa o cache
    cache.init_app(app) 

  
    

    # Função add_cache_headers(response): Esta função verifica o tipo de conteúdo da resposta e, se for uma imagem, adiciona
    # um cabeçalho de cache para armazenar a imagem no cache do navegador por 3 dias (max-age=259200).
    # Isso pode ajudar a melhorar o desempenho ao evitar que o navegador baixe a imagem novamente em futuras requisições.


    return app
