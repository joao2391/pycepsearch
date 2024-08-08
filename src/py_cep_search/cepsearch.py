from bs4 import BeautifulSoup
import urllib.request
import requests
import json
from py_cep_search.response_correios import ResponseCorreios

class CepSearch:

    def __init__(self):
        self.url = "https://buscacepinter.correios.com.br/app/endereco/carrega-cep-endereco.php"

    def get_address_by_cep(self, cep) -> dict:
        address = {}
        form_data = {
                        {"pagina","/app/endereco/index.php"},
                        {"endereco",cep },
                        {"tipoCEP","ALL" }
                    }
        
        data = requests.post(self.url, json=form_data)
        response_dict = json.loads(data)
        response = ResponseCorreios(**response_dict)



