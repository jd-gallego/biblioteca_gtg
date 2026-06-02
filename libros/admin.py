from django.contrib import admin
from .models import Libro

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'categoria', 'disponible']
    list_filter = ['disponible', 'categoria']
    search_fields = ['titulo', 'autor', 'isbn']