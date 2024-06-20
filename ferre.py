# Clase Producto para representar los productos en la ferretería
class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

# Lista de productos de la ferretería
productos = [
    Producto("001", "Martillo", 15.50, 50),
    Producto("002", "Destornillador", 5.75, 100),
    Producto("003", "Llave Inglesa", 12.30, 30),
    Producto("004", "Sierra Circular", 45.80, 20),
    Producto("005", "Taladro", 60.00, 15)
]

# Función para mostrar el inventario de productos
def mostrar_inventario():
    print("Inventario de la ferretería:")
    for producto in productos:
        print(f"Código: {producto.codigo} - Nombre: {producto.nombre} - Precio: ${producto.precio} - Stock: {producto.stock}")

# Función para realizar una venta
def realizar_venta():
    codigo_producto = input("Ingrese el código del producto a vender: ")
    cantidad = int(input("Ingrese la cantidad a vender: "))

    for producto in productos:
        if producto.codigo == codigo_producto:
            if producto.stock >= cantidad:
                producto.stock -= cantidad
                print(f"Venta realizada - Total a pagar: ${producto.precio * cantidad}")
            else:
                print("Error: Stock insuficiente para realizar la venta.")
            return

    print("Error: Producto no encontrado.")

# Función principal del sistema
def main():
    while True:
        print("\n1. Mostrar Inventario")
        print("2. Realizar Venta")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_inventario()
        elif opcion == "2":
            realizar_venta()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
