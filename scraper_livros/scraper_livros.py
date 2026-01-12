import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# 1. Configurações Iniciais
url_alvo = 'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def coletar_dados():
    print(f"Iniciando coleta em: {url_alvo}...")
    
    try:
        # Fazendo a requisição
        response = requests.get(url_alvo, headers=headers)
        response.raise_for_status() # Para o código se der erro 404 ou 500
        
        # Criando o objeto Soup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontrando todos os produtos (livros) na página
        produtos = soup.find_all('article', class_='product_pod')
        
        lista_dados = []

        # Iterando sobre cada livro encontrado
        for livro in produtos:
            # Extração do Título
            titulo = livro.h3.a['title']
            
            # Extração do Preço (limpando o símbolo da moeda)
            preco_texto = livro.find('p', class_='price_color').text
            preco = float(preco_texto.replace('Â£', ''))
            
            # Extração da Disponibilidade
            estoque = livro.find('p', class_='instock availability').text.strip()
            
            # Extração da Avaliação (Star Rating)
            classe_estrelas = livro.find('p', class_='star-rating')['class']
            estrelas = classe_estrelas[1] # Pega o segundo elemento da classe (ex: 'Four')

            lista_dados.append({
                'Data_Coleta': datetime.now().strftime('%Y-%m-%d'),
                'Titulo': titulo,
                'Preço_Libras': preco,
                'Avaliação': estrelas,
                'Disponibilidade': estoque
            })
            
        return lista_dados

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o site: {e}")
        return []

# 2. Execução e Salvamento
dados = coletar_dados()

if dados:
    # Transformando em DataFrame do Pandas
    df = pd.DataFrame(dados)
    
    # Exibindo uma prévia no terminal
    print("\n--- Prévia dos Dados Coletados ---")
    print(df.head())
    
    # Salvando em Excel (muito valorizado por clientes não técnicos)
    nome_arquivo = 'relatorio_livros.xlsx'
    df.to_excel(nome_arquivo, index=False)
    print(f"\nSucesso! Arquivo '{nome_arquivo}' gerado.")
else:
    print("Nenhum dado foi coletado.")