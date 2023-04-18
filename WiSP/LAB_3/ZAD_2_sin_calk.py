
import numpy as np
import matplotlib.pyplot as plot

h = float(input("Provide h: "))
k = float(input("Provide k: "))

n = np.linspace(0, 1000, 1001)

values = []

def x(n):
  x1 = k
  yield x1
  x2 = 4.9
  yield x2
  for i in n:
    temp = x2
    x2 = h**2*k*np.sin(i*h) -(1-h)*x1-(h-2)*x2    
    x1 = temp
    yield x2

_, ax = plot.subplots(figsize=(10, 5))

ax.plot(list(x(n)))
ax.legend()

plot.show()

