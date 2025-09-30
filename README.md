# Coletor de Filmes do IMDb

Um programa simples em Python que busca os filmes mais populares do IMDb e salva em CSV.

## 5W1H

### O QUE?
Um programa que coleta a lista dos filmes mais populares do IMDb e salva as informações em um arquivo CSV.

Dados coletados:
- Posição no ranking
- Título do filme
- Ano de lançamento
- Nota IMDb

### POR QUÊ?
Atividade da materia de Laboratório de Programação para exercitar o meu conhecimento em python, pandas e manipulação de dados.

### QUEM?
Este projeto foi feito por um aluno de Ciência da Computação.

### QUANDO?
O programa pode ser executado sempre que você quiser dados atualizados dos filmes mais populares do momento.

### ONDE?
- Fonte dos dados: https://www.imdb.com/chart/moviemeter/
- Funciona em: Windows, Linux e Mac

### COMO?
O programa funciona em 4 etapas:
1. Acessa o site do IMDb usando a biblioteca requests
2. Faz o parsing do HTML com BeautifulSoup
3. Extrai e organiza os dados usando pandas
4. Salva tudo em um arquivo CSV

## Como Usar

### Pré-requisitos
- Python 3.7 ou superior instalado
- pip (gerenciador de pacotes do Python)

### Instalação

**1. Instale as bibliotecas necessárias**

No Windows:
```bash
pip install -r requirements.txt
```

No Linux/Mac:
```bash
pip3 install -r requirements.txt
```

### Execução

No Windows:
```bash
python scraper_filmes.py
```

No Linux/Mac:
```bash
python3 scraper_filmes.py
```

### Resultado
Após a execução, o arquivo `movies.csv` será criado na mesma pasta do programa com todos os dados coletados.

## Tecnologias Utilizadas

- **Python 3** - Linguagem de programação
- **requests** - Para fazer requisições HTTP
- **BeautifulSoup4** - Para fazer parsing do HTML
- **pandas** - Para manipular e salvar dados em CSV
