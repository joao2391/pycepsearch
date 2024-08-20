from bs4 import BeautifulSoup
import requests
from py_cep_search.response_correios import ResponseCep

class CepSearch:

    def __init__(self):
        self.url_address = "https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaEndereco.cfm"
        self.url_cep = "https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm"


    def get_address_by_cep(self, cep) -> dict:
        if not cep.strip():
            raise ValueError("CEP is empty")
        
        form_data = { "CEP": cep }

        data = requests.post(self.url_address, data=form_data)

        soup_address = BeautifulSoup(data.text, features="html.parser")
        nodes = soup_address.find_all("td")
        
        rua = nodes[0].string.strip()
        bairro = nodes[1].string.strip()
        data_splitted = nodes[2].string.split("/")
        cidade = data_splitted[0].strip()
        uf = data_splitted[1].strip()
        
        result = ResponseCep(rua, bairro, cidade, cep, uf)

        return result.__dict__