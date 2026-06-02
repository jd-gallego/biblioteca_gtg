from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20, null=True, blank=True)
    categoria = models.CharField(max_length=100, null=True, blank=True)
    api_id = models.CharField(max_length=100, unique=True)
    disponible = models.BooleanField(default=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

    def marcar_prestado(self):
        self.disponible = False
        self.save()

    def marcar_disponible(self):
        self.disponible = True
        self.save()