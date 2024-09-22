import requests
from flask import Blueprint, render_template, request
import random
import os
from dotenv import load_dotenv
from app.services.scraping_amazon import scrape_products
from app.services.scraping_zoom import scraping_zoom


# Carregar variáveis de ambiente
load_dotenv()

# Obtém a chave da API do Mercado Livre do arquivo .env
KEY = os.getenv('KEY')
URL = os.getenv('ML_API_URL')

if not KEY or not URL:
    raise ValueError("Chave da API ou URL do Mercado Livre não encontrada. Verifique o arquivo .env")

main = Blueprint('main', __name__)

RANDOM_TERMS = ['smartphone', 'televisão', 'tablet', 'fones de ouvido', 'mouse', 'teclado', 'relógio', 'bicicleta', 'câmera', 'cadeira']

def fetch_mercado_livre_products(query):
    try:
        response = requests.get(URL, params={'q': query, 'access_token': KEY})
        response.raise_for_status()
        data = response.json()
        
        products = []
        for item in data.get('results', []):
            product = {
                'title': item.get('title'),
                'thumbnail': item.get('thumbnail', '/static/default-image.jpg'),
                'original_price': item.get('price'),
                'promo_price': item.get('price'),
                'company': 'Mercado Livre',
                'url': item.get('permalink')
            }
            products.append(product)

        return products

    except requests.exceptions.RequestException as e:
        print("Request Exception:", e)
        return []

@main.route('/')
def home():
    produtos = scraping_zoom() # zoom.com
    query = request.args.get('query', random.choice(RANDOM_TERMS))
    mercado_livre_products = fetch_mercado_livre_products(query)
    print(mercado_livre_products)  # No método home
    if not mercado_livre_products:
        return "Nenhum produto encontrado no Mercado Livre."

    return render_template('index.html', mercado_livre=mercado_livre_products,produto=produtos)


@main.route('/zoom')
def mercado_livre():
    produtos = scraping_zoom()

    if not produtos:
        return "Nenhum produto encontrado no site de scraping."

    print(produtos)  # Verifique se os produtos estão sendo retornados corretamente

    return render_template('mercado_livre.html', products=produtos)
