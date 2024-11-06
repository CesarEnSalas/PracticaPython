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

    # Metodo de eliminar_producto
    def eliminar_producto(self, nombre):
      producto = self.buscar_producto(nombre)
      if producto:
        if producto is not None:
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
            print(f"Error al actualizar el producto {e}")
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