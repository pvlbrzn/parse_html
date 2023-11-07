import requests
import json
from bs4 import BeautifulSoup as Bs




def get_html(url):
    response = requests.get(url)
    html_doc = Bs(response.text, features='lxml')
    return html_doc


def main():
    a = get_html("https://play.google.com/store/books?hl=ru&gl=US")
    container = a.select_one("#yDmH0d > c-wiz.SSPGKf.glB9Ve.K1b9Kc > div > div > div.N4FjMb.Z97G4e > c-wiz > div")
    items = container.select(".hP61id")
    result = []
    for item in items:
        name_box = item.select_one(".Epkrse")
        price_box = item.select_one(".VfPpfd")
        result.append({"name": name_box.text, "price": price_box.text})
    with open("result.json", "w") as file:
        file.write(json.dumps(result, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    main()