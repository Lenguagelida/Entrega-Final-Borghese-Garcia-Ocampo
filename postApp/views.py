from django.shortcuts import render
from postApp.models import Post


def inicio(request):

    return render(request, 'postApp/inicio.html')


def todos_los_post(request):

    posts = Post.objects.all()

    return render(request, 'postApp/todos_los_post.html', {'posts': posts})
