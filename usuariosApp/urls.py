from django.urls import path
from usuariosApp import views


urlpatterns = [
    path('', views.inicio, name="inicio"),
]