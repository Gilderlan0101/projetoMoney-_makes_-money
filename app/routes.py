from flask import render_template, Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')


@main.route('/categorias')
def categorias():
    return render_template('all_lojas.html')

# @main.route('/sobre')
# def sobre():
#     return render_template('sobre.html')

# @main.route('/contato')
# def contato():
#     return render_template('contato.html')
