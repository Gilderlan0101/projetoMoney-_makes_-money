import requests
import os
from dotenv import load_dotenv

load_dotenv()

CATEGORIES_URL = os.getenv('ML_API_URL','https://api.mercadolibre.com/sites/MLB/search?category=MLB1144')  # URL para obter categorias
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

        
def fetch_products_by_query(query='Games'):
    """
    Busca produtos relacionados à categoria de games e palavra-chave específica.
    :param query: Termo de busca (ex.: Games)
    :return: Lista de produtos
    """
    try:
        response = requests.get(
            SEARCH_URL, 
            params={
                'q': query,          # Palavra-chave
                'category': 'MLB1144'  # ID da categoria de Games
            }
        )
        response.raise_for_status()
        data = response.json()
        print(f"Dados retornados pela busca: {data}")
        return [
            {
                'title': item.get('title'),
                'thumbnail': item.get('thumbnail', '/static/default-image.jpg'),
                'price': item.get('price'),
                'permalink': item.get('permalink')
            }
            for item in data.get('results', [])
        ]
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar produtos para o termo {query}: {e}")
        return []
