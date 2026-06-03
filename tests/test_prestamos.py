import pytest
from libros.services import LibroService

class TestLibroService:

    def test_buscar_libros_retorna_lista(self):
        service = LibroService()
        resultado = service.buscar_libros("python")
        assert isinstance(resultado, list)

    def test_buscar_libros_resultado_tiene_campos(self):
        service = LibroService()
        resultado = service.buscar_libros("django")
        if resultado:
            assert "titulo" in resultado[0]
            assert "autor" in resultado[0]
            assert "api_id" in resultado[0]

    def test_buscar_libros_query_vacia_retorna_lista(self):
        service = LibroService()
        resultado = service.buscar_libros("")
        assert isinstance(resultado, list)

    def test_buscar_por_autor_retorna_lista(self):
        service = LibroService()
        resultado = service.buscar_por_autor("Borges")
        assert isinstance(resultado, list)

    def test_buscar_libros_query_invalida(self):
        service = LibroService()
        resultado = service.buscar_libros("xyzxyzxyz123456789abc")
        assert isinstance(resultado, list)