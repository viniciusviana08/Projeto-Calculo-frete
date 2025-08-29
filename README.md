# 🚚 Calculadora de Frete

![Badge Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Badge Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Badge TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

Uma aplicação web moderna e responsiva para calcular custos de frete com base no CEP e peso da encomenda. O projeto foi desenvolvido com Python e Flask no backend e estilizado com Tailwind CSS para uma interface elegante e intuitiva.

[![Deploy with Vercel](https://vercel.com/button)](https://projeto-calculo-frete.vercel.app/)

---

## 🚀 Acesso ao Projeto

Você pode testar a aplicação em tempo real através do link de deploy na Vercel:

**[https://projeto-calculo-frete.vercel.app/](https://projeto-calculo-frete.vercel.app/)**


## ✨ Funcionalidades Principais

-   **Consulta de CEP:** Integração com a [BrasilAPI](https://brasilapi.com.br/) para buscar o endereço completo (rua, cidade e estado) de forma automática.
-   **Cálculo por Região:** O valor do frete é determinado pela região do país (Norte, Nordeste, Sudeste, Sul e Centro-Oeste) correspondente ao CEP informado.
-   **Interface Moderna:** Design limpo e agradável, totalmente responsivo, que se adapta a desktops e dispositivos móveis, construído com Tailwind CSS.
-   **Feedback Instantâneo:** O resultado do cálculo ou mensagens de erro são exibidos dinamicamente na mesma página, proporcionando uma excelente experiência de usuário.

---

## 🛠️ Tecnologias Utilizadas

-   **Backend:** Python 3, Flask
-   **Frontend:** HTML, Tailwind CSS (via CDN)
-   **API Externa:** BrasilAPI para consulta de CEP
-   **Hospedagem:** Vercel

---

## ⚙️ Como Executar o Projeto Localmente

Siga os passos abaixo para rodar a aplicação em sua máquina:

1.  **Clone este repositório:**
    ```bash
    git clone https://github.com/viniciusviana08/Projeto-Calculo-frete.git
    cd Projeto-Calculo-frete
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    # Para Windows
    python -m venv venv
    venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências necessárias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação Flask:**
    ```bash
    python app.py
    ```

5.  **Acesse no seu navegador:**
    Abra o endereço [http://127.0.0.1:5000](http://127.0.0.1:5000) e comece a usar!

---

## 👨‍💻 Autor

Desenvolvido por Vinícius Viana. 
