import tkinter as tk
from models.biblioteca_modelo import agregar_biblioteca
from tkinter import messagebox, ttk
from gui.formulario_libro import crear_libro
from models.biblioteca_modelo import obtener_bibliotecas2

def crear_biblioteca(interfaz):
    interfaz.title("Formulario biblioteca")
    tk.Label(interfaz,text="Id biblioteca:").grid(row=0, column=0, sticky="e")
    input_id = tk.Entry(interfaz)
    input_id.grid(row=0, column=1, padx=5, pady=5)
    
    tk.Label(interfaz,text="Nombre:").grid(row=1, column=0, sticky="e")
    input_nombre = tk.Entry(interfaz)
    input_nombre.grid(row=1, column=1, padx=5, pady=5)
    
    
    tk.Label(interfaz,text="Ubicación:").grid(row=2, column=0, sticky="e")
    input_ubicacion = tk.Entry(interfaz)
    input_ubicacion.grid(row=2, column=1, padx=5, pady=5)

    def agregar():
        try:
            id_biblioteca = input_id.get()
            nombre_biblioteca = input_nombre.get()
            ubicacion_biblioteca = input_ubicacion.get()
            if not (id_biblioteca and nombre_biblioteca and ubicacion_biblioteca):
                messagebox.showwarning("Advertencia", "Debes rellenar los campos!")
                return
            agregar_biblioteca(id_biblioteca, nombre_biblioteca, ubicacion_biblioteca)
            messagebox.showinfo("Mensaje","Biblioteca agregada con éxito!")
            carga_bibliotecas()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(interfaz, text="Registrar", command=agregar ).grid(row=3, column=1, padx=5, pady=5)
    
    tk.Button(interfaz, text="Agregar libro", command=crear_libro).grid(row=4, column=1, padx=5, pady=5)

    #Vamos a mostrar una tablita:
    tk.Label(interfaz,text="Listado de bibliotecas").grid(row=5, column=0, columnspan=2)
    tabla = ttk.Treeview(interfaz, columns=("ID","NOMBRE","UBICACION"),show="headings")
    tabla.heading("id",text="id")
    tabla.heading("nombre",text="nombre")
    tabla.heading("ubicacion",text="ubicacion")
    tabla.grid(row=6,column=0,columnspan=2,padx=10,pady=5)

    def carga_bibliotecas():
        try:
            bibliotecas= obtener_bibliotecas2()
            #Como borrar todos los datos de una tabla ttk.treeview
            fila = tabla.get_children()
            for f in fila:
                tabla.delete(f)
            tabla.delete()
            for b in bibliotecas:
                tabla.insert("","end",values=b)
        except Exception as ex:
            messagebox.showerror("Error",f" No se puedieron cargar las bibliotecas: {ex}")
    
    carga_bibliotecas()