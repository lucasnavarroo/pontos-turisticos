from rest_framework.viewsets import ModelViewSet
from .serializers import AvaliacaoSerializer
from avaliacoes.models import Avaliacao

class AvaliacaoViewSet(ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer