import requests
from bs4 import BeautifulSoup

def scraping_zoom():
    url = "https://www.zoom.com.br/?og=18000&og=18000&gad_source=1&gclid=Cj0KCQjw3bm3BhDJARIsAKnHoVWW8OBS5VZ4LsMD_KbqIlBYHFRonyZ_sTj3gfCKke880QqmqVRdwbsaAuiqEALw_wcB"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
#########################################################################################################################################

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Usando a classe correta para o container de produtos
        product_containers = soup.find_all(class_="ProductCard_ProductCard_Inner__gapsh")
        
        produtos = []

#########################################################################################################################################
        for container in product_containers:
            # Extraindo o nome do produto
            nome = container.find(class_="ProductCard_ProductCard_Name__U_mUQ")
            nome_produto = nome.text.strip() if nome else 'Nome não encontrado'

            # Extraindo o preço do produto
            preco = container.find(class_="Text_Text__ARJdp Text_MobileHeadingS__HEz7L")
            preco_produto = preco.text.strip() if preco else 'Preço não encontrado'

            # Extraindo a imagem do produto
            imagen_produto = container.find(class_="ProductCard_ProductCard_Image__4v1sa")
            img_tag = imagen_produto.find('img') if imagen_produto else None
            img_url = img_tag['src'] if img_tag and 'src' in img_tag.attrs else 'Imagem não encontrada'

            # Extraindo o link do produto
            link_product = container.find('a', class_='dsvia-link-overlay css-1ogn60p')
            product_link = link_product['href'] if link_product and 'href' in link_product.attrs else 'Link não encontrado'

            # Extraindo a descrição do produto (ex: Menor preço via Fast Shop)
            descricao = container.find(class_="ProductCard_ProductCard_BestMerchant__JQo_V")
            descricao_produto = descricao.text.strip() if descricao else 'Descrição não encontrada'

            # Extraindo o rating
            rating = container.find(class_="ProductCard_ProductCard_Rating__kCx7o")
            rating_produto = rating.text.strip() if rating else 'Rating não encontrado'

            # Extraindo a condição (ex: Cashback)
            cashback = container.find(class_="ProductCard_ProductCard_CashbackInfoLabel__Td_EJ")
            cashback_info = cashback.text.strip() if cashback else 'Cashback não encontrado'
#########################################################################################################################################

            produtos.append({
                'name': nome_produto,
                'value': preco_produto,
                'image': img_url,
                'link': product_link,
                'description': descricao_produto,
                'rating': rating_produto,
                'cashback': cashback_info
            })
        
        return produtos



