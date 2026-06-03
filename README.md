# 📚 Biblioteca GTG

Sistema de gestión de biblioteca desarrollado en Python con Django.

## Integrantes
- Jhon Stiven Garcia, Juan Sebastian Trujillo, Julian David Gallego.

## Descripción
Aplicación web que permite gestionar el inventario de libros y usuarios de una biblioteca.
Integra una API externa (Open Library) para consultar el catálogo de libros disponibles.

## Módulos
- **Módulo de ingreso:** Login y registro de usuarios con roles
- **Módulo de préstamos:** Solicitud y devolución de libros
- **Módulo de gestión de usuarios:** Administración de usuarios (solo admin)
- **Módulo de gestión de libros:** Catálogo con búsqueda en API externa

## Tecnologías
- Python 3.13
- Django 6.0
- SQLite
- Bootstrap 5
- API: Open Library (https://openlibrary.org)

## Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/jd-gallego/biblioteca_gtg.git
cd biblioteca_gtg
```

### 2. Crear y activar el entorno virtual
```bash
python -m venv venv
source venv/Scripts/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Hacer las migraciones
```bash
python manage.py migrate
```

### 5. Correr el servidor
```bash
python manage.py runserver
```

Abre el navegador en `http://127.0.0.1:8000`

## Credenciales de prueba
- Registro disponible desde la pantalla de login
- Clave del sistema para administradores: `biblioteca2026`

## Pruebas unitarias
```bash
pytest tests/ -v
```

## Estructura del proyecto
```
biblioteca_gtg/
├── usuarios/        # Módulo de usuarios y autenticación
├── libros/          # Módulo de libros y consumo de API
├── prestamos/       # Módulo de préstamos
├── templates/       # HTML de las vistas
├── tests/           # Pruebas unitarias
├── requirements.txt
└── README.md
```