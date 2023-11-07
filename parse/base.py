import requests
import json
from bs4 import BeautifulSoup as Bs
from abc import ABC, abstractmethod




class ParserBase(ABC):
    html = None
    data = None
    _user_agent = (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    )


    def __init__(self, url):
        self._url = url
        self.data = []


    def get_html(self):
        response = requests.get(self._url, headers={"User-Agent": self._user_agent})
        if response.status_code == 200:
            self.html = Bs(response.text, features='lxml')
            return ...
        raise RuntimeError("Invalid response: status = {}, text = {}".format(response.status_code, response.text))


    @abstractmethod
    def parse(self):
        raise NotImplementedError("Method not implemeted")


    def save_json(self, file_name):
        with open(file_name, "w") as file:
            file.write(json.dumps(self.data, indent=4, ensure_ascii=False))
