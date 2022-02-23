#Funcionalidades de los post
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from postApp.models import Post, Comentario
from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from postApp.forms import ComentarioForm, PostForm
from django.core.paginator import Paginator, EmptyPage

#Import para enviar correos
from postApp.forms import ContactEmailForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect

def inicio(request):
    queryset = request.GET.get("buscar")
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(subtitulo__icontains = queryset)
        ).distinct()
        return render(request, 'postApp/inicio.html', {'posts': posts})
    else:
        todosLosPosts = Post.objects.all().order_by('-fecha_publicacion')
        mostrar = Paginator(todosLosPosts, 3)
        pagina_num = request.GET.get('pagina', 1)
        try:
            posts = mostrar.page(pagina_num)
            numeros = "n" * posts.paginator.num_pages
        except EmptyPage:
            posts = mostrar.page(1)
            numeros = "n" * posts.paginator.num_pages
        return render(request, 'postApp/inicio.html', {'posts': posts, 'numeros': numeros})


class ListaPosts(ListView):

    model = Post
    template_name= "postApp/lista_post.html"
    ordering = ['-fecha_publicacion']

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

    model = Post
    form_class= PostForm    
    success_url = "/postApp/postLista"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto.update({
            'tipo_template': 'Publicar'
        })
        return contexto
class UpdatePost(UpdateView):

    model = Post
    form_class= PostForm 
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

def periodismo(request):
    queryset = request.GET.get("buscar")
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(subtitulo__icontains = queryset)
        ).distinct()
        return render(request, 'postApp/inicio.html', {'posts': posts})
    else:
        posts=Post.objects.filter(categoria__nombre = 'Periodismo')
        return render(request,'postApp/categoria_periodismo.html',{'posts':posts})
    
def qatar2022(request):
    queryset = request.GET.get("buscar")
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(subtitulo__icontains = queryset)
        ).distinct()
        return render(request, 'postApp/inicio.html', {'posts': posts})
    else:    
        posts=Post.objects.filter(categoria__nombre = 'Qatar 2022')
        return render(request,'postApp/categoria_periodismo.html',{'posts':posts})

def futbol_argentino(request):
    queryset = request.GET.get("buscar")
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(subtitulo__icontains = queryset)
        ).distinct()
        return render(request, 'postApp/inicio.html', {'posts': posts})
    else:    
        posts=Post.objects.filter(categoria__nombre = 'Futbol Argentino')
        return render(request,'postApp/categoria_periodismo.html',{'posts':posts})

def futbol_internacional(request):
    queryset = request.GET.get("buscar")
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(subtitulo__icontains = queryset)
        ).distinct()
        return render(request, 'postApp/inicio.html', {'posts': posts})
    else:    
        posts=Post.objects.filter(categoria__nombre = 'Futbol Internacional')
        return render(request,'postApp/categoria_periodismo.html',{'posts':posts})

def aboutUs(request):
    return render(request,'postApp/about_us.html')

#Envio de correo desde Contacto
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
            return render(request, "usuariosApp/bienvenido.html", {"mensaje": "Tu correo ha sido enviado con éxito. En al menos 48 horas nuestro equipo de soporte te va a contactar."})

    form = ContactEmailForm()
    return render(request, "postApp/contacto.html", {'form':form})