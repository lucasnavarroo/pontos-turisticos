from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

@method_decorator(cache_page(60), name='dispatch')
class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

class PontoTuristicoViewSetBd2(ModelViewSet):
    queryset = PontoTuristico.objects.using('banco2').all()
    serializer_class = PontoTuristicoSerializer

# class HapvidaQueryViewSet(ModelViewSet):
#     queryset = 

# python manage.py migrate --database=banco2