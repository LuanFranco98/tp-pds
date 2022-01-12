from django.test import TestCase
from usuario.models import *
# Create your tests here.


class TestBackend(TestCase):
    def setUp(self) -> None:
        user1 =Usuario.objects.create(nome="Admin",
                                email="admin@admin.com",
                                senha="admin")
        
        Usuario.objects.create(nome="Admin2",
                                email="admin2@admin.com",
                                senha="admin2")

        categoria1 = Categoria.objects.create(nome="Categoria1")
        
        Categoria.objects.create(nome="Categoria2")

        post1 = Post.objects.create(titulo="TituloPost1",
                                conteudo="ConteudoPost1",
                                imagem="linkImagem1",
                                criador=user1
        )

        post1.categorias.add(categoria1)

        
        Comentario.objects.create(criador=user1,
                            comentario="comentario1",
                            post=post1)        

    def test_usuario(self):
        usuario = Usuario.objects.get(id=1)
        informacoes_esperadas = ["Admin","admin@admin.com", "admin"]
        informacoes_usuario = [usuario.nome, usuario.email, usuario.senha]
        self.assertEqual(informacoes_usuario, informacoes_esperadas)

    def test_categoria(self):
        categoria = Categoria.objects.get(id=1)
        self.assertEqual(categoria.nome, "Categoria1")

    def test_post(self):
        post = Post.objects.get(id=1)
        criador = Usuario.objects.get(id=1)

        informacoes_esperadas = ["TituloPost1", "ConteudoPost1", "linkImagem1", criador]
        informacoes_post = [post.titulo, post.conteudo, post.imagem, post.criador]
        self.assertEqual(informacoes_esperadas, informacoes_post)

    def test_comentario(self):
        comentario = Comentario.objects.get(id=1)
        self.assertEqual(comentario.comentario, "comentario1")
    
    def test_vinculacao_comentario(self):
        comentario = Comentario.objects.get(id=1)
        post = Post.objects.get(id=1)
        self.assertIn(comentario, post.comentarios.all())
    
    def test_vinculacao_categoria(self):
        categoria = Categoria.objects.get(id=1)
        post = Post.objects.get(id=1)
        self.assertIn(categoria, post.categorias.all())