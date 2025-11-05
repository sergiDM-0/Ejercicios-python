import numpy as np
import plotly.graph_objects as go       

# Parámetros
x_vals = np.linspace(-1, 1, 50)
theta = np.linspace(0, 2*np.pi, 30)

# Malla
X, Theta = np.meshgrid(x_vals, theta)

# Radio de giro: distancia desde x hasta x = -1
R = X + 1

# Altura Y: promedio entre las dos curvas (para superficie media)
Y_lower = np.where(X < 0, X, X**2)
Y_upper = np.where(X < 0, X**2, X)
Y = (Y_lower + Y_upper) / 2

# Coordenadas 3D después de rotar alrededor de x = -1
Z = R * np.cos(Theta)
X_3D = R * np.sin(Theta) - 1  # trasladamos para que el eje sea x = -1
Y_3D = Y

# Crear superficie 3D
fig = go.Figure(data=[go.Surface(
    x=X_3D,
    y=Y_3D,
    z=Z,
    colorscale='Viridis',
    surfacecolor=Y_3D,  # color por altura
    opacity=0.8
)])

# Configuración de la escena
fig.update_layout(
    title='Sólido de Revolución: Región entre y=x, y=x² girada alrededor de x=-1',
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        camera=dict(
            eye=dict(x=1.5, y=1.5, z=1.5)  # ángulo inicial
        )
    ),
    width=900,
    height=700,
    margin=dict(r=20, l=10, b=10, t=40)
)

# Mostrar gráfico interactivo
fig.show()