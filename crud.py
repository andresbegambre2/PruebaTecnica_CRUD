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

def actualizar_producto():
    conexion = conectar()
    cursor = conexion.cursor()

    id_producto = int(input("Ingrese el ID del producto a actualizar: "))

    cursor.execute("SELECT * FROM productos WHERE id = %s", (id_producto,))
    producto = cursor.fetchone()

    if producto is None:
        print("Producto no encontrado.")
        conexion.close()
        return

    print(f"Nombre actual: {producto[1]}")
    nuevo_nombre = input("Nuevo nombre (dejar en blanco para no cambiar): ")
    if not nuevo_nombre:
        nuevo_nombre = producto[1]

    print(f"Precio actual: {producto[2]}")
    nuevo_precio_input = input("Nuevo precio (dejar en blanco para no cambiar): ")
    if not nuevo_precio_input:
        nuevo_precio = producto[2]
    else:
        nuevo_precio = float(nuevo_precio_input)
        if nuevo_precio < 0:
            print("El precio no puede ser negativo.")
            conexion.close()
            return

    print(f"Stock actual: {producto[3]}")
    nuevo_stock_input = input("Nuevo stock (dejar en blanco para no cambiar): ")
    if not nuevo_stock_input:
        nuevo_stock = producto[3]
    else:
        nuevo_stock = int(nuevo_stock_input)
        if nuevo_stock < 0:
            print("El stock no puede ser negativo.")
            conexion.close()
            return

    print(f"Categoría actual: {producto[4]}")
    nueva_categoria = input("Nueva categoría (dejar en blanco para no cambiar): ")
    if not nueva_categoria:
        nueva_categoria = producto[4]

    sql = """
    UPDATE productos
    SET nombre = %s, precio = %s, stock = %s, categoria = %s
    WHERE id = %s
    """

    valores = (nuevo_nombre, nuevo_precio, nuevo_stock, nueva_categoria, id_producto)

    cursor.execute(sql, valores)
    conexion.commit()

    print("Producto actualizado correctamente.")

    cursor.close()
    conexion.close()    