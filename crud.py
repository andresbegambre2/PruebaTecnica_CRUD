from conexion import conectar

def crear_producto():
    conexion = conectar()
    cursor = conexion.cursor()

    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock: "))
    categoria = input("Categoría: ")

    if precio < 0:
        print("El precio no puede ser negativo.")
        conexion.close()
        return

    if stock < 0:
        print("El stock no puede ser negativo.")
        conexion.close()
        return

    sql = """
    INSERT INTO productos(nombre, precio, stock, categoria)
    VALUES (%s, %s, %s, %s)
    """

    valores = (nombre, precio, stock, categoria)

    cursor.execute(sql, valores)
    conexion.commit()

    print("Producto registrado correctamente.")

    cursor.close()
    conexion.close()

def listar_productos():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    if not productos:
        print("No hay productos registrados.")
    else:
        print("\nLista de productos")
        print("-" * 60)

        for producto in productos:
            print(f"ID: {producto[0]}")
            print(f"Nombre: {producto[1]}")
            print(f"Precio: {producto[2]}")
            print(f"Stock: {producto[3]}")
            print(f"Categoría: {producto[4]}")
            print("-" * 60)

    cursor.close()
    conexion.close()    