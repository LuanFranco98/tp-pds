from django.contrib import admin

# Register your models here.

from .models import Usuario, Post, Categoria, Comentario

admin.site.register(Usuario)
admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(Comentario)
