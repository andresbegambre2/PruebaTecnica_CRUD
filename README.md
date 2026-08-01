# CRUD de Productos - Python + MySQL

## Descripción del proyecto

Durante el desarrollo fui separando el código en diferentes archivos para mantener una mejor organización y facilitar posibles cambios en el futuro.

## Tecnologías utilizadas

* Python
* MySQL
* MySQL Connector
* Tkinter para la interfaz gráfica

## Desarrollo del proyecto

### Conexión con la base de datos

Lo primero que realicé fue la conexión entre Python y MySQL.

Para esto creé el archivo `conexion.py`, donde se encuentra la función `conectar()` encargada de establecer la conexión con la base de datos.

Decidí manejar la conexión en un archivo independiente para evitar repetir el mismo código en cada operación y tener un solo lugar donde modificar los datos de acceso a la base de datos.

conexion:

```python
def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="crud_productos"
    )
    return conexion
```

## Creación de las funciones CRUD

Después de tener lista la conexión, desarrollé las funciones principales para manejar los productos:

* `crear_producto()` para registrar nuevos productos.
* `listar_productos()` para consultar los productos almacenados.
* `actualizar_producto()` para modificar información existente.
* `eliminar_producto()` para borrar productos.

Para ejecutar las consultas en MySQL utilicé parámetros:

```python
cursor.execute(sql, valores)
```

Esto permite enviar los datos separados de la consulta SQL y evita construir consultas directamente con la información ingresada por el usuario.

## Validaciones realizadas

Durante el desarrollo agregué validaciones para controlar la información antes de guardarla en la base de datos.

Por ejemplo, se valida que el precio y el stock no sean valores negativos:

```python
if precio < 0 or stock < 0:
```

También se revisa que los campos principales tengan información antes de registrar un producto.

Estas validaciones ayudan a mantener datos correctos dentro del sistema.

## Creación de la interfaz gráfica

Después de tener funcionando el CRUD, agregué una interfaz gráfica utilizando Tkinter.

La interfaz permite realizar las mismas operaciones pero de una forma más sencilla para el usuario, utilizando botones, campos de texto y una tabla para visualizar los productos.

Para mostrar los registros utilicé `Treeview`, ya que permite organizar la información en forma de tabla.

## Selección de productos

Se agregó una función para seleccionar un producto directamente desde la tabla.

Al seleccionar un registro, sus datos se cargan automáticamente en los campos de edición, permitiendo actualizar la información sin tener que escribir nuevamente todos los datos.

## Organización del proyecto

La estructura quedó organizada de la siguiente manera:

```
CRUD_PRODUCTOS

├── conexion.py
├── crud.py
├── interfaz.py
└── main.py
```

`conexion.py`: manejo de conexión con MySQL.

`crud.py`: contiene la lógica de las operaciones sobre los productos.

`interfaz.py`: contiene la ventana gráfica y la interacción con el usuario.

`main.py`: archivo utilizado para ejecutar el programa en consola.

## Contratiempos durante el desarrollo

Tuve algunas fallas con el equipo mientras trabajaba en esto y se me fue el tiempo, así que no alcancé a pulir todo como quería. Sin embargo, sí logré resolver el error inicial donde el sistema no reconocía el ID del producto al momento de actualizar o eliminar. 

El problema era que el campo de ID estaba configurado en modo solo lectura, y por eso, aunque seleccionara un producto en la tabla, el ID no se guardaba correctamente. Esto hacía que al presionar "Actualizar" o "Eliminar" saliera el mensaje de que faltaba seleccionar un producto, aunque sí lo había seleccionado.

La solución fue habilitar momentáneamente el campo antes de insertar el valor, y luego volver a bloquearlo:

En `interfaz.py`Reemplazar las funciones por

```python

def seleccionar_fila(event):
    seleccionado = tabla.focus()
    if not seleccionado:
        return
    valores = tabla.item(seleccionado, "values")

    limpiar_campos()

    entry_id.config(state="normal")      
    entry_id.insert(0, valores[0])
    entry_id.config(state="readonly")    

    entry_nombre.insert(0, valores[1])
    entry_precio.insert(0, valores[2])
    entry_stock.insert(0, valores[3])
    entry_categoria.insert(0, valores[4])
```

Y lo mismo apliqué en la función que limpia los campos, para que no fallara al intentar borrar el ID:

```python
def limpiar_campos():
    entry_id.config(state="normal")
    entry_id.delete(0, tk.END)
    entry_id.config(state="readonly")

    entry_nombre.delete(0, tk.END)
    entry_precio.delete(0, tk.END)
    entry_stock.delete(0, tk.END)
    entry_categoria.delete(0, tk.END)
```

Con estos ajustes, ya el programa reconoce bien el ID seleccionado y las funciones de actualizar y eliminar funcionan correctamente.
Por no alterar el horario de subida del proyecto ya funcional, no subo el código con este cambio aplicado; queda documentado aquí en el README para integrarlo en la próxima actualización.



## Ejecución

Instalar la dependencia necesaria:

```bash
pip install mysql-connector-python
```

Configurar los datos de conexión en `conexion.py`.

Ejecutar la aplicación

