# Projeto Cálculo de Frete

Este projeto é uma aplicação web para calcular o valor do frete com base no CEP e no peso do pacote. A aplicação utiliza a API BrasilAPI para obter informações sobre o endereço a partir do CEP fornecido.

## Tecnologias Utilizadas

- Python
- Flask
- HTML/CSS
- Requests (biblioteca Python para fazer requisições HTTP)

## Estrutura do Projeto

- `app.py`: Arquivo principal da aplicação Flask.
- `templates/index.html`: Template HTML para a interface do usuário.
- `static/style.css`: Arquivo CSS para estilização da página (se necessário).

## Como Executar o Projeto

1. Clone o repositório para sua máquina local.
2. Navegue até o diretório do projeto.
3. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```
4. Instale as dependências necessárias:
    ```bash
    pip install flask requests
    ```
5. Execute a aplicação:
    ```bash
    python app.py
    ```
6. Abra seu navegador e acesse `http://127.0.0.1:5000`.

## Como Usar

1. Insira o CEP e o peso do pacote no formulário.
2. Clique no botão "Calcular".
3. O valor do frete será exibido na tela, juntamente com as informações do endereço.

## Estrutura de Preços

Os preços são calculados com base na região do estado de destino:

- Sudeste: R$ 5,00 por 100g
- Sul: R$ 6,00 por 100g
- Centro-Oeste: R$ 7,00 por 100g
- Nordeste: R$ 8,00 por 100g
- Norte: R$ 10,00 por 100g

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
