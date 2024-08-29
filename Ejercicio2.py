from datetime import datetime, timedelta

class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.fecha_prestamo = None
        self.fecha_devolucion = None
        self.fecha_limite = None

class Biblioteca:
    def __init__(self):
        self.libros_prestados = {}

    def prestar_libro(self, libro, nombre_persona):
        if libro.titulo in self.libros_prestados:
            print(f"El libro '{libro.titulo}' ya está prestado.")
        else:
            libro.fecha_prestamo = datetime.now()
            libro.fecha_limite = libro.fecha_prestamo + timedelta(days=14)  # Ejemplo: 14 días de préstamo
            self.libros_prestados[libro.titulo] = (nombre_persona, libro)
            print(f"Libro '{libro.titulo}' prestado a {nombre_persona}. Fecha límite de devolución: {libro.fecha_limite.strftime('%d/%m/%Y')}")

    def devolver_libro(self, titulo_libro):
        if titulo_libro in self.libros_prestados:
            nombre_persona, libro = self.libros_prestados[titulo_libro]
            libro.fecha_devolucion = datetime.now()
            if libro.fecha_devolucion > libro.fecha_limite:
                dias_retraso = (libro.fecha_devolucion - libro.fecha_limite).days
                sancion = dias_retraso * 0.50  # 50 centavos por cada día de retraso
                print(f"Libro '{libro.titulo}' devuelto con retraso de {dias_retraso} días. Sanción: ${sancion:.2f}.")
            else:
                print(f"Libro '{libro.titulo}' devuelto a tiempo.")
            del self.libros_prestados[titulo_libro]
        else:
            print(f"El libro '{titulo_libro}' no se encuentra en los registros de préstamos.")

    def mostrar_libros_prestados(self):
        if self.libros_prestados:
            print("\n--- Libros actualmente prestados ---")
            for titulo, (nombre_persona, libro) in self.libros_prestados.items():
                print(f"Título: {libro.titulo}")
                print(f"Prestado a: {nombre_persona}")
                print(f"Fecha de préstamo: {libro.fecha_prestamo.strftime('%d/%m/%Y')}")
                print(f"Fecha límite de devolución: {libro.fecha_limite.strftime('%d/%m/%Y')}")
                print("-----------------------------")
        else:
            print("No hay libros prestados en este momento.")

    def imprimir_registros(self):
        if self.libros_prestados:
            print("\n--- Resumen de todos los préstamos realizados ---")
            for titulo, (nombre_persona, libro) in self.libros_prestados.items():
                print(f"Nombre: {nombre_persona}")
                print(f"Título del libro: {libro.titulo}")
                print(f"Fecha de préstamo: {libro.fecha_prestamo.strftime('%d/%m/%Y')}")
                print(f"Fecha límite de devolución: {libro.fecha_limite.strftime('%d/%m/%Y')}")
                if libro.fecha_devolucion:
                    print(f"Fecha de devolución: {libro.fecha_devolucion.strftime('%d/%m/%Y')}")
                else:
                    print("Fecha de devolución: No devuelto aún")
                print("-----------------------------")
        else:
            print("No hay registros de préstamos para mostrar.")

# Ejemplo interactivo
biblioteca = Biblioteca()

while True:
    print("\n--- Sistema de Préstamos de la Biblioteca ---")
    print("1. Prestar un libro")
    print("2. Devolver un libro")
    print("3. Mostrar libros prestados")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        titulo_libro = input("Ingrese el título del libro: ")
        nombre_persona = input("Ingrese el nombre de la persona que realiza el préstamo: ")
        libro = Libro(titulo_libro)
        biblioteca.prestar_libro(libro, nombre_persona)
    elif opcion == "2":
        titulo_libro = input("Ingrese el título del libro a devolver: ")
        biblioteca.devolver_libro(titulo_libro)
    elif opcion == "3":
        biblioteca.mostrar_libros_prestados()
    elif opcion == "4":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Por favor, intente nuevamente.")

# Imprimir la información de todos los registros al final
print("--------------------------------------------------------------------------")
biblioteca.imprimir_registros()

