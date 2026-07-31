from crud import crear_producto, listar_productos, eliminar_producto

while True:
    print("\nCRUD DE PRODUCTOS")
    print("1. Crear producto")
    print("2. Listar productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear_producto()

    elif opcion == "2":
        listar_productos()

    elif opcion == "3":
        break

    else:
        print("Opción no válida.")