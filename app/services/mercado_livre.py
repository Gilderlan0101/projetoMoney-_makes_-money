import requests
import os
from dotenv import load_dotenv

load_dotenv()

CATEGORIES_URL = os.getenv('ML_API_URL')  # URL para obter categorias
SEARCH_URL = "https://api.mercadolibre.com/sites/MLB/search"  # URL para buscar produtos

def fetch_categories():
    """
    Obtém a lista de categorias do Mercado Livre.
    :return: Lista de categorias principais
    """
    try:
        response = requests.get(CATEGORIES_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar categorias: {e}")
        return []

def fetch_products_by_category(category_id):
    """
    Busca produtos de uma categoria específica.
    :param category_id: ID da categoria (ex.: MLB1144 para Games)
    :return: Lista de produtos
    """
    try:
        response = requests.get(SEARCH_URL, params={'category': category_id})
        response.raise_for_status()
        data = response.json()
        products = []
        for item in data.get('results', []):
            product = {
                'title': item.get('title'),
                'thumbnail': item.get('thumbnail', '/static/default-image.jpg'),
                'price': item.get('price'),
                'permalink': item.get('permalink')
            }
            products.append(product)
        return products
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar produtos da categoria {category_id}: {e}")
        return []
