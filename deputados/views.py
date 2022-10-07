from rest_framework import viewsets

from deputados.models import Deputado
from deputados.serializers import DeputadoSerializer


class DeputadoViewSet(viewsets.ModelViewSet):
    queryset = Deputado.objects.all()
    serializer_class = DeputadoSerializer
    # http_method_names = ["get", "head"]
