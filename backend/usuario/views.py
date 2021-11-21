from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class  = UsuarioSerializer


# def index(request):
#     usuarios = [usuario.nome for usuario in Usuario.objects.all()]
#     return JsonResponse(usuarios, safe=False)