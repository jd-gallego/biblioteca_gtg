from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    ROL_CHOICES = [
        ('administrador', 'Administrador'),
        ('lector', 'Lector'),
    ]
    rol = models.CharField(max_length=20, choices=ROL_CHOICES, default='lector')
    documento = models.CharField(max_length=20, unique=True, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.username} - {self.rol}"

    def es_administrador(self):
        return self.rol == 'administrador'

    def es_lector(self):
        return self.rol == 'lector'