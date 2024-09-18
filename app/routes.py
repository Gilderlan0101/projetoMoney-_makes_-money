from flask import render_template, Blueprint, request, current_app
import requests
import random
from .utils import cache, config

main = Blueprint('main', __name__)

# Lista de termos de pesquisa aleatórios
RANDOM_TERMS = ['smartphone', 'televisão', 'tablet', 'fones de ouvido', 'mouse', 'teclado', 'relógio', 'bicicleta', 'câmera', 'cadeira']

def fetch_mercado_livre_products(query):
    """Busca produtos na API do Mercado Livre com base em um termo de pesquisa"""
    ML_API_URL = current_app.config['ML_API_URL']  # Obtém a URL da API das configurações
    try:
        response = requests.get(ML_API_URL, params={'q': query})
        response.raise_for_status()  # Verifica se houve erro na requisição
        data = response.json()  # Tenta decodificar a resposta como JSON
        
        # Adiciona logging para depuração
        print("Response Status Code:", response.status_code)
        print("Response Data:", data)

        # Mapeia os dados do Mercado Livre para a estrutura esperada no template
        products = []
        for item in data.get('results', []):
            product = {
                'title': item.get('title'),
                'thumbnail': item.get('thumbnail', '/path/to/default-image.jpg'),
                'original_price': item.get('price'),
                'promo_price': item.get('price'),  # Se não houver preço promocional separado, use o mesmo preço
                'company': 'Mercado Livre',
                'url': item.get('permalink')  # Link para o produto no Mercado Livre
            }
            products.append(product)
        
        return products
    
    except requests.exceptions.RequestException as e:
        print("Request Exception:", e)
        return []


@main.route('/')
def home():
    # Se nenhum termo for passado na URL, escolhe um termo aleatório da lista
    query = request.args.get('query', random.choice(RANDOM_TERMS))

    # Solicita os dados da API do Mercado Livre
    mercado_livre_products = fetch_mercado_livre_products(query)

    # Se não houver produtos do Mercado Livre, exibe uma mensagem de erro ou retorna uma lista vazia
    if not mercado_livre_products:
        return "Nenhum produto encontrado no Mercado Livre."

    return render_template('index.html', products=mercado_livre_products)

@main.route('/mercado_livre')
@cache.cached(timeout=50)
def mercado():
    query = request.args.get('query', random.choice(RANDOM_TERMS))

    # Solicita os dados da API do Mercado Livre
    mercado_livre_products = fetch_mercado_livre_products(query)

    if not mercado_livre_products:
        return "Nenhum produto encontrado no Mercado Livre."
    return render_template('mercado_livre.html',  products=mercado_livre_products)
