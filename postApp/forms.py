from django import forms
from .models import Post

class FormularioPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen']