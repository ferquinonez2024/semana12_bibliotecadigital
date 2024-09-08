class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn}) - Categoría: {self.categoria}"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios = set()  # Conjunto para IDs de usuario únicos

    def añadir_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya está en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' añadido a la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print(f"El libro con ISBN {isbn} no existe en la biblioteca.")

    def registrar_usuario(self, nombre, id_usuario):
        if id_usuario in [usuario.id_usuario for usuario in self.usuarios]:
            print(f"El usuario con ID {id_usuario} ya está registrado.")
        else:
            nuevo_usuario = Usuario(nombre, id_usuario)
            self.usuarios.add(nuevo_usuario)
            print(f"Usuario '{nombre}' registrado con ID {id_usuario}.")

    def dar_baja_usuario(self, id_usuario):
        usuario_a_eliminar = next((usuario for usuario in self.usuarios if usuario.id_usuario == id_usuario), None)
        if usuario_a_eliminar:
            self.usuarios.remove(usuario_a_eliminar)
            print(f"Usuario con ID {id_usuario} eliminado.")
        else:
            print(f"El usuario con ID {id_usuario} no está registrado.")

    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros and any(usuario.id_usuario == id_usuario for usuario in self.usuarios):
            libro = self.libros[isbn]
            usuario = next(usuario for usuario in self.usuarios if usuario.id_usuario == id_usuario)
            usuario.prestar_libro(libro)
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
        else:
            print("El libro o el usuario no están registrados.")

    def devolver_libro(self, isbn, id_usuario):
        if isbn in self.libros and any(usuario.id_usuario == id_usuario for usuario in self.usuarios):
            libro = self.libros[isbn]
            usuario = next(usuario for usuario in self.usuarios if usuario.id_usuario == id_usuario)
            usuario.devolver_libro(libro)
            print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
        else:
            print("El libro o el usuario no están registrados.")

    def buscar_libro(self, busqueda):
        resultados = [libro for libro in self.libros.values() if (busqueda.lower() in libro.titulo.lower() or
                                                                   busqueda.lower() in libro.autor.lower() or
                                                                   busqueda.lower() in libro.categoria.lower())]
        if resultados:
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros con esa búsqueda.")

    def listar_libros_prestados(self, id_usuario):
        usuario = next((usuario for usuario in self.usuarios if usuario.id_usuario == id_usuario), None)
        if usuario:
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print(f"El usuario con ID {id_usuario} no está registrado.")


# Ejemplo de uso del sistema

# Crear una biblioteca
biblioteca = Biblioteca()

# Añadir libros
libro1 = Libro("1984", "George Orwell", "Distopía", "123456789")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", "987654321")
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Registrar usuarios
biblioteca.registrar_usuario("Juan Pérez", "u001")
biblioteca.registrar_usuario("Ana Gómez", "u002")

# Prestar libros
biblioteca.prestar_libro("123456789", "u001")

# Listar libros prestados
biblioteca.listar_libros_prestados("u001")

# Buscar libros
biblioteca.buscar_libro("Cien años de soledad")

# Devolver libros
biblioteca.devolver_libro("123456789", "u001")

# Quitar libros
biblioteca.quitar_libro("987654321")

# Dar de baja un usuario
biblioteca.dar_baja_usuario("u002")
