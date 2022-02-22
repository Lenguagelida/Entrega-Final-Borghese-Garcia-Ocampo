from django import forms
from .models import Post, Comentario

#Formulario contacto para enviar email
class ContactEmailForm(forms.Form):
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    email_address = forms.EmailField(max_length = 150)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000)

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('contenido',)

class PostForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = ('titulo', 'subtitulo', 'categoria', 'autor', 'contenido', 'imagen')
        
            widgets = {
            'titulo': forms.TextInput(attrs={'placeholder':'Titulo'}),
            'subtitulo': forms.TextInput(attrs={'placeholder':'Subtitulo'}),
            'autor' : forms.TextInput(attrs={'placeholder':'','id':'autor', 'readonly':"readonly" }),
        }
        

