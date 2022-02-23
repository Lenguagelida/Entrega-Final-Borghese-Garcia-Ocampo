from django.shortcuts import redirect, render
# Para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from usuariosApp.forms import UserRegisterForm, UserEditForm
from postApp.models import Post
from django.contrib.auth.models import Group

# Register
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            group = Group.objects.get(name='Comunidad')
            user = form.save()
            user.groups.add(group)
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


def postsConMeGustaPropios(request):
    current_user = request.user.id
    posts = Post.objects.filter(likes__id=current_user)
    return render(request, 'usuariosApp/posts_con_megusta.html', {"posts": posts})
