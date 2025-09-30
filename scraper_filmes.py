import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL do site
url = "https://www.imdb.com/chart/moviemeter/"

# Headers para o site aceitar a requisição
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

print("Buscando filmes...")
pagina = requests.get(url, headers=headers)
soup = BeautifulSoup(pagina.content, 'html.parser')

# Listas para guardar os dados
posicoes = []
titulos = []
anos = []
notas = []

# Procurando os filmes na página
filmes = soup.find_all('li', class_='ipc-metadata-list-summary-item')

if len(filmes) == 0:
    filmes = soup.select('ul.ipc-metadata-list li')

if len(filmes) == 0:
    filmes = soup.find_all('li')

print(f"Encontrei {len(filmes)} elementos")

# Pegando informações de cada filme
contador = 0
for filme in filmes:
    # Pegando o título
    titulo = filme.find('h3')
    if not titulo:
        titulo = filme.find('a')

    if titulo:
        titulo_texto = titulo.text.strip()

        if len(titulo_texto) < 2:
            continue

        # Tirando o número do título
        if '. ' in titulo_texto:
            partes = titulo_texto.split('. ', 1)
            if len(partes) > 1:
                titulo_texto = partes[1]

        contador += 1
        posicoes.append(contador)
        titulos.append(titulo_texto)

        # Pegando o ano
        ano = filme.find('span', class_='cli-title-metadata-item')
        if not ano:
            spans = filme.find_all('span')
            ano_texto = "N/A"
            for span in spans:
                texto = span.text.strip()
                if len(texto) == 4 and texto.isdigit():
                    ano_texto = texto
                    break
            anos.append(ano_texto)
        else:
            anos.append(ano.text.strip())

        # Pegando a nota
        nota = filme.find('span', class_='ipc-rating-star--rating')
        if not nota:
            spans = filme.find_all('span')
            nota_texto = "N/A"
            for span in spans:
                texto = span.text.strip()
                if '.' in texto and len(texto) <= 4:
                    try:
                        float(texto)
                        nota_texto = texto
                        break
                    except:
                        pass
            notas.append(nota_texto)
        else:
            notas.append(nota.text.strip())

        if contador >= 100:
            break

print(f"\nTotal coletado: {contador} filmes")

if contador == 0:
    print("\nNão consegui pegar os filmes")
else:
    # Criando um dicionário com os dados
    dados = {
        'posicao': posicoes,
        'titulo': titulos,
        'ano': anos,
        'nota': notas
    }

    # Transformando em DataFrame
    df = pd.DataFrame(dados)

    # Salvando em CSV
    df.to_csv('movies.csv', index=False, encoding='utf-8-sig')

    print("Pronto! Dados salvos em movies.csv")
    print(f"Total de filmes: {len(df)}")
    print("\nPrimeiros 5 filmes:")
    print(df.head())