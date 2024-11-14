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
    def agregar_producto(self):
        nombre = input("Nombre del Producto: ")
        categoria = input("Categoria del Producto: ")
        try:
            precio = float(input("Precio del Producto: "))
            cantidad = int(input("Cantidad del Producto: "))
            producto = Producto(nombre, categoria, precio, cantidad)
            if self.buscar_producto(producto.get_nombre()) is None:
                self.__productos.append(producto)
                print(f"Producto {producto.get_nombre()} agregado al inventario.")
            else:
                print(f"El producto {producto.get_nombre()} ya existe en el inventario.")
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
    def actualizar_producto(self):
        nombre = input("Nombre del Producto: ")
        producto = self.buscar_producto(nombre)
    
        if producto:
            # Actualizar precio
            precio_input = input("Nuevo Precio del Producto (deja vacío para no cambiarlo): ")
            if precio_input:  # Si no está vacío
                try:
                    precio = float(precio_input)
                    producto.set_precio(precio)
                    print(f"Precio de {nombre} actualizado a {precio}.")
                except ValueError:
                    print("Error: El precio ingresado no es válido.")
            else:
                print("No se actualizó el precio del producto.")
        
            # Actualizar cantidad
            cantidad_input = input("Nueva Cantidad del Producto (deja vacío para no cambiarla): ")
            if cantidad_input:  # Si no está vacío
                try:
                    cantidad = int(cantidad_input)
                    producto.set_cantidad(cantidad)
                    print(f"Cantidad de {nombre} actualizada a {cantidad}.")
                except ValueError:
                    print("Error: La cantidad ingresada no es válida.")
            else:
                print("No se actualizó la cantidad del producto.")
            
        else:
            print(f"El producto {nombre} no se encuentra en el inventario.")

    # Metodo mostrar_inventario
    def mostrar_inventario(self):
        if self.__productos:
            print("Inventario: ")
            for producto in self.__productos:
                print(producto)
        else:
            print("No hay productos en el inventario.")
