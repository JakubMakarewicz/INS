
import numpy as np
import matplotlib.pyplot as plot

h = float(input("Provide h: "))
k = float(input("Provide k: "))

n = np.linspace(0, 1000, 1001)

values = []

def x(n):
  x1 = 0
  yield x1
  x2 = np.sin(1)
  yield x2
  for i in n:
    temp = x2
    x2 = h**2*k*np.sin(i*h) -(h**2-h+1)*x1-(h-2)*x2    
    x1 = temp
    yield x2

_, ax = plot.subplots(figsize=(10, 5))

ax.plot(list(x(n)))
ax.legend()

plot.show()

