# Clase Producto
class Producto:
  def __init__(self, nombre, categoria, precio, cantidad):
    self.__nombre = nombre
    self.__categoria = categoria
    self.set_precio(precio)
    self.set_cantidad(cantidad)

  # Getters
  def get_nombre(self):
    return self.__nombre
  
  def get_categorio(self):
    return self.__categoria
  
  def get_precio(self):
    return self.__precio
  
  def get_cantidad(self):
    return self.__cantidad
  
  # Setters
  def set_precio(self, precio):
    if precio > 0:
      self.__precio = precio
    else:
      raise ValueError("El precio debe ser mayor a 0")
  
  def set_cantidad(self, cantidad):
    if cantidad >= 0:
      self.__cantidad = cantidad
    else:
     raise ValueError("La cantidad del producto tiene que ser mayor o igual a 0")
    
  # Metodo toString
  def __str__(self):
    return f"Producto: {self.__nombre}, Categoria: {self.__categoria}, Precio: {self.__precio}, Cantidad: {self.__cantidad}"
  
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
            if precio is not None:
                producto.set_precio(precio)
                print(f"Precio de {nombre} actualizado a {precio}.")
            if cantidad is not None:
                producto.set_cantidad(cantidad)
                print(f"Cantidad de {nombre} actualizada a {cantidad}.")
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
    
if __name__ == "__main__":

  producto02 = Producto("Laptop", "Electrónica", 1500, 10)  
  producto03 = Producto("Samsung", "Electrónica", 2000, 100)  
  producto04 = Producto("Teclado", "Electrónica", 40, 5)

  inventario = Inventario()
  inventario.mostrar_inventario()
  inventario.agregar_producto(producto02)
  inventario.agregar_producto(producto03)  
  inventario.agregar_producto(producto04)
  
  inventario.mostrar_inventario()
  inventario.actualizar_producto("Laptop", precio=1201, cantidad=20)
  inventario.eliminar_producto("Samsung")
  
  inventario.mostrar_inventario()
  
