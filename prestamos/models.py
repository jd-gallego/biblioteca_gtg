from django.db import models
from django.conf import settings
from libros.models import Libro

class Prestamo(models.Model):
    ESTADOS = [
        ('activo', 'Activo'),
        ('devuelto', 'Devuelto'),
    ]
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='prestamos')
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='prestamos')
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    fecha_devolucion = models.DateTimeField(null=True, blank=True)
    fecha_limite = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='activo')

    def __str__(self):
        return f"{self.usuario.username} - {self.libro.titulo} ({self.estado})"

    def devolver(self):
        from django.utils import timezone
        self.estado = 'devuelto'
        self.fecha_devolucion = timezone.now()
        self.libro.marcar_disponible()
        self.save()

    def esta_vencido(self):
        from django.utils import timezone
        return self.estado == 'activo' and timezone.now() > self.fecha_limite