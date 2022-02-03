from django.shortcuts import render


#Para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate



def inicio(request):

    return render(request, "usuariosApp/inicio.html")


#Login
def login_request(request):

    if request.method == "POST":
        
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            data = form.cleaned_data

            user = authenticate(username=data['username'], password=data['password'])

            if user is not None:

                login(request, user)

                return render (request, "usuariosApp/inicio2.html", {"mensaje":f"Bienvenido {user.get_username()}"})
            
            else:

                return render (request, "usuariosApp/inicio2.html", {"mensaje":"Datos incorrectos"})
        
        else:

                return render (request, "usuariosApp/inicio2.html", {"mensaje":"Error en el formulario"})
    
    form = AuthenticationForm()

    return render (request,"usuariosApp/login.html", {'form':form})

#Register
def register(request):

    if request.method == "POST":

        form = UserCreationForm(data=request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()

            return render (request, "usuariosApp/inicio2.html", {"mensaje":"Usuario creado con Éxito"})

    else:

        form = UserCreationForm()

    return render (request, "usuariosApp/registro.html" , {"form":form})