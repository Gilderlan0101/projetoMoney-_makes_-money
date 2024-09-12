from flask import render_template, Blueprint
import requests


main = Blueprint('main', __name__)


# Configurações da API do Mercado Livre
ML_API_URL = "https://api.mercadolibre.com/sites/MLB/search" # Coloca isso no arquivo privado
ML_QUERY = "laptop"  # Exemplo de termo de pesquisa

def fetch_mercado_livre_products():
    """Busca produtos na API do Mercado Livre"""
    try:
        response = requests.get(ML_API_URL, params={'q': ML_QUERY})
        response.raise_for_status()  # Verifica se houve erro na requisição
        data = response.json()  # Tenta decodificar a resposta como JSON
        
        # Adiciona logging para depuração
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
    # Solicita os dados da API do Mercado Livre
    mercado_livre_products = fetch_mercado_livre_products()

    # Se não houver produtos do Mercado Livre, exibe uma mensagem de erro ou retorna uma lista vazia
    if not mercado_livre_products:
        return "Nenhum produto encontrado no Mercado Livre."

    return render_template('index.html', products=mercado_livre_products)
