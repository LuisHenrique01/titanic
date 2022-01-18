# Save yourself from the Titanic

Essa API recebe três dados classe [0, 3], sexo (0 homem e 1 mulher) e idade.

## Como é feito o cálculo?

É usado um modelo de inteligência artificial baseado em regressão linear, esse modelo tem como base o livro “Python para Análise de Dados". A ideia de transformar isso em uma API é basicamente para melhorar minhas capacidades de implantação de exemplos simples em pŕodução mesmo não sendo o modelo ideal. Foi usado o Framework Chalice AWS para o desenvolvimento da API.

### Instalação

1. Criar ambiente virtual.

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Instalando pacotes.

   ```bash
   pip install -r requirements.txt
   ```

3. Ativando API

   ```bash
   chalice local
   ```
