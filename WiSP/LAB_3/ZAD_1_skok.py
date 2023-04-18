import numpy as np
import matplotlib.pyplot as plot

h = float(input("Provide h: "))

n = np.linspace(0, 1000, 1000)

u = np.zeros(len(n))
u[len(n)//2:] = 1

def x(n):
  x = 0
  yield x
  for i in range(1,len(n)):
    x = x + h * (-x + u[i - 1])
    yield x

_, ax = plot.subplots(figsize=(10, 5))

ax.plot(n, list(x(n)), label='Odpowiedź')
# ax.plot(n, u, label='Pobudzenie')
ax.legend()

plot.show()