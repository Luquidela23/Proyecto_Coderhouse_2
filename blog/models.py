from django.db import models
from django.contrib.auth.models import User

class Articulo(models.Model):
    titulo = models.CharField(max_length=255)
    subtitulo = models.CharField(max_length=255, blank=True, null=True)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
