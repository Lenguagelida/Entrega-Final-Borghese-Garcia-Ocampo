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
    path('verPost/<pk>/comentar/',views.AgregarComentario.as_view(), name='comentar'),
    path('like/<pk>', views.meGusta, name='likePost'),
    path('contacto/',views.contact, name='Contacto'),
    path('periodismo/',views.periodismo,name='CategoriaPeriodismo'),
    path('qatar2022/',views.qatar2022,name='Qatar2022'),
    path('futbolargentino/',views.futbol_argentino,name='Futbolargentino'),
    path('futbolinternacional/',views.futbol_internacional,name='Futbolinternacional'),
]