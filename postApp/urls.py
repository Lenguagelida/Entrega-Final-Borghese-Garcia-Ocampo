from django.urls import path
from postApp import views


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('todosLosPosts/', views.todos_los_post, name='todosLosPosts'),
]