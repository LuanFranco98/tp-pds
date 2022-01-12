from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.serializers import Serializer

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from .models import Categoria, Usuario, Post, Comentario
from .serializers import CategoriaSerializer, UsuarioSerializer, PostSerializer,  ComentarioSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class  = UsuarioSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer




# def index(request):
#     usuarios = [usuario.nome for usuario in Usuario.objects.all()]
#     return JsonResponse(usuarios, safe=False)