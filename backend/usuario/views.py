from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.serializers import Serializer

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from .models import Usuario, Post
from .serializers import UsuarioSerializer, PostSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class  = UsuarioSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



# def index(request):
#     usuarios = [usuario.nome for usuario in Usuario.objects.all()]
#     return JsonResponse(usuarios, safe=False)