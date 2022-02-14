from django.shortcuts import render
from postApp.models import Post,Categoria
from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
#from postApp.forms import FormularioPost

def inicio(request):
    queryset = request.GET.get("buscar")
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(subtitulo__icontains = queryset) |
            Q(contenido__icontains = queryset)
        ).distinct()
        return render(request,'postApp/inicio.html',{'posts':posts})
    else:
        posts = Post.objects.all().order_by('-fecha_publicacion')
        return render(request, 'postApp/inicio.html', {'posts': posts})


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

def buscar(request):
    queryset = request.GET.get("buscar")
    # print(queryset)
    posts = Post.objects.filter(estado = True)
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(subtitulo__icontains = queryset) |
            Q(contenido__icontains = queryset)
        ).distinct()
    return render(request,'postApp/inicio.html',{'posts':posts})