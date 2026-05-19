import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 1. Configuración inicial
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 200)
line, = ax.plot([], [], lw=2)

ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1, 1)

# 2. Función que actualiza el fotograma 'i'
def animate(i):
    y = np.sin(x + i * 0.1)
    line.set_data(x, y)
    return line,

# 3. Creación de la animación
ani = animation.FuncAnimation(
    fig, animate, frames=100, interval=50, blit=True
)

plt.show()