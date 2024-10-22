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


    def agregar_producto(self, producto):
      if self.buscar_producto(producto.get_nombre()) is None:
        self.__productos.append(producto)
        print(f"Producto {producto.get_nombre()} agregado al inventario.")
      else:
        print(f"El producto {producto.get_nombre()} ya existe en el inventario.")