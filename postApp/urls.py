from django.urls import path
from postApp import views


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('todosLosPosts/', views.todos_los_post, name='todosLosPosts'),
    path('postLista/', views.ListaPosts.as_view(), name='postLista'),
    path('crearPost/', views.CrearPost.as_view(), name='crearPost'),
    path('verPost/<pk>/', views.VerPost.as_view(), name='verPost'),
    path('editarPost/<pk>/', views.UpdatePost.as_view(), name='editarPost'),
    path('borrarPost/<pk>/', views.BorrarPost.as_view(), name='borrarPost'),
    
]