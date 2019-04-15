from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Avaliacao

class AvaliacaoSerializer(ModelSerializer):
    model = Avaliacao
    fields = [ 'id', 'user', 'comentario', 'nota', 'data']