from django.contrib import admin
from .models import Prestamo

@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'libro', 'fecha_prestamo', 'fecha_limite', 'estado']
    list_filter = ['estado']
    search_fields = ['usuario__username', 'libro__titulo']