from django.contrib import admin

from postApp.models import Categoria, Comentario, Post

admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(Comentario)
