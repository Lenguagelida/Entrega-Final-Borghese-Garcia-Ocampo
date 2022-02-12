from django.db import models


class Post(models.Model):
    titulo = models.CharField('titulo', max_length=50, null=False, blank=False)
    subtitulo = models.CharField(
        'subtitulo', max_length=100, null=False, blank=False)
    contenido = models.TextField('contenido', null=False, blank=False)
    imagen = models.ImageField(
        upload_to='imagenes_post', null=True, blank=True)
    # Agrega fecha de origen del post:
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    # Agrega fecha y actualiza segun la fecha de la edicion:
    fecha_edicion = models.DateTimeField(auto_now=True)
    #autor= models.ForeignKey()

    def __str__(self):
        return f'{self.titulo}'
        # - Autor: {self.autor}
    
    def delete(self, *args, **kwargs):
        self.imagen.delete()
        super().delete(args,kwargs)


class Comentario(models.Model):
    #autor= models.ForeignKey()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField('contenido', null=False, blank=False)

    # def __str__(self):
    #    return f'{self.autor}'


class Vistas(models.Model):
    #autor= models.ForeignKey()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #    return f'{self.autor}'


class MeGusta(models.Model):
    #autor= models.ForeignKey()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    # def __str__(self):
    #    return f'{self.autor}'


class NoMeGusta(models.Model):
    #autor= models.ForeignKey()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    # def __str__(self):
    #    return f'{self.autor}'
