from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework.decorators import action

@method_decorator(cache_page(60), name='dispatch')
class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        queryset = PontoTuristico.objects.all()
        
        if id:
            queryset = PontoTuristico.objects.filter(pk=id)
        if nome:
            queryset =  PontoTuristico.objects.filter(nome__iexact=nome)
        if descricao:
            queryset =  PontoTuristico.objects.filter(descricao__iexact=descricao)

        return queryset

    def list(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet, self).partial_update(request, *args, **kwargs)
    
    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        pass
    
    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass
class PontoTuristicoViewSetBd2(ModelViewSet):
    queryset = PontoTuristico.objects.using('banco2').all()
    serializer_class = PontoTuristicoSerializer

# class HapvidaQueryViewSet(ModelViewSet):
#     queryset = 

# python manage.py migrate --database=banco2