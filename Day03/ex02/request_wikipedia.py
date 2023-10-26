import requests
import json
import dewiki
import sys

def request_wikipedia(term):
    # Primeira query para verificar o id da primeira ocorrencia
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": term,
        "format": "json",
    }

    resp = requests.get(url, params=params)
    page_id = resp.json()['query']['search'][0]['pageid']

    # Segunda solicitacao para pegar o conteudo com base no id
    params_by_id = {
        "action": "query",
        "format": "json",
        "pageids": page_id,
        "prop": "revisions",
        "rvslots": "*",
        "rvprop": "content",
    }

    resp_by_id = requests.get(url, params=params_by_id)
    page_data = resp_by_id.json().get("query", {}).get("pages", {}).get(str(page_id), {})

    wiki_content = page_data["revisions"][0]["slots"]["main"]["*"]

    parsed_content = dewiki.from_string(wiki_content)

    name_file = term.split()
    for e in name_file:
        e = e.strip()
    name_file = '_'.join(name_file) + '.wiki'

    file_ = open(name_file, 'w')
    file_.write(parsed_content)
    file_.close()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error: Please provide a search query as an argument.")
        sys.exit(1)

    request_wikipedia(sys.argv[1])
