import numpy as np
import matplotlib.pyplot as plot

h = float(input("Provide h: "))

k = 5
n = np.linspace(0, 100, 101)
T=0.1
u = np.zeros(len(n))
u[::10] = 1


def x(n):
  x1 = 0
  yield x1
  x2 = 0
  yield x2
  for i in range(len(n)-2):
    temp = x2
    x2 = 1/T*h**2 * k * u[int(i)] - (1/T*h-2)*x2 - (1/T*h**2 - 1/T*h + 1)*x1 
    x1 = temp
    yield x2


_, ax = plot.subplots(figsize=(10, 5))

ax.plot(n,list(x(n)))
ax.legend()

plot.show()