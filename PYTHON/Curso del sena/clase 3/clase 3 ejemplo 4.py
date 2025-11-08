
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import filedialog, messagebox
import os

# ===============================
# FUNCIONES PRINCIPALES
# ===============================

def cargar_archivo():
    """Permite seleccionar y cargar un archivo CSV o Excel"""
    ruta = filedialog.askopenfilename(
        title="Seleccionar archivo académico",
        filetypes=[("Archivos CSV o Excel", "*.csv *.xlsx")]
    )
    if not ruta:
        return

    try:
        global df
        if ruta.endswith(".csv"):
            df = pd.read_csv(ruta)
        else:
            df = pd.read_excel(ruta)

        # Intentar convertir notas a numéricas
        if "Nota" in df.columns:
            df["Nota"] = pd.to_numeric(df["Nota"], errors="coerce")
            df["Nota"] = df["Nota"].clip(0, 5)  # Limita notas entre 0 y 5

        lbl_estado.config(text=f"✅ Archivo cargado: {os.path.basename(ruta)}")
        messagebox.showinfo("Éxito", "Datos cargados correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar el archivo:\n{e}")

def validar_datos():
    """Valida los registros académicos y administrativos"""
    if df is None or df.empty:
        messagebox.showwarning("Advertencia", "Primero cargue un archivo válido.")
        return

    errores = []

    vacios = df[df.isnull().any(axis=1)]
    if not vacios.empty:
        errores.append(f"Registros con campos vacíos: {len(vacios)}")

    if "Nota" in df.columns:
        fuera_rango = df[(df["Nota"] < 0) | (df["Nota"] > 5)]
        if not fuera_rango.empty:
            errores.append(f"Notas fuera de rango (corregidas): {len(fuera_rango)}")
    else:
        errores.append("No existe la columna 'Nota'")

    programas_validos = ["Sistemas", "Contabilidad", "Gestión Empresarial", "Electrónica"]
    if "Programa" in df.columns:
        no_validos = df[~df["Programa"].isin(programas_validos)]
        if not no_validos.empty:
            errores.append(f"Programas no reconocidos: {len(no_validos)}")
    else:
        errores.append("No existe la columna 'Programa'")

    if errores:
        messagebox.showwarning("Validación completada", "\n".join(errores))
    else:
        messagebox.showinfo("Validación completada", "Todos los datos son válidos.")
    lbl_estado.config(text="🔎 Validación finalizada")

def generar_reporte():
    """Genera el reporte institucional en Excel"""
    if df is None or df.empty:
        messagebox.showwarning("Advertencia", "Primero cargue un archivo válido.")
        return

    try:
        reporte = df.groupby("Programa").agg(
            Promedio_Nota=("Nota", "mean"),
            Aprobados=("Estado", lambda x: (x == "Aprobado").sum()),
            Reprobados=("Estado", lambda x: (x == "Reprobado").sum()),
            Total=("Estado", "count")
        )
        reporte["Tasa_Aprobación"] = (reporte["Aprobados"] / reporte["Total"]) * 100
        reporte.to_excel("Reporte_Institucional.xlsx")
        messagebox.showinfo("Éxito", "Reporte guardado como 'Reporte_Institucional.xlsx'")
        lbl_estado.config(text="📊 Reporte institucional generado")
        return reporte
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo generar el reporte:\n{e}")

def mostrar_graficos():
    """Muestra los gráficos de desempeño institucional con Matplotlib"""
    if df is None or df.empty:
        messagebox.showwarning("Advertencia", "Primero cargue un archivo válido.")
        return

    try:
        reporte = df.groupby("Programa").agg(
            Promedio_Nota=("Nota", "mean"),
            Tasa_Aprobación=("Estado", lambda x: (x == "Aprobado").sum() / len(x) * 100),
            Total=("Estado", "count")
        )

        # Crear figura de Matplotlib con tres gráficos
        fig, axs = plt.subplots(1, 3, figsize=(14, 5))

        # --- Gráfico 1: Promedio de notas ---
        reporte["Promedio_Nota"].plot(kind="bar", color="cornflowerblue", ax=axs[0])
        axs[0].set_title("Promedio de Notas")
        axs[0].set_ylabel("Nota promedio")
        axs[0].grid(axis="y", linestyle="--", alpha=0.6)
        fig.tight_layout()
        fig.savefig("Promedio_Notas.png")

        # --- Gráfico 2: Tasa de Aprobación ---
        reporte["Tasa_Aprobación"].plot(kind="bar", color="seagreen", ax=axs[1])
        axs[1].set_title("Tasa de Aprobación (%)")
        axs[1].grid(axis="y", linestyle="--", alpha=0.6)
        fig.tight_layout()
        fig.savefig("Tasa_Aprobacion.png")

        # --- Gráfico 3: Distribución de estudiantes ---
        axs[2].pie(
            reporte["Total"],
            labels=reporte.index,
            autopct="%1.1f%%",
            colors=["#74b9ff", "#55efc4", "#ffeaa7", "#fab1a0"]
        )
        axs[2].set_title("Distribución por Programa")
        fig.tight_layout()
        fig.savefig("Distribucion_Programas.png")

        # Mostrar los gráficos en la interfaz Tkinter
        for widget in frame_grafico.winfo_children():
            widget.destroy()
        canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
        canvas.draw()
        canvas.get_tk_widget().pack()
        lbl_estado.config(text="📈 Gráficos de desempeño generados")

    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron generar los gráficos:\n{e}")

# ===============================
# INTERFAZ GRÁFICA (Tkinter)
# ===============================

root = tk.Tk()
root.title("Sistema de Automatización Académica")
root.geometry("1100x650")
root.configure(bg="#f2f2f2")

df = None  # Variable global para los datos

titulo = tk.Label(root, text="📚 Sistema de Automatización Académica", font=("Arial", 16, "bold"), bg="#f2f2f2")
titulo.pack(pady=10)

frame_botones = tk.Frame(root, bg="#f2f2f2")
frame_botones.pack(pady=10)

btn_cargar = tk.Button(frame_botones, text="📂 Cargar Archivo", width=18, command=cargar_archivo, bg="#74b9ff")
btn_validar = tk.Button(frame_botones, text="✅ Validar Datos", width=18, command=validar_datos, bg="#81ecec")
btn_reporte = tk.Button(frame_botones, text="📊 Generar Reporte", width=18, command=generar_reporte, bg="#55efc4")
btn_graficos = tk.Button(frame_botones, text="📈 Mostrar Gráficos", width=18, command=mostrar_graficos, bg="#fab1a0")

btn_cargar.grid(row=0, column=0, padx=5, pady=5)
btn_validar.grid(row=0, column=1, padx=5, pady=5)
btn_reporte.grid(row=0, column=2, padx=5, pady=5)
btn_graficos.grid(row=0, column=3, padx=5, pady=5)

frame_grafico = tk.Frame(root, bg="white", bd=2, relief="groove", width=950, height=400)
frame_grafico.pack(pady=20)
frame_grafico.pack_propagate(False)

lbl_estado = tk.Label(root, text="📋 Esperando acción del usuario...", bg="#f2f2f2", fg="gray", font=("Arial", 10))
lbl_estado.pack(pady=10)

root.mainloop()

