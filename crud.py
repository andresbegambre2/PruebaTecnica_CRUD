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