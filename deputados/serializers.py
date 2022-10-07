from rest_framework import serializers

from deputados.models import Deputado


class DeputadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deputado
        fields = "__all__"
