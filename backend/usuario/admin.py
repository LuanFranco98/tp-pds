from django.contrib import admin

# Register your models here.

from .models import Usuario, Post, Categoria

admin.site.register(Usuario)
admin.site.register(Post)
admin.site.register(Categoria)
