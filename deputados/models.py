from django.db import models


class Deputado(models.Model):
    """
    Estrutura do json que vem da api da Câmara
    {
        "dados": [
        {
              "id": 178835,
              "uri": "https://dadosabertos.camara.leg.br/api/v2/deputados/178835",
              "nome": "Afonso Motta",
              "siglaPartido": "PDT",
              "uriPartido": "https://dadosabertos.camara.leg.br/api/v2/partidos/36786",
              "siglaUf": "RS",
              "idLegislatura": 56,
              "urlFoto": "https://www.camara.leg.br/internet/deputado/bandep/178835.jpg",
              "email": null
        },
    }
    """

    id_api = models.PositiveIntegerField(verbose_name='Id na API da Câmara')
    uri = models.URLField()
    nome = models.CharField(max_length=255)
    sigla_partido = models.CharField(max_length=10)
    uri_partido = models.URLField()
    sigla_uf = models.CharField(max_length=2)
    id_legislatura = models.PositiveIntegerField()
    url_foto = models.URLField()
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.id_api})"

    class Meta:
        ordering = ("-id",)

