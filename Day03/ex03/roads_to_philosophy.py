import requests
import sys
from bs4 import BeautifulSoup

def roads_to_philosophy(term):

    title = ''
    subject_titles = []
    counter = 0
    init_term = term

    print(term)

    while title != 'Philosophy':
        search_url = f"https://en.wikipedia.org/wiki/{term}"

        response = requests.get(search_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            base = soup.find("div",{'class':'mw-body-content mw-content-ltr'})
            parag = base.find_all("p")
            
            uris = []
            titles = []

            for p in parag:
                a = str(p.find('a')).split()
                for i in a:
                    if 'href' in i and not ':' in i:
                        uris.append(i)
                    if 'title' in i and not ':' in i:
                        titles.append(i)
                    pass
                
            term = uris[0].replace('"','').replace('href=/wiki/','')
            ind = []
            for i in range(1,len(titles[0])-1):
                if titles[0][i] == '"':
                    ind.append(i)
            title = titles[0][ind[0] + 1:ind[1] if len(ind)>1 else 1000]
            for t in subject_titles:
                if t == title:
                    print("It's a dead end !")
                    return
            subject_titles.append(title)
            print(title)
            counter += 1
    print(f'{counter} roads from {init_term} to philosophy !')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Please provide a search query as an argument.")
        sys.exit(1)
    roads_to_philosophy(sys.argv[1])
