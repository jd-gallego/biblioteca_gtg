import requests

class LibroService:
    BASE_URL = "https://openlibrary.org/search.json"

    def buscar_libros(self, query: str) -> list:
        try:
            response = requests.get(self.BASE_URL, params={"q": query, "limit": 10})
            response.raise_for_status()
            data = response.json()
            libros = []
            for doc in data.get("docs", []):
                libros.append({
                    "api_id": doc.get("key", ""),
                    "titulo": doc.get("title", "Sin título"),
                    "autor": ", ".join(doc.get("author_name", ["Desconocido"])),
                    "isbn": doc.get("isbn", [None])[0] if doc.get("isbn") else None,
                    "categoria": doc.get("subject", [None])[0] if doc.get("subject") else None,
                })
            return libros
        except requests.RequestException as e:
            print(f"Error al consultar API: {e}")
            return []

    def buscar_por_titulo(self, titulo: str) -> list:
        return self.buscar_libros(titulo)

    def buscar_por_autor(self, autor: str) -> list:
        try:
            response = requests.get(self.BASE_URL, params={"author": autor, "limit": 10})
            response.raise_for_status()
            data = response.json()
            libros = []
            for doc in data.get("docs", []):
                libros.append({
                    "api_id": doc.get("key", ""),
                    "titulo": doc.get("title", "Sin título"),
                    "autor": ", ".join(doc.get("author_name", ["Desconocido"])),
                    "isbn": doc.get("isbn", [None])[0] if doc.get("isbn") else None,
                    "categoria": doc.get("subject", [None])[0] if doc.get("subject") else None,
                })
            return libros
        except requests.RequestException as e:
            print(f"Error al consultar API: {e}")
            return []