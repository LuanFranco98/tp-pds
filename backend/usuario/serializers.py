from django.db.models import fields
from rest_framework.serializers import ModelSerializer

from .models import Usuario, Post

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha', 'favoritos']
    

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'titulo',
            'conteudo',
            'imagem',
            'criador',
            'categoria',
        ]