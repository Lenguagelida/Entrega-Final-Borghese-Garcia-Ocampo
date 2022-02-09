import django
from django.shortcuts import redirect, render


#Para el login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


#login_required(login_url='login')

def inicio(request):

    return render(request, "usuariosApp/inicio.html")


#Register
def register(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:

        if request.method == "POST":

            form = CreateUserForm(data=request.POST)

            if form.is_valid():

                username = form.cleaned_data['username']
                form.save()
                return render (request, "usuariosApp/login.html", {"mensaje":"Usuario creado con Éxito"})

        else:

            form = CreateUserForm()

            return render (request, "usuariosApp/registro.html" , {"form":form})


#Login
def login_request(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        if request.method == "POST":
                
            form = AuthenticationForm(request, data=request.POST)

            if form.is_valid():

                data = form.cleaned_data

                user = authenticate(username=data['username'], password=data['password'])

                if user is not None:

                    login(request, user)

                        #return redirect ('inicio2.html')

                    return render (request, "usuariosApp/inicio2.html", {"mensaje":f"Bienvenido {user.get_username()}"})
                    
                else:

                    return render (request, "usuariosApp/login.html", {"mensaje":"Datos incorrectos"})
                
            else:

                return render (request, "usuariosApp/login.html", {"mensaje":"Error en el formulario"})
            
        form = AuthenticationForm()

        return render (request,"usuariosApp/login.html", {'form':form})




#logout
# def logout_request(request):
#     logout(request)
#     return redirect('login')