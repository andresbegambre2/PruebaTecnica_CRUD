from crud import crear_producto

while True:
    print("\nCRUD DE PRODUCTOS")
    print("1. Crear producto")
    print("2. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear_producto()

    elif opcion == "2":
        break

    else:
        print("Opción no válida.")