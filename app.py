from flask import Flask, render_template, request
import requests

app = Flask(__name__)

regioes = {
    "Sudeste": {"estados": ["SP", "RJ", "MG", "ES"], "preco_100g": 5.00},
    "Sul": {"estados": ["PR", "SC", "RS"], "preco_100g": 6.00},
    "Centro-Oeste": {"estados": ["MT", "MS", "GO", "DF"], "preco_100g": 7.00},
    "Nordeste": {"estados": ["BA", "SE", "AL", "PE", "PB", "RN", "CE", "PI", "MA"], "preco_100g": 8.00},
    "Norte": {"estados": ["AM", "RR", "AP", "PA", "TO", "RO", "AC"], "preco_100g": 10.00},
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    cep = request.form.get('cep')
    peso = request.form.get('peso')
    API_ENDPOINT = f'https://brasilapi.com.br/api/cep/v1/{cep}'
    response = requests.get(API_ENDPOINT)
    if response.status_code == 200:
        data = response.json()
        state = data['state']
        city = data['city']
        street = data['street']
        for regiao, dados in regioes.items():
            if state in dados["estados"]:
                preco_100g = dados["preco_100g"]
                frete = (float(peso) / 100) * preco_100g
                return render_template('index.html', frete=frete, city=city, state=state, regiao=regiao, street=street)
    return render_template('index.html', error="CEP inválido")

if __name__ == '__main__':
    app.run(debug=True)