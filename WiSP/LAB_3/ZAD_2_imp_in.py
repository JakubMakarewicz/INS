import numpy as np
import matplotlib.pyplot as plot
from scipy import signal

h = float(input("Provide h: "))
k = float(input("Provide k: "))

n = np.linspace(0, 10, 10)
dirac = signal.unit_impulse(int(h*1001),30)
values = []

def x(n):
  x1 = k
  yield x1
  x2 = k
  yield x2
  for i in n[:-2]:
    temp = x2
    x2 = h**2*k*dirac[int(i)] - (h**2-h+1)*x1-(h-2)*x2
    print(x2)
    x1 = temp
    yield x2

_, ax = plot.subplots(figsize=(10, 5))

ax.plot(n,list(x(n)))
ax.legend()

plot.show()