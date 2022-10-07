import logging

import requests
from rest_framework import status

from deputados.models import Deputado

logger = logging.getLogger(__name__)


def consumir_api_deputados_camara():
    """
    https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome
    {
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
          "email": null
        }, (...)
      ]
    }
    """

    url = (
        "https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome"
    )
    headers = {
        "accept": "application/json",
    }
    response = requests.get(url=url, headers=headers)

    if response.status_code == status.HTTP_200_OK:
        return response.json()
    else:
        logger.error(f"ERRO ao consultar PJE " f"status_code {response.status_code}")


def processar_retorno_da_api(retorno: dict):
    return retorno.get("dados")


def salvar_dados_do_deputado_no_banco(deputado: dict):
    id_deputado = deputado.get("id")
    nome = deputado.get("nome")
    try:
        dep_db = Deputado.objects.get_or_create(
            id_api=id_deputado,
            uri=deputado.get("uri"),
            nome=nome,
            sigla_partido=deputado.get("siglaPartido"),
            uri_partido=deputado.get("uriPartido"),
            sigla_uf=deputado.get("siglaUf"),
            id_legislatura=deputado.get("idLegislatura"),
            url_foto=deputado.get("urlFoto"),
            email=deputado.get("email"),
        )
        logger.warning(f"Deputado: {dep_db[0]}, cadastrado com sucesso!")
    except Exception as save_deputado_exception:
        logger.error(
            f"Erro ao salvar deputado no banco. "
            f"\nDetalhe do erro: {save_deputado_exception.args}"
        )
        logger.error(f"Dados do Deputado: {nome}, ID: {id_deputado}")


def popular_base_com_dados_deputados(json_deputados: dict):
    lista_deputados = processar_retorno_da_api(json_deputados)

    for deputado in lista_deputados:
        salvar_dados_do_deputado_no_banco(deputado)


def executar_scripts_para_obter_e_salvar_os_dados():
    json_deputados = consumir_api_deputados_camara()
    return popular_base_com_dados_deputados(json_deputados)
