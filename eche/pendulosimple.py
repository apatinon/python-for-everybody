#pendulo rígido
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

l = float(input("ingrese la longitud del pendulo en metros "))
m = float(input("ingrese la masa del pendulo en kilogramos "))
g = 9.8
theta_grados = float(input("ingrese el ángulo incial del pendulo en grados "))
theta = math.radians(theta_grados)
omega = 0

def derivadadeomega(g, l, theta):
    return -(g/l)*math.sin((theta))

#METODO DE EULER-CROMER PARA EL CALCULO DE DERIVADAS
#parametros de el metodo de euler-cromer
dt = 0.01
tiempo_total = 10
n = int(tiempo_total / dt) #numero de pasos de siempre, nada raro
#listas vacías
tiempos = [] 
thetas = []
omegas = []
#euler-cromer
t = 0 
for i in range(n):
    alpha = -(g/l) * math.sin(theta) #ecuacion que rige la velocidad angular
    omega = omega + alpha * dt # actualizacion de esa velocidad angular
    theta = theta + omega * dt # actualizacion del angulo
    #guardamos estos nuevos datos
    tiempos.append(t)
    thetas.append(theta)
    omegas.append(omega)
    #y avanzamos en el tiempo
    t = t+dt
#plt.plot(tiempos, thetas)

#plt.title("Péndulo simple")
#plt.xlabel("Tiempo (s)")
#plt.ylabel("Ángulo (rad)")

#plt.grid(True)

#plt.show()

#LA ANIMACIÓN
#detalles iniciales de la animación
fig, ax = plt.subplots()
ax.set_xlim(-l-0.5, l+0.5)
ax.set_ylim(-l-0.5, l+0.5)
ax.set_aspect('equal')

cuerda, = ax.plot([], [], lw=2)
masa, = ax.plot([], [], 'o', markersize=12)

#funcion de animacion
x_limite = 0
y_limite = 0
def animate(i):
    theta_actual = thetas[i]
    x = x_limite + l* math.sin(theta_actual)
    y = y_limite - l * math.cos(theta_actual)
    cuerda.set_data([0,x], [0,y])
    masa.set_data([x], [y])
    return cuerda, masa

animacion = animation.FuncAnimation(
    fig, animate, frames=len(thetas), interval=10, blit=True
)
plt.grid(True)
plt.show()
