import requests
import pandas as pd

def noticiaPrincipal(url):
    # Capturar uma solicitação GET para a URL
    resposta = requests.get(url)
    resposta = resposta.text

    # Encontrar o índice das tags
    TagInicial = '<h3'
    TagFinal = '</h3>'
    IndexInicial = resposta.find(TagInicial)
    IndexInicial = resposta.find('>', IndexInicial) + 1
    IndexFinal = resposta.find('<!', IndexInicial)

    # Extrair o texto entre as tags <h3> e </h3>
    title = resposta[IndexInicial:IndexFinal].strip()
    return title

# Exemplo de uso
url = 'https://www.uol.com.br/'  # Substitua pelo URL da página HTML que contém o <h3>
Noticia = noticiaPrincipal(url)
print(Noticia)
