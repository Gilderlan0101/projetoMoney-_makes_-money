from app import create_app

app = create_app()



@app.after_request
def add_header(response):
    # Desabilitar cache de arquivos estáticos
    response.headers['Cache-Control'] = 'no-store'
    return response


if __name__ == '__main__':
    app.run(debug=True)
