from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_products():
    url = "http://books.toscrape.com/"  # Exemplo de site
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        products = []
        
        # Encontrar todos os produtos
        product_containers = soup.find_all('article', class_='product_pod')
        
        for container in product_containers:
            # Encontrar o nome e o link do produto
            link_tag = container.find('h3').find('a')
            if link_tag:
                product_name = link_tag['title']  # nome do produto
                product_link = url + link_tag['href'].replace('../../../', '')  # completar o link do produto com a URL base
            
            # Encontrar a imagem dentro da div image_container
            image_container = container.find(class_='image_container')
            if image_container:
                img_tag = image_container.find('img')
                if img_tag:
                    picture_produto = url + img_tag['src'].replace('../../', '')  # completar o link da imagem

            # Encontrar o preço do produto
            product_price = container.find(class_='product_price')
            if product_price:
                price_tag = product_price.find('p', class_='price_color')  # Encontra a tag de preço com a classe específica
                if price_tag:
                    response_value = price_tag.text.strip()
                else:
                    response_value = 'Preço não encontrado'
            else:
                response_value = 'Informação de preço não disponível'

            # Adicionar produto à lista de produtos
            products.append({
                'name': product_name,
                'link': product_link,
                'img': picture_produto,
                'value': response_value
            })

        return products
    else:
        print(f"Erro ao acessar o site: {response.status_code}")
        return []
