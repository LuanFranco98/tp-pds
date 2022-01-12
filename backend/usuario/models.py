from django.db import models

# Create your models here.


class Usuario(models.Model):
    nome = models.CharField(max_length=140)
    email = models.EmailField(max_length=254)
    senha = models.CharField(max_length=140)
    favoritos = models.ManyToManyField('Post', blank=True)

    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=140)
    posts = models.ManyToManyField('Post', blank=True)
    def __str__(self):
        return self.nome    

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    conteudo = models.TextField()
    imagem = models.CharField(max_length=1000, blank=True, null=True)
    criador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria, through=Categoria.posts.through, blank=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    criador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comentario = models.TextField()
    post = models.ForeignKey(Post, related_name='comentarios', on_delete=models.CASCADE)
