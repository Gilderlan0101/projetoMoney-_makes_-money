
from flask import Blueprint, render_template
import random
from app.services.scraping_zoom import scraping_zoom
from app.services.mercado_livre import fetch_mercado_livre_products
from dotenv import load_dotenv
import os
load_dotenv()

RANDOM_TERMS = os.getenv('RANDOM_TERMS').split(',')
main = Blueprint('main', __name__)

#######################################################################################################################
@main.route('/', methods=['GET', 'POST'])
def home():
    produtos = scraping_zoom()  # zoom.com
    print(produtos)
    # Gera três termos de busca aleatórios
    queries = random.choices(RANDOM_TERMS, k=3)
    # Busca produtos no Mercado Livre para os três termos distintos
    mercado_livre_products = fetch_mercado_livre_products(queries)
    print(mercado_livre_products)
    
    if not mercado_livre_products:
        return "Nenhum produto encontrado no Mercado Livre."
    
    return render_template('index.html', mercado_livre=mercado_livre_products, produto=produtos)


#########################################################################################################################################

@main.route('/mercado_livre')
def mercado_livre():
    produtos = scraping_zoom()
    queries = random.choices(RANDOM_TERMS)
    mercado_livre_products = fetch_mercado_livre_products(queries)

    if not produtos:
        return "Nenhum produto encontrado no site de scraping."


    return render_template('mercado_livre.html', mercado_livre=mercado_livre_products)
