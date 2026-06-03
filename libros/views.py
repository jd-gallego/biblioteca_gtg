from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Libro
from .services import LibroService

@login_required
def catalogo_libros(request):
    query = request.GET.get('q', '')
    buscar = request.GET.get('buscar', '')
    libros_api = []

    if query and request.user.es_administrador():
        service = LibroService()
        libros_api = service.buscar_libros(query)

    libros_db = Libro.objects.all()
    if buscar:
        libros_db = libros_db.filter(titulo__icontains=buscar) | libros_db.filter(autor__icontains=buscar)

    return render(request, 'libros/catalogo.html', {
        'libros_api': libros_api,
        'libros_db': libros_db,
        'query': query,
        'buscar': buscar
    })

@login_required
def agregar_libro(request):
    if not request.user.es_administrador():
        return redirect('catalogo_libros')
    if request.method == 'POST':
        try:
            Libro.objects.get_or_create(
                api_id=request.POST.get('api_id'),
                defaults={
                    'titulo': request.POST.get('titulo'),
                    'autor': request.POST.get('autor'),
                    'isbn': request.POST.get('isbn'),
                    'categoria': request.POST.get('categoria'),
                }
            )
            messages.success(request, 'Libro agregado al catálogo.')
        except Exception as e:
            messages.error(request, f'Error al agregar libro: {e}')
    return redirect('catalogo_libros')