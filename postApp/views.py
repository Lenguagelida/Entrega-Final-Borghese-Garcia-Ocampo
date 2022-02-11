from django.shortcuts import render
from postApp.models import Post

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView

def inicio(request):

    return render(request, 'index.html')


def todos_los_post(request):

    posts = Post.objects.all()

    return render(request, 'postApp/todos_los_post.html', {'posts': posts})

class ListaPosts(ListView):

    model = Post
    template_name= "postApp/lista_post.html"

class VerPost(DetailView):
    
    model = Post
    template_name= "postApp/ver_post.html"

class UpdatePost(UpdateView):

    model = Post
    success_url = "postApp/updatePost.html"
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']

class BorrarPost(DeleteView):

    model = Post
    success_url = "/postApp/postLista"

class CrearPost(CreateView):

    model = Post
    success_url = "postApp/post/list"
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']