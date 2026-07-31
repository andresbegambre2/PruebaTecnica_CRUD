import tkinter as tk
from tkinter import ttk, messagebox
from conexion import conectar



def cargar_productos():
    """Trae todos los productos y los pinta en la tabla."""
    for fila in tabla.get_children():
        tabla.delete(fila)

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    cursor.close()
    conexion.close()

    for producto in productos:
        tabla.insert("", tk.END, values=producto)


def limpiar_campos():
    entry_id.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_precio.delete(0, tk.END)
    entry_stock.delete(0, tk.END)
    entry_categoria.delete(0, tk.END)


def crear_producto():
    nombre = entry_nombre.get().strip()
    precio = entry_precio.get().strip()
    stock = entry_stock.get().strip()
    categoria = entry_categoria.get().strip()

    if not nombre or not precio or not stock:
        messagebox.showwarning("Datos incompletos", "Nombre, precio y stock son obligatorios.")
        return

    try:
        precio = float(precio)
        stock = int(stock)
    except ValueError:
        messagebox.showerror("Error", "Precio debe ser numérico y stock un número entero.")
        return

    if precio < 0 or stock < 0:
        messagebox.showerror("Error", "El precio y el stock no pueden ser negativos.")
        return

    conexion = conectar()
    cursor = conexion.cursor()
    sql = """
        INSERT INTO productos(nombre, precio, stock, categoria)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql, (nombre, precio, stock, categoria))
    conexion.commit()
    cursor.close()
    conexion.close()

    messagebox.showinfo("Éxito", "Producto registrado correctamente.")
    limpiar_campos()
    cargar_productos()


def actualizar_producto():
    id_producto = entry_id.get().strip()
    if not id_producto:
        messagebox.showwarning("Falta el ID", "Selecciona un producto de la tabla primero.")
        return

    nombre = entry_nombre.get().strip()
    precio = entry_precio.get().strip()
    stock = entry_stock.get().strip()
    categoria = entry_categoria.get().strip()

    try:
        precio = float(precio)
        stock = int(stock)
    except ValueError:
        messagebox.showerror("Error", "Precio debe ser numérico y stock un número entero.")
        return

    if precio < 0 or stock < 0:
        messagebox.showerror("Error", "El precio y el stock no pueden ser negativos.")
        return

    conexion = conectar()
    cursor = conexion.cursor()
    sql = """
        UPDATE productos
        SET nombre = %s, precio = %s, stock = %s, categoria = %s
        WHERE id = %s
    """
    cursor.execute(sql, (nombre, precio, stock, categoria, id_producto))
    conexion.commit()
    cursor.close()
    conexion.close()

    messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
    limpiar_campos()
    cargar_productos()


def eliminar_producto():
    id_producto = entry_id.get().strip()
    if not id_producto:
        messagebox.showwarning("Falta el ID", "Selecciona un producto de la tabla primero.")
        return

    confirmar = messagebox.askyesno("Confirmar", f"¿Eliminar el producto con ID {id_producto}?")
    if not confirmar:
        return

    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE id = %s", (id_producto,))
    conexion.commit()
    cursor.close()
    conexion.close()

    messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
    limpiar_campos()
    cargar_productos()


def seleccionar_fila(event):
    seleccionado = tabla.focus()
    if not seleccionado:
        return
    valores = tabla.item(seleccionado, "values")

    limpiar_campos()
    entry_id.insert(0, valores[0])
    entry_nombre.insert(0, valores[1])
    entry_precio.insert(0, valores[2])
    entry_stock.insert(0, valores[3])
    entry_categoria.insert(0, valores[4])



ventana = tk.Tk()
ventana.title("CRUD de productos")
ventana.geometry("650x500")

frame_form = ttk.Frame(ventana, padding=10)
frame_form.pack(fill="x")

ttk.Label(frame_form, text="ID (solo lectura):").grid(row=0, column=0, sticky="w")
entry_id = ttk.Entry(frame_form, state="readonly")
entry_id.grid(row=0, column=1, sticky="ew", padx=5, pady=2)

ttk.Label(frame_form, text="Nombre:").grid(row=1, column=0, sticky="w")
entry_nombre = ttk.Entry(frame_form)
entry_nombre.grid(row=1, column=1, sticky="ew", padx=5, pady=2)

ttk.Label(frame_form, text="Precio:").grid(row=2, column=0, sticky="w")
entry_precio = ttk.Entry(frame_form)
entry_precio.grid(row=2, column=1, sticky="ew", padx=5, pady=2)

ttk.Label(frame_form, text="Stock:").grid(row=3, column=0, sticky="w")
entry_stock = ttk.Entry(frame_form)
entry_stock.grid(row=3, column=1, sticky="ew", padx=5, pady=2)

ttk.Label(frame_form, text="Categoría:").grid(row=4, column=0, sticky="w")
entry_categoria = ttk.Entry(frame_form)
entry_categoria.grid(row=4, column=1, sticky="ew", padx=5, pady=2)

frame_form.columnconfigure(1, weight=1)

frame_botones = ttk.Frame(ventana, padding=(10, 0))
frame_botones.pack(fill="x")

ttk.Button(frame_botones, text="Crear", command=crear_producto).pack(side="left", padx=5)
ttk.Button(frame_botones, text="Actualizar", command=actualizar_producto).pack(side="left", padx=5)
ttk.Button(frame_botones, text="Eliminar", command=eliminar_producto).pack(side="left", padx=5)
ttk.Button(frame_botones, text="Limpiar campos", command=limpiar_campos).pack(side="left", padx=5)
ttk.Button(frame_botones, text="Refrescar tabla", command=cargar_productos).pack(side="left", padx=5)

columnas = ("id", "nombre", "precio", "stock", "categoria")
tabla = ttk.Treeview(ventana, columns=columnas, show="headings", height=12)
for col in columnas:
    tabla.heading(col, text=col.capitalize())
    tabla.column(col, width=100)
tabla.pack(fill="both", expand=True, padx=10, pady=10)
tabla.bind("<<TreeviewSelect>>", seleccionar_fila)

cargar_productos()

ventana.mainloop()
