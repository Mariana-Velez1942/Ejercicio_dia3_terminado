# Inventario como diccionario: clave = nombre del producto, valor = (precio, cantidad)
inventario = {}

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Menú de Gestión de Inventario ---")
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar precio")
    print("4. Eliminar producto")
    print("5. Calcular valor total del inventario")
    print("0. Salir")

# Función para añadir producto
def añadir_producto():
    nombre = input("Ingrese el nombre del producto: ").strip()
    if len(nombre) == 0:
        print("El nombre no puede estar vacío.")
        return
    try:
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad disponible: "))
        inventario[nombre] = (precio, cantidad)
        print("Producto añadido correctamente.")
    except ValueError:
        print("Error: Ingrese datos válidos para precio y cantidad.")

# Función para consultar un producto
def consultar_producto():
    nombre = input("Ingrese el nombre del producto a consultar: ").strip()
    if nombre in inventario:
        precio, cantidad = inventario[nombre]
        print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")
    else:
        print("El producto no está en el inventario.")

# Función para actualizar el precio
def actualizar_precio():
    nombre = input("Ingrese el nombre del producto a actualizar: ").strip()
    if nombre in inventario:
        try:
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            cantidad = inventario[nombre][1]
            inventario[nombre] = (nuevo_precio, cantidad)
            print("Precio actualizado correctamente.")
        except ValueError:
            print("Error: Ingrese un valor numérico válido para el precio.")
    else:
        print("El producto no está en el inventario.")

# Función para eliminar un producto
def eliminar_producto():
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip()
    if nombre in inventario:
        del inventario[nombre]
        print("Producto eliminado correctamente.")
    else:
        print("El producto no está en el inventario.")

# Función lambda para calcular el valor total del inventario
calcular_valor_total = lambda: sum(precio * cantidad for precio, cantidad in inventario.values())

# Bucle principal
while True:
    mostrar_menu()
    try:
        opcion = int(input("Seleccione una opción: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    if opcion == 1:
        añadir_producto()
    elif opcion == 2:
        consultar_producto()
    elif opcion == 3:
        actualizar_precio()
    elif opcion == 4:
        eliminar_producto()
    elif opcion == 5:
        total = calcular_valor_total()
        print(f"Valor total del inventario: ${total:.2f}")
    elif opcion == 0:
        print("Gracias por usar el gestor de inventario. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
