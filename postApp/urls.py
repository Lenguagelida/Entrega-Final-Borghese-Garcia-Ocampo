from django.urls import path
from postApp import views


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('aboutUs/', views.aboutUs, name='AboutUs'),
    path('postLista/', views.ListaPosts.as_view(), name='postLista'),
    path('verPost/<pk>/', views.VerPost.as_view(), name='verPost'),
    path('crearPost/', views.CrearPost.as_view(), name='crearPost'),
    path('editarPost/<pk>/', views.UpdatePost.as_view(), name='editarPost'),
    path('borrarPost/<pk>/', views.BorrarPost.as_view(), name='borrarPost'),
    path('contacto/',views.contact, name='Contacto'),
    # path('buscar',views.buscar, name='buscar'),
    
]