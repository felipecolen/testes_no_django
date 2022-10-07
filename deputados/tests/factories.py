class EstruturaJsonDeputadosFactory():

    def __init__(self):
        self.json_dados = {
            "dados": [
                {
                    "id": 204521,
                    "uri": "https://dadosabertos.camara.leg.br/api/v2/deputados/204521",
                    "nome": "Abou Anni",
                    "siglaPartido": "UNIÃO",
                    "uriPartido": "https://dadosabertos.camara.leg.br/api/v2/partidos/38009",
                    "siglaUf": "SP",
                    "idLegislatura": 56,
                    "urlFoto": "https://www.camara.leg.br/internet/deputado/bandep/204521.jpg",
                    "email": None
                },
                {
                    "id": 204379,
                    "uri": "https://dadosabertos.camara.leg.br/api/v2/deputados/204379",
                    "nome": "Acácio Favacho",
                    "siglaPartido": "MDB",
                    "uriPartido": "https://dadosabertos.camara.leg.br/api/v2/partidos/36899",
                    "siglaUf": "AP",
                    "idLegislatura": 56,
                    "urlFoto": "https://www.camara.leg.br/internet/deputado/bandep/204379.jpg",
                    "email": None
                },
                {
                    "id": 204560,
                    "uri": "https://dadosabertos.camara.leg.br/api/v2/deputados/204560",
                    "nome": "Adolfo Viana",
                    "siglaPartido": "PSDB",
                    "uriPartido": "https://dadosabertos.camara.leg.br/api/v2/partidos/36835",
                    "siglaUf": "BA",
                    "idLegislatura": 56,
                    "urlFoto": "https://www.camara.leg.br/internet/deputado/bandep/204560.jpg",
                    "email": None
                },
            ]
        }
        # lista todas as chaves no primeiro nível
        # nesse caso só vai listar a chave "dados"
        self.chaves = [chave for chave in self.json_dados.keys()]

        self.lista_deputados = self.json_dados.get('dados')
        # vamos pegar os valores da chave "dados", que é uma lista
        # o primeiro item vai conter o dicionário/json com os dados do deputado, de fato
        primeiro_item_da_lista = self.lista_deputados[0]
        self.chaves_dados_do_deputado = [chave for chave in primeiro_item_da_lista.keys()]

