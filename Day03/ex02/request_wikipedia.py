import requests
import json
import dewiki
import sys

def request_wikipedia(term):
    # Parâmetros da solicitação
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": term,
        "format": "json",
    }

    # Envie a solicitação
    response = requests.get(url, params=params)

    print(response.json()['query']['search'][0]['pageid'])

    # Verifique se a solicitação foi bem-sucedida
    # if response.status_code == 200:
    #     data = response.json()
    #     print(data)
    #     # Processar os dados da resposta aqui
    # else:
    #     print("Erro na solicitação à API da Wikipedia")

if __name__ == '__main__':
    request_wikipedia('escola 42')
