from django.contrib import admin

from postApp.models import Categoria, Comentario, MeGusta, NoMeGusta, Post, Vistas

admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(Comentario)
admin.site.register(Vistas)
admin.site.register(MeGusta)
admin.site.register(NoMeGusta)