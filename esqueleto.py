import tkinter as tk
from tkinter import messagebox, simpledialog, StringVar, Listbox, Scrollbar
from PIL import Image, ImageTk  # Asegúrate de tener Pillow instalado

# Ejemplo de almacenamiento de recetas (puedes cambiar esto a tu implementación real)
recetas = {}

class GestorRecetasApp:
    def __init__(self, master):
        self.master = master
        master.title("Gestor de Recetas")
        
        # Cargar imagen de fondo
        self.fondo_imagen = ImageTk.PhotoImage(Image.open("C:\\Users\\rocio\\MissingYou\\fondo.png"))  # Cambia la ruta aquí
        self.label_fondo = tk.Label(master, image=self.fondo_imagen)
        self.label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        self.label = tk.Label(master, text="Bienvenido al Gestor de Recetas", bg="white")
        self.label.pack(pady=10)

        self.boton_agregar = tk.Button(master, text="Agregar Receta", command=self.agregar_receta)
        self.boton_agregar.pack(pady=5)

        self.boton_ver = tk.Button(master, text="Ver Recetas", command=self.ver_recetas)
        self.boton_ver.pack(pady=5)

        self.boton_eliminar = tk.Button(master, text="Eliminar Receta", command=self.eliminar_receta)
        self.boton_eliminar.pack(pady=5)

        self.boton_editar = tk.Button(master, text="Editar Receta", command=self.editar_receta)
        self.boton_editar.pack(pady=5)

    def agregar_receta(self):
        def guardar_receta():
            nombre = nombre_receta.get()
            ingredientes_text = ingredientes.get()
            instrucciones_text = instrucciones.get()
            recetas[nombre] = {'ingredientes': ingredientes_text, 'instrucciones': instrucciones_text}
            messagebox.showinfo("Éxito", "Receta agregada con éxito")
            ventana_agregar.destroy()

        ventana_agregar = tk.Toplevel(self.master)
        ventana_agregar.title("Agregar Receta")

        tk.Label(ventana_agregar, text="Nombre de la receta:").pack()
        nombre_receta = tk.Entry(ventana_agregar)
        nombre_receta.pack()

        tk.Label(ventana_agregar, text="Ingredientes:").pack()
        ingredientes = tk.Entry(ventana_agregar)
        ingredientes.pack()

        tk.Label(ventana_agregar, text="Instrucciones:").pack()
        instrucciones = tk.Entry(ventana_agregar)
        instrucciones.pack()

        tk.Button(ventana_agregar, text="Guardar", command=guardar_receta).pack()

    def ver_recetas(self):
        ventana_ver = tk.Toplevel(self.master)
        ventana_ver.title("Ver Recetas")

        lista_recetas = Listbox(ventana_ver)
        lista_recetas.pack(side=tk.LEFT, fill=tk.BOTH)

        scrollbar = Scrollbar(ventana_ver)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        lista_recetas.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=lista_recetas.yview)

        for nombre in recetas:
            lista_recetas.insert(tk.END, nombre)

        def mostrar_detalles(event):
            seleccion = lista_recetas.curselection()
            if seleccion:
                indice = seleccion[0]
                nombre_receta = lista_recetas.get(indice)
                ingredientes = recetas[nombre_receta]['ingredientes']
                instrucciones = recetas[nombre_receta]['instrucciones']
                messagebox.showinfo(nombre_receta, f"Ingredientes:\n{ingredientes}\n\nInstrucciones:\n{instrucciones}")

        lista_recetas.bind('<<ListboxSelect>>', mostrar_detalles)

    def eliminar_receta(self):
        ventana_eliminar = tk.Toplevel(self.master)
        ventana_eliminar.title("Eliminar Receta")

        lista_recetas = Listbox(ventana_eliminar)
        lista_recetas.pack(side=tk.LEFT, fill=tk.BOTH)

        scrollbar = Scrollbar(ventana_eliminar)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        lista_recetas.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=lista_recetas.yview)

        for nombre in recetas:
            lista_recetas.insert(tk.END, nombre)

        def confirmar_eliminacion():
            seleccion = lista_recetas.curselection()
            if seleccion:
                indice = seleccion[0]
                nombre_receta = lista_recetas.get(indice)
                del recetas[nombre_receta]
                messagebox.showinfo("Éxito", "Receta eliminada con éxito")
                ventana_eliminar.destroy()
            else:
                messagebox.showwarning("Advertencia", "Selecciona una receta para eliminar.")

        tk.Button(ventana_eliminar, text="Eliminar", command=confirmar_eliminacion).pack()

    def editar_receta(self):
        ventana_editar = tk.Toplevel(self.master)
        ventana_editar.title("Editar Receta")

        lista_recetas = Listbox(ventana_editar)
        lista_recetas.pack(side=tk.LEFT, fill=tk.BOTH)

        scrollbar = Scrollbar(ventana_editar)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        lista_recetas.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=lista_recetas.yview)

        for nombre in recetas:
            lista_recetas.insert(tk.END, nombre)

        def cargar_receta():
            seleccion = lista_recetas.curselection()
            if seleccion:
                indice = seleccion[0]
                nombre_receta = lista_recetas.get(indice)
                ingredientes = recetas[nombre_receta]['ingredientes']
                instrucciones = recetas[nombre_receta]['instrucciones']

                # Limpiar entradas existentes
                nombre_receta_entry.delete(0, tk.END)
                nombre_receta_entry.insert(0, nombre_receta)
                ingredientes_entry.delete(0, tk.END)
                ingredientes_entry.insert(0, ingredientes)
                instrucciones_entry.delete(0, tk.END)
                instrucciones_entry.insert(0, instrucciones)

        tk.Button(ventana_editar, text="Cargar", command=cargar_receta).pack()

        tk.Label(ventana_editar, text="Nombre de la receta:").pack()
        nombre_receta_entry = tk.Entry(ventana_editar)
        nombre_receta_entry.pack()

        tk.Label(ventana_editar, text="Ingredientes:").pack()
        ingredientes_entry = tk.Entry(ventana_editar)
        ingredientes_entry.pack()

        tk.Label(ventana_editar, text="Instrucciones:").pack()
        instrucciones_entry = tk.Entry(ventana_editar)
        instrucciones_entry.pack()

        def guardar_cambios():
            seleccion = lista_recetas.curselection()
            if seleccion:
                indice = seleccion[0]
                nombre_receta_antiguo = lista_recetas.get(indice)
                nombre_receta_nuevo = nombre_receta_entry.get()
                ingredientes_text = ingredientes_entry.get()
                instrucciones_text = instrucciones_entry.get()

                # Eliminar la receta antigua y agregar la nueva
                del recetas[nombre_receta_antiguo]
                recetas[nombre_receta_nuevo] = {'ingredientes': ingredientes_text, 'instrucciones': instrucciones_text}
                messagebox.showinfo("Éxito", "Receta editada con éxito")
                ventana_editar.destroy()

        tk.Button(ventana_editar, text="Guardar Cambios", command=guardar_cambios).pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = GestorRecetasApp(root)
    root.mainloop()
