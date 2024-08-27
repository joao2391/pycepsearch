import unittest
from src.py_cep_search import cepsearch
from unittest.mock import patch, MagicMock
from pathlib import Path

class CepSearchTests(unittest.TestCase):

    def setUp(self) -> None:
        self.url_address = "https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaEndereco.cfm"
        self.url_cep = "https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm"

        relative_path = 'mock_data_address.html'
        dir = Path(__file__).parent
        absolute_path = dir.joinpath(relative_path)
        with open(absolute_path, "r") as file:
            self.html_adress = file.read()

        relative_path = 'mock_data_cep.html'
        dir = Path(__file__).parent
        absolute_path = dir.joinpath(relative_path)
        with open(absolute_path, "r") as file:
            self.html_cep = file.read()


    @patch('requests.post')
    def test_get_address_by_cep(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status = 200

        mock_response.read.return_value = self.html_adress
        mock_response.text = self.html_adress

        mock_requests.return_value = mock_response

        obj = cepsearch.CepSearch()
        address = obj.get_address_by_cep("69918-120")
        self.assertIsNotNone(address)
        self.assertEqual(address["rua"], "Rua Frei Caneca")

    

    if __name__ == '__main__':
        unittest.main(argv=['first-arg-is-ignored'], exit=False)