from django.test import RequestFactory, TestCase

from deputados.services import consumir_api_deputados_camara, processar_retorno_da_api
from deputados.tests.factories import EstruturaJsonDeputadosFactory


class DeputadoTest(TestCase):
    # https://docs.djangoproject.com/en/4.1/intro/tutorial05/
    # https://docs.djangoproject.com/en/4.1/topics/testing/advanced/
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

        self.estrutura_estatica_json_deputados = EstruturaJsonDeputadosFactory()
        self.estrutura_dinamica_json_deputados = consumir_api_deputados_camara()

    def test_validar_estrutura_de_chaves_json_api_camara(self):
        lista_dinamica_de_chaves_get_api = [k for k in self.estrutura_dinamica_json_deputados.keys()]
        # o json que vem da api deve possuir as chaves da estrutura ou mais
        # podem surgir novos campos, mas não podem diminuir ou mudar o nome
        self.assertGreaterEqual(lista_dinamica_de_chaves_get_api, self.estrutura_estatica_json_deputados.chaves)

    def test_validar_o_processamento_json_retornando_lista_de_deputados(self):
        dados_processados = processar_retorno_da_api(self.estrutura_dinamica_json_deputados)
        self.assertTrue(type(dados_processados) == list)
        self.assertTrue(dados_processados[0])

    def test_validar_estrutura_de_chaves_json_api_camara_dados_deputados(self):
        dados_da_api = self.estrutura_dinamica_json_deputados

        dados_processados = processar_retorno_da_api(dados_da_api)
        primeiro_item_da_lista = dados_processados[0]
        lista_dinamica_de_chaves_do_deputado = [k for k in primeiro_item_da_lista.keys()]

        # o json que vem da api deve possuir as chaves da estrutura ou mais
        # podem surgir novos campos, mas não podem diminuir ou mudar o nome
        self.assertGreaterEqual(lista_dinamica_de_chaves_do_deputado, self.estrutura_estatica_json_deputados.chaves_dados_do_deputado)

