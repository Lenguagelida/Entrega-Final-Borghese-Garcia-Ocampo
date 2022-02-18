#Funcionalidades de los post
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from postApp.models import Post,Categoria, Comentario
from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from postApp.forms import ComentarioForm

#Import para enviar correos
from postApp.forms import ContactEmailForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect

#Decorators
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, only_escritor


def inicio(request):
    posts = Post.objects.all().order_by('-fecha_publicacion')
    return render(request, 'postApp/inicio.html', {'posts': posts})


class ListaPosts(ListView):

    model = Post
    template_name= "postApp/lista_post.html"

class VerPost(DetailView):
    
    model = Post
    template_name= "postApp/ver_post.html"

    def get_context_data(self,*args, **kwargs):
        contexto= super(VerPost, self).get_context_data(*args, **kwargs)
        numero = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = numero.total_likes()
        contexto['total_likes']= total_likes
        return contexto

class CrearPost(CreateView):
    
    #form_class= FormularioPost
    model = Post
    fields = ['titulo', 'subtitulo', 'categoria', 'autor', 'contenido', 'imagen']
    success_url = "/postApp/postLista"

#allowed_users(allowed_roles=['lectores'])
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

class AgregarComentario(CreateView):
    
    model = Comentario
    form_class = ComentarioForm
    template_name = "postApp/comentario_form.html"

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
    success_url = "/"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto.update({
            'tipo_template': 'Comentar'
        })
        return contexto


def meGusta(request,pk):
        post = get_object_or_404(Post, id=request.POST.get('post_id'))
        post.likes.add(request.user)
        return HttpResponseRedirect(reverse('verPost', args=pk))

#NO ANDA
#def buscar(request):
#    if request.method == "POST":
#        campo = request.POST['buscar']
#        posts = Post.objects.filter(titulo__contains=campo)
#        return render(request,'postApp/resultados_busqueda.html',{'campo': campo},{'posts':posts})
#    else:
#        return render(request,'postApp/resultados_busqueda.html',{'campo': campo},{'posts':posts})


def periodismo(request):
    posts=Post.objects.filter(categoria__nombre = 'Periodismo')
    return render(request,'postApp/categoria_periodismo.html',{'posts':posts})
    
def qatar2022(request):
    posts=Post.objects.filter(categoria__nombre = 'Qatar 2022')
    return render(request,'postApp/categoria_periodismo.html',{'posts':posts})

def futbol_argentino(request):
    posts=Post.objects.filter(categoria__nombre = 'Futbol Argentino')
    return render(request,'postApp/categoria_periodismo.html',{'posts':posts})

def futbol_internacional(request):
    posts=Post.objects.filter(categoria__nombre = 'Futbol Internacional')
    return render(request,'postApp/categoria_periodismo.html',{'posts':posts})

def aboutUs(request):
    return render(request,'postApp/about_us.html')

#Envio de correo desde Contacto
#allowed_users(allowed_roles=['lectores'])
def contact(request):
    if request.method == 'POST':
        form = ContactEmailForm(request.POST)
        if form.is_valid():
            subject = "Tienes una nueva consulta desde el blog Tercer Tiempo" 
            body = {
            'first_name': form.cleaned_data['first_name'], 
            'last_name': form.cleaned_data['last_name'], 
            'email': form.cleaned_data['email_address'], 
            'message':form.cleaned_data['message'], 
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'blogtercertiempo2022@gmail.com', ['blogtercertiempo2022@gmail.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse('Tu correo ha sido enviado con éxito. En al menos 48 horas nuestro equipo de soporte te va a contactar.')

    form = ContactEmailForm()
    return render(request, "postApp/contacto.html", {'form':form})