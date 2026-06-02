from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from .models import Prestamo
from libros.models import Libro

@login_required
def mis_prestamos(request):
    prestamos = Prestamo.objects.filter(usuario=request.user)
    return render(request, 'prestamos/mis_prestamos.html', {'prestamos': prestamos})

@login_required
def todos_prestamos(request):
    if not request.user.es_administrador():
        return redirect('mis_prestamos')
    prestamos = Prestamo.objects.all()
    return render(request, 'prestamos/todos_prestamos.html', {'prestamos': prestamos})

@login_required
def solicitar_prestamo(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if not libro.disponible:
        messages.error(request, 'Este libro no está disponible.')
        return redirect('catalogo_libros')
    try:
        Prestamo.objects.create(
            usuario=request.user,
            libro=libro,
            fecha_limite=timezone.now() + timedelta(days=15)
        )
        libro.marcar_prestado()
        messages.success(request, f'Préstamo de "{libro.titulo}" registrado correctamente.')
    except Exception as e:
        messages.error(request, f'Error al registrar préstamo: {e}')
    return redirect('mis_prestamos')

@login_required
def devolver_libro(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, id=prestamo_id, usuario=request.user)
    prestamo.devolver()
    messages.success(request, f'Libro "{prestamo.libro.titulo}" devuelto correctamente.')
    return redirect('mis_prestamos')