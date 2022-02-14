from django.shortcuts import render
from postApp.models import Post

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
#from postApp.forms import FormularioPost

def inicio(request):

    return render(request, 'postApp/inicio.html')


def todos_los_post(request):

    posts = Post.objects.all().order_by('-fecha_publicacion')

    return render(request, 'postApp/todos_los_post.html', {'posts': posts})

class ListaPosts(ListView):

    model = Post
    template_name= "postApp/lista_post.html"

class VerPost(DetailView):
    
    model = Post
    template_name= "postApp/ver_post.html"

class CrearPost(CreateView):
    
    #form_class= FormularioPost
    model = Post
    fields = ['titulo', 'subtitulo', 'categoria', 'autor', 'contenido', 'imagen']
    success_url = "/postApp/postLista"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto.update({
            'tipo_template': 'Publicar'
        })
        return contexto
class UpdatePost(UpdateView):

    #form_class= FormularioPost
    model = Post
    fields = ['titulo', 'subtitulo', 'categoria', 'autor', 'contenido', 'imagen']
    success_url = "/postApp/postLista"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto.update({
            'tipo_template': 'Editar' 
        })
        return contexto
class BorrarPost(DeleteView):

    model = Post
    success_url = "/postApp/postLista"

def aboutUs(request):
    return render(request,'postApp/about_us.html')

def contacto(request):
    return render(request,'postApp/contacto.html')