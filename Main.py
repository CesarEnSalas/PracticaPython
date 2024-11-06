from Producto import Producto
from Inventario import Inventario

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
  
