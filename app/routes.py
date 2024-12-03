
from flask import Blueprint, render_template
import random
from app.services.scraping_zoom import scraping_zoom
from app.services.mercado_livre import  fetch_products_by_category

from dotenv import load_dotenv
import os
load_dotenv()

RANDOM_TERMS = os.getenv('RANDOM_TERMS').split(',')
main = Blueprint('main', __name__)

#######################################################################################################################
@main.route('/', methods=['GET', 'POST'])
def home():
    produtos = scraping_zoom()  # scraping do site Zoom
    
    # Escolhe aleatoriamente 1 termo para busca (a partir de RANDOM_TERMS)
    queries = random.choices(RANDOM_TERMS, k=1)
    
    # Busca produtos no Mercado Livre para os termos escolhidos
    mercado_livre_products = fetch_products_by_category(queries)

    print(mercado_livre_products)
    
    if not mercado_livre_products:
        return "Nenhum produto encontrado no Mercado Livre."

    return render_template('index.html', mercado_livre=mercado_livre_products, produto=produtos)



#########################################################################################################################################

@main.route('/mercado_livre')
def mercado_livre():
    produtos = scraping_zoom()
    queries = random.choices(RANDOM_TERMS)
    mercado_livre_products = fetch_products_by_category(queries)

    if not produtos:
        return "Nenhum produto encontrado no site de promoção tente no grupo na pagina home."


    return render_template('mercado_livre.html', mercado_livre=mercado_livre_products)

#########################################################################################################################################

@main.route('/categoria/<category_id>')
def categoria(category_id):
    """
    Rota para exibir produtos de uma categoria específica.
    :param category_id: ID da categoria
    """
    produtos = (category_id)
    if not produtos:
        return "Nenhum produto encontrado nesta categoria."
    return {'mercado_livre': produtos}