from django.test import RequestFactory, TestCase

from deputados.models import Deputado
from deputados.services import popular_base_com_dados_deputados
from deputados.tests.factories import EstruturaJsonDeputadosFactory
from deputados.views import DeputadoViewSet


class DeputadoViewsTest(TestCase):
    # https://docs.djangoproject.com/en/4.1/intro/tutorial05/
    # https://docs.djangoproject.com/en/4.1/topics/testing/advanced/
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

        self.estrutura_estatica_json_deputados = EstruturaJsonDeputadosFactory()

    def test_popular_base_com_dados_deputados(self):
        resposta_da_api = self.estrutura_estatica_json_deputados.json_dados
        popular_base_com_dados_deputados(resposta_da_api)

        deputados_no_banco = Deputado.objects.all()

        total_deputados_no_json = len(self.estrutura_estatica_json_deputados.lista_deputados)
        total_deputados_cadastrados = deputados_no_banco.count()
        self.assertTrue(total_deputados_cadastrados == total_deputados_no_json)
        # ou, o mesmo que
        self.assertTrue(total_deputados_no_json == 3)
        self.assertTrue(total_deputados_cadastrados == 3)

        # verificando pela api se retorna o mesmo
        request = self.factory.get('/')

        response = DeputadoViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200)

        """
        {
            "count": 3,
            "next": "http://localhost:8000/?format=json&limit=5&offset=5",
            "previous": null,
            "results": [
            {
                "id": 12,
                "id_api": 204549,
                "uri": "https://dadosabertos.camara.leg.br/api/v2/deputados/204549",
                "nome": "AJ Albuquerque",
                "sigla_partido": "PP",
                "uri_partido": "https://dadosabertos.camara.leg.br/api/v2/partidos/37903",
                "sigla_uf": "CE",
                "id_legislatura": 56,
                "url_foto": "https://www.camara.leg.br/internet/deputado/bandep/204549.jpg",
                "email": null
            }, (...)
        }
        """

        self.assertEqual(response.data.get('count'), 3)


