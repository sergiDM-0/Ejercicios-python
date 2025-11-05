import tkinter as tk
from tkinter import simpledialog, messagebox
class ArregloUnidimensionalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Arreglo Unidimensional - Nombres")
        self.root.geometry("480x580")
        self.root.resizable(False, False)

        # Preguntar tamaño del arreglo al iniciar
        self.tamano = simpledialog.askinteger(
            "Tamaño del arreglo",
            "¿Cuántos nombres desea registrar?",
            minvalue=1,
            maxvalue=100
        )

        if not self.tamano:
            messagebox.showinfo("Salida", "Debe ingresar un tamaño válido. El programa se cerrará.")
            root.destroy()
            return

        self.nombres = [None] * self.tamano
        self.papelera = []  # Guarda tuplas (nombre, posición)

        # --- Interfaz gr/áfica ---
        tk.Label(root, text="MENÚ PRINCIPAL", font=("Arial", 16, "bold")).pack(pady=10)

        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        botones = [
            ("Registrar nombre", self.registrar),
            ("Buscar nombre", self.buscar),
            ("Modificar nombre", self.modificar),
            ("Modificar por posición", self.modificar_por_posicion),
            ("Eliminar por posición", self.eliminar_por_posicion),
            ("Deshacer eliminación", self.deshacer_eliminacion),
            ("Salir", root.quit)
        ]

        for texto, comando in botones:
            tk.Button(frame_botones, text=texto, width=25, font=("Arial", 10), command=comando).pack(pady=5)

        tk.Label(root, text="Nombres registrados:", font=("Arial", 12, "bold")).pack(pady=10)
        self.lista = tk.Listbox(root, width=45, height=10, font=("Arial", 11))
        self.lista.pack(pady=5)

        # Etiqueta de papelera
        self.lbl_papelera = tk.Label(root, text="Papelera: (vacía)", font=("Arial", 10, "italic"))
        self.lbl_papelera.pack(pady=5)

        self.actualizar_lista()

    # ---------------- MÉTODOS ---------------- #

    def actualizar_lista(self):
        """Refresca el contenido del Listbox con los nombres actuales."""
        self.lista.delete(0, tk.END)
        for i, n in enumerate(self.nombres):
            texto = f"{i}: {n if n is not None else '(vacío)'}"
            self.lista.insert(tk.END, texto)
        # Actualizar etiqueta de papelera
        if self.papelera:
            ultimo = self.papelera[-1]
            self.lbl_papelera.config(text=f"Papelera: {ultimo[0]} (posición {ultimo[1]})")
        else:
            self.lbl_papelera.config(text="Papelera: (vacía)")

    def registrar(self):
        if None not in self.nombres:
            messagebox.showwarning("Advertencia", "El arreglo está lleno.")
            return

        nombre = simpledialog.askstring("Registrar", "Ingrese un nombre:")
        if not nombre:
            return

        nombre = nombre.strip()
        if nombre == "":
            messagebox.showerror("Error", "El nombre no puede estar vacío.")
            return

        if nombre in self.nombres:
            messagebox.showerror("Error", "Este nombre ya está registrado.")
            return

        for i in range(len(self.nombres)):
            if self.nombres[i] is None:
                self.nombres[i] = nombre
                messagebox.showinfo("Éxito", f"Nombre '{nombre}' registrado en la posición {i}.")
                break

        self.actualizar_lista()

    def buscar(self):
        nombre = simpledialog.askstring("Buscar", "Ingrese el nombre a buscar:")
        if not nombre:
            return

        nombre = nombre.strip()
        if nombre == "":
            return

        if nombre in self.nombres:
            pos = self.nombres.index(nombre)
            messagebox.showinfo("Resultado", f"'{nombre}' se encuentra en la posición {pos}.")
        else:
            messagebox.showerror("No encontrado", f"'{nombre}' no está en el arreglo.")

    def modificar(self):
        nombre = simpledialog.askstring("Modificar", "Ingrese el nombre a modificar:")
        if not nombre:
            return

        nombre = nombre.strip()
        if nombre == "":
            return

        if nombre in self.nombres:
            nuevo = simpledialog.askstring("Nuevo nombre", f"Ingrese el nuevo nombre para '{nombre}':")
            if not nuevo:
                return
            nuevo = nuevo.strip()
            if nuevo == "":
                messagebox.showerror("Error", "El nuevo nombre no puede estar vacío.")
                return
            if nuevo in self.nombres:
                messagebox.showerror("Error", "El nuevo nombre ya existe en el arreglo.")
                return
            pos = self.nombres.index(nombre)
            self.nombres[pos] = nuevo
            messagebox.showinfo("Éxito", f"'{nombre}' fue modificado por '{nuevo}'.")
            self.actualizar_lista()
        else:
            messagebox.showerror("No encontrado", f"'{nombre}' no está en el arreglo.")

    def modificar_por_posicion(self):
        """Permite modificar un nombre directamente por su posición."""
        if all(x is None for x in self.nombres):
            messagebox.showwarning("Advertencia", "El arreglo está vacío. No hay nada que modificar.")
            return

        pos = simpledialog.askinteger(
            "Modificar por posición",
            f"Ingrese la posición (0 a {self.tamano - 1}) a modificar:",
            minvalue=0,
            maxvalue=self.tamano - 1
        )

        if pos is None:
            return

        if self.nombres[pos] is None:
            messagebox.showerror("Error", f"La posición {pos} está vacía, no hay nombre para modificar.")
            return

        nuevo_nombre = simpledialog.askstring("Nuevo nombre", f"Ingrese el nuevo nombre para la posición {pos}:")
        if not nuevo_nombre:
            return

        nuevo_nombre = nuevo_nombre.strip()
        if nuevo_nombre == "":
            messagebox.showerror("Error", "El nombre no puede estar vacío.")
            return

        if nuevo_nombre in self.nombres:
            messagebox.showerror("Error", "Ese nombre ya existe en el arreglo.")
            return

        antiguo = self.nombres[pos]
        self.nombres[pos] = nuevo_nombre
        messagebox.showinfo("Éxito", f"'{antiguo}' fue modificado por '{nuevo_nombre}' en la posición {pos}.")
        self.actualizar_lista()

    def eliminar_por_posicion(self):
        """Pide la posición (índice) para eliminar y la mueve a la papelera."""
        if all(x is None for x in self.nombres):
            messagebox.showwarning("Advertencia", "El arreglo está vacío. No hay nada que eliminar.")
            return

        pos = simpledialog.askinteger(
            "Eliminar por posición",
            f"Ingrese la posición (0 a {self.tamano - 1}) a eliminar:",
            minvalue=0,
            maxvalue=self.tamano - 1
        )

        if pos is None:
            return

        if self.nombres[pos] is None:
            messagebox.showerror("Error", f"La posición {pos} está vacía (no hay nombre para eliminar).")
            return

        confirmar = messagebox.askyesno("Confirmar eliminación", f"¿Desea eliminar '{self.nombres[pos]}' en la posición {pos}?")
        if not confirmar:
            return

        eliminado = self.nombres[pos]
        self.papelera.append((eliminado, pos))
        self.nombres[pos] = None
        messagebox.showinfo("Eliminado", f"'{eliminado}' fue movido a la papelera.")
        self.actualizar_lista()

    def deshacer_eliminacion(self):
        """Restaura el último nombre eliminado si su posición está vacía."""
        if not self.papelera:
            messagebox.showinfo("Papelera vacía", "No hay eliminaciones para deshacer.")
            return

        nombre, pos = self.papelera[-1]
        if self.nombres[pos] is not None:
            messagebox.showwarning("Advertencia", f"No se puede restaurar '{nombre}' porque la posición {pos} ya está ocupada.")
            return

        confirmar = messagebox.askyesno("Restaurar", f"¿Desea restaurar '{nombre}' en la posición {pos}?")
        if not confirmar:
            return

        self.nombres[pos] = nombre
        self.papelera.pop()
        messagebox.showinfo("Restaurado", f"'{nombre}' fue restaurado en la posición {pos}.")
        self.actualizar_lista()


# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = ArregloUnidimensionalApp(root)
    root.mainloop()

