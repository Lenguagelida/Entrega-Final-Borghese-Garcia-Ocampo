from django.urls import path
from postApp import views


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('todosLosPosts/', views.todos_los_post, name='todosLosPosts'),
    path('postlista', views.ListaPosts.as_view(), name='postlista'),
    path('about',views.aboutUs,name='AboutUs'),
]