from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent


def graficos(resultados):
    # Gráfico: promedios por programa
    df_programa = resultados['por_programa']
    plt.figure()
    df_programa['promedio'].plot(kind='bar', title="Promedio por Programa")
    plt.ylabel("Promedio")
    plt.tight_layout()
    plt.savefig(BASE / "grafico_programa.png")
    plt.close()

    # Gráfico: asignaturas mayor variabilidad
    df_asig = resultados['asignaturas_mayor_variabilidad']
    plt.figure()
    df_asig['desviacion'].plot(kind='bar', title="Asignaturas con Mayor Variabilidad")
    plt.ylabel("Desviación Estándar")
    plt.tight_layout()
    plt.savefig(BASE / "grafico_variabilidad.png")
    plt.close()


def tabla_pdf(pdf, df, x, y, max_width=520):
    # Estilo para salto de línea en texto largo
    style = ParagraphStyle(name="Tabla", fontSize=8, alignment=1)

    # Convertir fila por fila a Paragraph para que se vea el texto completo
    data = [[Paragraph(str(col), style) for col in df.columns]]
    for row in df.round(2).values.tolist():
        data.append([Paragraph(str(cell), style) for cell in row])

    # Ajuste uniforme de ancho
    col_widths = [max_width / len(df.columns)] * len(df.columns)

    table = Table(data, colWidths=col_widths)

    table.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0), colors.HexColor("#003366")),
        ('TEXTCOLOR',(0,0),(-1,0), colors.white),
        ('GRID',(0,0),(-1,-1), 0.5, colors.black),
        ('FONTNAME',(0,0),(-1,0), 'Helvetica-Bold'),
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('BOTTOMPADDING',(0,0),(-1,0), 6),
        ('LEFTPADDING',(0,0),(-1,-1), 2),
        ('RIGHTPADDING',(0,0),(-1,-1), 2),
    ]))

    w, h = table.wrapOn(pdf, x, y)
    table.drawOn(pdf, x, y - h)


def generar_pdf(resultados):
    graficos(resultados)

    pdf_path = BASE / "Informe_Analitica_Ejecutivo.pdf"
    pdf = canvas.Canvas(str(pdf_path), pagesize=A4)
    width, height = A4

    # ✅ PORTADA
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(80, height - 100, "Informe Ejecutivo de Analítica Institucional")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(80, height - 130, "Rendimiento Académico - Universidad ECCI")
    pdf.drawString(80, height - 150, "Generado automáticamente con Python")
    pdf.showPage()

    # ✅ GRÁFICO 1
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(80, height - 50, "Promedio por Programa")
    pdf.drawImage(BASE / "grafico_programa.png", 50, height - 400, width=500, preserveAspectRatio=True)
    pdf.showPage()

    # ✅ GRÁFICO 2
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(80, height - 50, "Asignaturas con Mayor Variabilidad")
    pdf.drawImage(BASE / "grafico_variabilidad.png", 50, height - 400, width=500, preserveAspectRatio=True)
    pdf.showPage()

    # ✅ TABLA 1 - Programas (índice convertido a columna)
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, height - 50, "Resumen por Programa")
    df_prog = resultados['por_programa'].reset_index().rename(columns={'programa': 'Programa'})
    tabla_pdf(pdf, df_prog, 50, height - 100)
    pdf.showPage()

    # ✅ TABLA 2 - Asignaturas (índice convertido a columna)
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, height - 50, "Asignaturas con Mayor Variabilidad")
    df_asig = resultados['asignaturas_mayor_variabilidad'].reset_index().rename(columns={'asignatura': 'Asignatura'})
    tabla_pdf(pdf, df_asig, 50, height - 100)
    pdf.showPage()

    # ✅ CONCLUSIONES
    riesgo = resultados['porcentaje_en_riesgo']
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, height - 80, "Conclusiones del Análisis")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, height - 120, f"- {riesgo}% de estudiantes están en riesgo académico (promedio < 3.0).")
    pdf.drawString(50, height - 150, "- Las asignaturas con mayor variabilidad requieren atención prioritaria.")
    pdf.drawString(50, height - 180, "- Se recomienda fortalecer tutorías y seguimiento a grupos críticos.")

    pdf.save()
    print(f"✅ PDF generado correctamente: {pdf_path}")


if __name__ == "__main__":
    from analysis_institucional import cargar_fuentes, limpiar_datos, integrar, calcular_estadisticas
    
    df_enroll, df_grades, df_subj = cargar_fuentes()
    df_enroll, df_grades_clean = limpiar_datos(df_enroll, df_grades)
    df_integrado = integrar(df_enroll, df_grades_clean, df_subj)
    resultados = calcular_estadisticas(df_integrado)

    generar_pdf(resultados)


