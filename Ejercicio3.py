from datetime import datetime

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Venta:
    def __init__(self):
        self.productos = []
        self.total = 0

    def agregar_producto(self, producto, cantidad):
        self.productos.append((producto, cantidad))
        self.total += producto.precio * cantidad

    def mostrar_detalles(self):
        print("-----------------------------------------------------------")
        print("\n--- Detalles de la Venta ---")
        for producto, cantidad in self.productos:
            print(f"Producto: {producto.nombre}, Cantidad: {cantidad}, Precio Unitario: ${producto.precio:.2f}")
        print(f"Total a pagar: ${self.total:.2f}")

    def calcular_vuelto(self, monto_pagado):
        if monto_pagado < self.total:
            print("Monto insuficiente para cubrir la venta.")
            return 0
        return monto_pagado - self.total

class Tienda:
    def __init__(self):
        self.proveedores = []

    def registrar_venta(self):
        venta = Venta()
        
        print("\n--- Registro de Venta ---")
        while True:
            nombre_producto = input("Ingrese el nombre del producto (o presione Enter para terminar): ")
            if nombre_producto == "":
                break
            cantidad = int(input(f"Ingrese la cantidad de {nombre_producto}: "))
            precio = float(input(f"Ingrese el precio unitario de {nombre_producto}: "))
            producto = Producto(nombre_producto, precio)
            venta.agregar_producto(producto, cantidad)
        venta.mostrar_detalles()
        monto_pagado = float(input("Ingrese el monto pagado por el cliente: "))
        vuelto = venta.calcular_vuelto(monto_pagado)
        print(f"Vuelto a entregar: ${vuelto:.2f}")

    def registrar_proveedor(self):
        nombre_proveedor = input("Ingrese el nombre del proveedor: ")
        nombre_producto = input("Ingrese el nombre del producto entregado: ")
        precio_sugerido = float(input(f"Ingrese el precio sugerido para {nombre_producto}: "))
        producto = Producto(nombre_producto, precio_sugerido)
        self.proveedores.append((nombre_proveedor, producto))
        print(f"Producto '{nombre_producto}' registrado con precio sugerido de ${precio_sugerido:.2f}.")

    def mostrar_proveedores(self):
        if self.proveedores:
            print("\n--- Detalles de Proveedores ---")
            for proveedor, producto in self.proveedores:
                print(f"Proveedor: {proveedor}")
                print(f"Producto: {producto.nombre}, Precio Sugerido: ${producto.precio:.2f}")
                print("-----------------------------")
              
        else:
            print("No hay proveedores registrados.")

# Ejemplo interactivo
tienda = Tienda()

while True:
    print("\n--- Sistema de Gestión de la Tienda ---")
    print("1. Registrar venta")
    print("2. Registrar proveedor")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        tienda.registrar_venta()
    elif opcion == "2":
        tienda.registrar_proveedor()
    elif opcion == "3":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Por favor, intente nuevamente.")


print("-----------------------------------------------------------")


