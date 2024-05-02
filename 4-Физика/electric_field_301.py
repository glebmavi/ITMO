from math import sqrt

import numpy as np
import matplotlib.pyplot as plt

# Charges Q = (x, y, q), where x, y are the coordinates of the charge and q is the charge value
Q = [(0, 0, 1), (4, 0, 1), (2, sqrt(3)*2, -1)]

# Define the area of the simulation
x1, y1 = -3, -3
x2, y2 = 7, 7

# Define the resolution of the simulation
resolution = 10

# Create the grid
m, n = resolution * (y2 - y1), resolution * (x2 - x1)
x, y = np.linspace(x1, x2, n), np.linspace(y1, y2, m)
x, y = np.meshgrid(x, y)

# Calculate the electric field at each point
Ex = np.zeros((m, n))
Ey = np.zeros((m, n))

# Coulomb's constant
k = 9 * 10 ** 9

for j in range(m):
    for i in range(n):
        xp, yp = x[j][i], y[j][i]
        for q in Q:
            deltaX = xp - q[0]
            deltaY = yp - q[1]

            distance = (deltaX ** 2 + deltaY ** 2) ** 0.5

            E = (k * q[2]) / (distance ** 2)
            Ex[j][i] += E * (deltaX / distance)
            Ey[j][i] += E * (deltaY / distance)

fig, ax = plt.subplots()
ax.set_aspect('equal')

# Plot the charges
ax.scatter([q[0] for q in Q], [q[1] for q in Q],
           c=['red' if q[2] > 0 else 'blue' for q in Q],
           s=[abs(q[2]) * 20 for q in Q],
           zorder=1)

# Label the charges
for q in Q:
    ax.text(q[0] + 0.1, q[1] - 0.3, '{} Кл'.format(q[2]),
            color='black',
            zorder=2)

ax.streamplot(x, y, Ex, Ey, linewidth=0.5, density=1, zorder=0)

plt.title('Силовые линии электрического поля')
plt.show()
