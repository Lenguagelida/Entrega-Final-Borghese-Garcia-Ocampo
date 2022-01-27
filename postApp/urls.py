from django.urls import path
from postApp import views


urlpatterns = [
    path('', views.inicio, name="inicio"),
]