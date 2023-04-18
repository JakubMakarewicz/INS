import numpy as np
import matplotlib.pyplot as plot

h = float(input("Provide h: "))

n = np.linspace(0, 100, 100)

u = np.zeros(len(n))
u[0] = 1/h

def x(n):
  x = 0
  yield x
  for i in range(1,len(n)):
    x = x + h * (-x + u[i - 1]) / 2
    yield x

_, ax = plot.subplots(figsize=(10, 5))

ax.plot(n, list(x(n)), label='Odpowiedź')
# ax.plot(n, u, label='Pobudzenie')
ax.legend()

plot.show()