from Producto import Producto
from Inventario import Inventario


def imprimir_mensaje():
    print("-" * 30)
    print("""
¿Que acción quieres realizar?
1. Mostrar Inventario
2. Agregar Producto
3. Actualizar Producto
4. Eliminar Producto
0. Finalizar
""".strip())
    print("-" * 30)

if __name__ == "__main__":

    inventario = Inventario()

    while True:
        imprimir_mensaje()
        try:
            numero = int(input("¿Que acción quieres realizar?: "))
            print("")
            if numero == 0:
                print("Finalizando Programa...")
                break
            elif numero == 1:
                inventario.mostrar_inventario()
            elif numero == 2:
                inventario.agregar_producto()
            elif numero == 3:
                inventario.actualizar_producto()
            elif numero == 4:
                print("¿Que Producto quieres Borrar?")
                nombre = input("Nombre del Producto: ")
                inventario.eliminar_producto(nombre)
            else:
                print("Opción no válida. Intente con los número de la lista.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número")
