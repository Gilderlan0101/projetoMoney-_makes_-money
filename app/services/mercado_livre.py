
import requests
import os
from dotenv import load_dotenv
load_dotenv()

KEY = os.getenv('KEY')
URL = os.getenv('ML_API_URL')

if not KEY or not URL:
    raise ValueError("Chave da API ou URL do Mercado Livre não encontrada. Verifique o arquivo .env")

def fetch_mercado_livre_products(queries):
    products = []
    
    for query in queries:  # Itera sobre cada termo de busca
        try:
            response = requests.get(URL, params={'q': query, 'access_token': KEY})
            response.raise_for_status()
            data = response.json()
            
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

        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar {query}: {e}")
            continue

    return products