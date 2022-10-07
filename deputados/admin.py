from django.contrib import admin

from deputados.models import Deputado


@admin.register(Deputado)
class DeputadoAdmin(admin.ModelAdmin):
    list_display = ("id", "id_api", "nome", "sigla_partido", "sigla_uf")
    list_filter = ("sigla_partido", "sigla_uf")
    search_fields = ("nome",)
