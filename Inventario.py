from Producto import Producto

# Clase Inventario
class Inventario:
    def __init__(self):
        self.__productos = []

    # Metodo buscar_producto
    def buscar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre().lower() == nombre.lower():
                return producto
        return None 

    # Metodo de agregar_producto
    def agregar_producto(self, producto):
        if self.buscar_producto(producto.get_nombre()) is None:
            self.__productos.append(producto)
            print(f"Producto {producto.get_nombre()} agregado al inventario.")
        else:
            print(f"El producto {producto.get_nombre()} ya existe en el inventario.")
    
    # Metodo para pedir los datos del Producto
    def datos_producto(self):
        nombre = input("Nombre del Producto: ")
        categoria = input("Categoria del Producto: ")
        try:
            precio = float(input("Precio del Producto: "))
            cantidad = int(input("Cantidad del Producto: "))
            producto = Producto(nombre, categoria, precio, cantidad)
            self.agregar_producto(producto)
        except ValueError:
            print("Error: Por favor ingresa un precio y cantidad válidos.") 

    # Metodo de eliminar_producto
    def eliminar_producto(self, nombre):
        producto = self.buscar_producto(nombre)
        if producto:
            self.__productos.remove(producto)
            print(f"Producto {producto.get_nombre()} eliminado del inventario.")
        else:
            print(f"El producto {nombre} no se encuentra en el inventario.")

    # Metodo actualizar_producto
    def actualizar_producto(self, nombre, precio=None, cantidad=None):
        producto = self.buscar_producto(nombre)
        if producto:
            try:
                if precio is not None:
                    producto.set_precio(precio)
                    print(f"Precio de {nombre} actualizado a {precio}.")
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                    print(f"Cantidad de {nombre} actualizada a {cantidad}.")
            except ValueError as e:
                print(f"Error al actualizar el producto: {e}")
        else:
            print(f"El producto {nombre} no se encuentra en el inventario.")

    # Este método solo mostrará el menú de opciones, sin hacer nada más.
    def mostrar_menu_actualizacion(self):
        print("-" * 30)
        print("""
¿Qué dato quieres actualizar del Producto?
1. Precio
2. Cantidad
3. Ambos
0. Regresar
""".strip())
        print("-" * 30)

    # Método para actualizar los datos de un producto
    def dato_a_actualizar(self):
        while True:
            self.mostrar_menu_actualizacion() 

            try:
                opcion = int(input("¿Qué acción quieres realizar?: "))
                if opcion == 0:
                    print("Cancelando Cambios...")
                    return  # Salir del ciclo y regresar al menú principal
                nombre = input("Nombre del Producto: ")
                
                if opcion == 1:
                    nuevo_precio = float(input("Nuevo Precio del Producto: "))
                    self.actualizar_producto(nombre, precio=nuevo_precio)
                elif opcion == 2:
                    nueva_cantidad = int(input("Nueva Cantidad del Producto: "))
                    self.actualizar_producto(nombre, cantidad=nueva_cantidad)
                elif opcion == 3:
                    nuevo_precio = float(input("Nuevo Precio del Producto: "))
                    nueva_cantidad = int(input("Nueva Cantidad del Producto: "))
                    self.actualizar_producto(nombre, precio=nuevo_precio, cantidad=nueva_cantidad)
                else:
                    print("Opción no válida. Por favor, elige una opción correcta.")
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número")

    # Metodo mostrar_inventario
    def mostrar_inventario(self):
        if self.__productos:
            print("Inventario: ")
            for producto in self.__productos:
                print(producto)
        else:
            print("No hay productos en el inventario.")
