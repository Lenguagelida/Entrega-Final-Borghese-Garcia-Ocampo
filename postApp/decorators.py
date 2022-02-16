from ast import NodeVisitor
from tokenize import group
from django.http import HttpResponse
from django.shortcuts import redirect
#from usuariosApp.views import login, login_request

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect ('inicio')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('No estas autorizado para ver esta pagina')
        return wrapper_func
    return decorator


def only_escritor(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        
        if group == 'escritor':
            return HttpResponse('Puedes acceder')
        
        if group == 'lector':
            return HttpResponse('No puedes acceder')
    
    return wrapper_func