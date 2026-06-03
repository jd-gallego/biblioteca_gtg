from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Usuario

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.activo:
                login(request, user)
                if user.es_administrador():
                    return redirect('admin_dashboard')
                return redirect('catalogo_libros')
            else:
                messages.error(request, 'Tu cuenta está desactivada.')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'usuarios/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def admin_dashboard(request):
    if not request.user.es_administrador():
        return redirect('catalogo_libros')
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/admin_dashboard.html', {'usuarios': usuarios})

CLAVE_ADMIN = "biblioteca2026"

def registro_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        documento = request.POST.get('documento')
        telefono = request.POST.get('telefono')
        rol = request.POST.get('rol', 'lector')
        clave_admin = request.POST.get('clave_admin', '')

        if rol == 'administrador' and clave_admin != CLAVE_ADMIN:
            messages.error(request, 'La clave de administrador es incorrecta.')
            return render(request, 'usuarios/registro.html')

        if Usuario.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe.')
            return render(request, 'usuarios/registro.html')

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'El correo ya está registrado.')
            return render(request, 'usuarios/registro.html')

        usuario = Usuario.objects.create_user(
            username=username,
            email=email,
            password=password,
            documento=documento,
            telefono=telefono,
            rol=rol
        )
        messages.success(request, 'Usuario registrado correctamente.')
        return redirect('login')
    return render(request, 'usuarios/registro.html')

@login_required
def toggle_usuario(request, usuario_id):
    if not request.user.es_administrador():
        return redirect('catalogo_libros')
    try:
        usuario = Usuario.objects.get(id=usuario_id)
        usuario.activo = not usuario.activo
        usuario.save()
        estado = 'activado' if usuario.activo else 'desactivado'
        messages.success(request, f'Usuario {usuario.username} {estado} correctamente.')
    except Usuario.DoesNotExist:
        messages.error(request, 'Usuario no encontrado.')
    return redirect('admin_dashboard')