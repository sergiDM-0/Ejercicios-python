import tkinter as tk
from tkinter import simpledialog, messagebox


class GestorProyectosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Proyectos de Investigación")
        self.root.geometry("600x550")
        self.root.resizable(False, False)

        # Lista de proyectos (cada uno será un diccionario)
        self.proyectos = []

        # Título principal
        tk.Label(root, text="Gestor de Proyectos", font=("Arial", 18, "bold")).pack(pady=10)

        # Botones de acciones
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        botones = [
            ("Registrar Proyecto", self.registrar_proyecto),
            ("Buscar Proyecto", self.buscar_proyecto),
            ("Modificar Proyecto", self.modificar_proyecto),
            ("Eliminar Proyecto", self.eliminar_proyecto),
            ("Ver Lista Completa", self.mostrar_lista),
            ("Salir", root.quit)
        ]

        for texto, comando in botones:
            tk.Button(frame_botones, text=texto, width=25, font=("Arial", 11), command=comando).pack(pady=5)

        # Listbox para mostrar proyectos
        tk.Label(root, text="Proyectos registrados:", font=("Arial", 12, "bold")).pack(pady=10)
        self.lista = tk.Listbox(root, width=80, height=15, font=("Arial", 10))
        self.lista.pack(pady=5)

    def actualizar_lista(self):
        """Refresca el Listbox con los proyectos actuales"""
        self.lista.delete(0, tk.END)
        if not self.proyectos:
            self.lista.insert(tk.END, "(No hay proyectos registrados)")
        else:
            for i, p in enumerate(self.proyectos):
                texto = f"{i}. {p['nombre']} - {p['investigador']} ({p['área']}) [{p['estado']}]"
                self.lista.insert(tk.END, texto)

    def registrar_proyecto(self):
        """Agrega un nuevo proyecto"""
        nombre = simpledialog.askstring("Registrar", "Nombre del proyecto:")
        if not nombre:
            return
        # Verificar si ya existe
        for p in self.proyectos:
            if p["nombre"].lower() == nombre.lower():
                messagebox.showerror("Error", "Ya existe un proyecto con ese nombre.")
                return

        investigador = simpledialog.askstring("Registrar", "Nombre del investigador:")
        area = simpledialog.askstring("Registrar", "Área del proyecto:")
        estado = simpledialog.askstring("Registrar", "Estado del proyecto (En curso / Finalizado):")

        if not investigador or not area or not estado:
            messagebox.showerror("Error", "Debe completar todos los campos.")
            return

        nuevo = {
            "nombre": nombre,
            "investigador": investigador,
            "área": area,
            "estado": estado
        }

        self.proyectos.append(nuevo)
        messagebox.showinfo("Éxito", "Proyecto registrado correctamente.")
        self.actualizar_lista()

    def buscar_proyecto(self):
        """Busca un proyecto por nombre"""
        nombre = simpledialog.askstring("Buscar", "Ingrese el nombre del proyecto:")
        if not nombre:
            return

        for i, p in enumerate(self.proyectos):
            if p["nombre"].lower() == nombre.lower():
                mensaje = (
                    f"Proyecto encontrado:\n\n"
                    f"Nombre: {p['nombre']}\n"
                    f"Investigador: {p['investigador']}\n"
                    f"Área: {p['área']}\n"
                    f"Estado: {p['estado']}\n"
                    f"Posición: {i}"
                )
                messagebox.showinfo("Resultado de búsqueda", mensaje)
                return
        messagebox.showwarning("No encontrado", "No existe un proyecto con ese nombre.")

    def modificar_proyecto(self):
        """Modifica un proyecto existente"""
        nombre = simpledialog.askstring("Modificar", "Ingrese el nombre del proyecto a modificar:")
        if not nombre:
            return

        for p in self.proyectos:
            if p["nombre"].lower() == nombre.lower():
                nuevo_nombre = simpledialog.askstring("Modificar", "Nuevo nombre:", initialvalue=p["nombre"])
                nuevo_investigador = simpledialog.askstring("Modificar", "Nuevo investigador:", initialvalue=p["investigador"])
                nueva_area = simpledialog.askstring("Modificar", "Nueva área:", initialvalue=p["área"])
                nuevo_estado = simpledialog.askstring("Modificar", "Nuevo estado:", initialvalue=p["estado"])

                if nuevo_nombre and nuevo_investigador and nueva_area and nuevo_estado:
                    p.update({
                        "nombre": nuevo_nombre,
                        "investigador": nuevo_investigador,
                        "área": nueva_area,
                        "estado": nuevo_estado
                    })
                    messagebox.showinfo("Éxito", "Proyecto modificado correctamente.")
                    self.actualizar_lista()
                else:
                    messagebox.showerror("Error", "No puede dejar campos vacíos.")
                return

        messagebox.showwarning("No encontrado", "No existe un proyecto con ese nombre.")

    def eliminar_proyecto(self):
        """Elimina un proyecto por nombre"""
        nombre = simpledialog.askstring("Eliminar", "Ingrese el nombre del proyecto a eliminar:")
        if not nombre:
            return

        for p in self.proyectos:
            if p["nombre"].lower() == nombre.lower():
                self.proyectos.remove(p)
                messagebox.showinfo("Eliminado", f"El proyecto '{nombre}' ha sido eliminado.")
                self.actualizar_lista()
                return

        messagebox.showwarning("No encontrado", "No existe un proyecto con ese nombre.")

    def mostrar_lista(self):
        """Actualiza la lista visual"""
        self.actualizar_lista()


# Ejecución del programa
if __name__ == "__main__":
    root = tk.Tk()
    app = GestorProyectosApp(root)
    root.mainloop()

