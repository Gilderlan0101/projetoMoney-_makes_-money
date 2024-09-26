
import requests  # Blibioteca python para  requisição HTTP
#Beautiful Soup é amplamente utilizada em projetos de web scraping
# permitindo que desenvolvedores obtenham dados de maneira eficiente e prática.
from bs4 import BeautifulSoup



def scrape_products():
    url = "https://www.tokstok.com.br/promocao/todos-os-produtos?srsltid=AfmBOooolkZKvBDjbwjNEf6BIjc6jEXOIjqmzcjOJCLEdSku4RI6uHVm"  # Exemplo de site
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        products = []
        
        # Encontrar todos os produtos
        product_containers = soup.find_all(class_='c-jyRwEJ c-jyRwEJ-hQofwP-size-contained')
        
        for container in product_containers:
            # Encontrar o nome e o link do produto
            # link_tag = container.find('div').find('p')
            # if link_tag:
            #     product_name = link_tag['p']  # nome do produto
            #     product_link = url + link_tag['href'].replace('../../../', '')  # completar o link do produto com a URL base
            #     print(product_link)
            
            # Encontrar a imagem dentro da div image_container
            # image_container = container.find(class_="dcl-product-image-container")
            # if image_container:
            #     img_tag = image_container.find('img')
            #     if img_tag:
            #         picture_produto = url + img_tag['src'].replace('../../', '')  # completar o link da imagem

            # Encontrar o preço do produto
            product_price = container.find(class_='c-gyMVMl c-gyMVMl-cLCUdC-size-300 c-gyMVMl-hyvuql-weight-bold c-gyMVMl-ZzHSU-fontStyle-normal c-gyMVMl-fNnUSH-lineHeight-medium c-gyMVMl-hnUxyT-color-green60')
            if product_price:
                price_tag = product_price.find('div', class_='c-gyMVMl c-gyMVMl-cLCUdC-size-300 c-gyMVMl-hyvuql-weight-bold c-gyMVMl-ZzHSU-fontStyle-normal c-gyMVMl-fNnUSH-lineHeight-medium c-gyMVMl-hnUxyT-color-green60')  # Encontra a tag de preço com a classe específica
                if price_tag:
                    response_value = price_tag.text.strip()
                else:
                    response_value = 'Preço não encontrado'
            else:
                response_value = 'Informação de preço não disponível'

            # Adicionar produto à lista de produtos
            products.append({
                
                
                'value': response_value
            })
            
            
            print(response_value)

        return products
    else:
        print(f"Erro ao acessar o site: {response.status_code}")
        return []
go = scrape_products()
