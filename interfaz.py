import tkinter as tk

from tkinter import messagebox


def crear():
    messagebox.showinfo("Información", "Aquí irá la función Crear")


def actualizar():
    messagebox.showinfo("Información", "Aquí irá la función Actualizar")


def eliminar():
    messagebox.showinfo("Información", "Aquí irá la función Eliminar")


def listar():
    messagebox.showinfo("Información", "Aquí irá la función Listar")

ventana = tk.Tk()
ventana.title("CRUD de Productos")
ventana.geometry("700x500")

titulo = tk.Label(
    ventana,
    text="CRUD DE PRODUCTOS",
    font=("Arial", 18, "bold")
)
titulo.pack(pady=10)

tk.Label(ventana, text="Nombre").pack()
entrada_nombre = tk.Entry(ventana, width=40)
entrada_nombre.pack()

tk.Label(ventana, text="Precio").pack()
entrada_precio = tk.Entry(ventana, width=40)
entrada_precio.pack()

tk.Label(ventana, text="Stock").pack()
entrada_stock = tk.Entry(ventana, width=40)
entrada_stock.pack()

tk.Label(ventana, text="Categoría").pack()
entrada_categoria = tk.Entry(ventana, width=40)
entrada_categoria.pack()

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=15)

tk.Button(frame_botones, text="Crear", width=12, command=crear).grid(row=0, column=0, padx=5)

tk.Button(frame_botones, text="Actualizar", width=12, command=actualizar).grid(row=0, column=1, padx=5)

tk.Button(frame_botones, text="Eliminar", width=12, command=eliminar).grid(row=0, column=2, padx=5)

tk.Button(frame_botones, text="Listar", width=12, command=listar).grid(row=0, column=3, padx=5)

ventana.mainloop()