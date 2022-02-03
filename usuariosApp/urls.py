from telnetlib import LOGOUT
from django.urls import path
from usuariosApp import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio, name ="inicio"),
    path('login', views.login_request, name ="Login"),
    path('register', views.register, name ="Register"),
    path('logout', LogoutView.as_view(template_name='usuariosApp/logout.html'), name ="Logout"),
]