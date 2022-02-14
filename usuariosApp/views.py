import django
from django.shortcuts import redirect, render
from django.db.models import Q


# Para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from usuariosApp.forms import UserRegisterForm, UserEditForm
from postApp.models import Post


# login_required(login_url='login')

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

# Register
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()

            return render(request, 'usuariosApp/bienvenido.html', {"mensaje": f"El usuario de {username} se ha creado con éxito"})

        else:

            return render(request, 'usuariosApp/bienvenido.html', {"mensaje": "El usuario no se ha creado"})

    else:

        form = UserRegisterForm()
        return render(request, 'usuariosApp/registro.html', {"form": form})


# Login
def login_request(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        if request.method == "POST":

            form = AuthenticationForm(request, data=request.POST)

            if form.is_valid():

                data = form.cleaned_data

                user = authenticate(
                    username=data['username'], password=data['password'])

                if user is not None:

                    login(request, user)

                    # return redirect ('inicio2.html')

                    return render(request, "usuariosApp/bienvenido.html", {"mensaje": f"Bienvenido {user.get_username()}"})

                else:

                    return render(request, "usuariosApp/login.html", {"mensaje": "Datos incorrectos"})

            else:

                return render(request, "usuariosApp/login.html", {"mensaje": "Error en el formulario"})

        form = AuthenticationForm()

        return render(request, "usuariosApp/login.html", {'form': form})


def editarPerfil(request):

    # Instancia del login
    usuario = request.user

    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():  # Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            # Datos que se modificarán
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            usuario.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "usuariosApp/bienvenido.html", {"mensaje": "Datos de perfil modificados correctamente"})
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = UserEditForm(initial={
                                    'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name})

    # Voy al html que me permite editar
    return render(request, "usuariosApp/editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})


# logout
# def logout_request(request):
#     logout(request)
#     return redirect('login')
