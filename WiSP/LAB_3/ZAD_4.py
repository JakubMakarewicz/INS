import numpy as np
import matplotlib.pyplot as plot

x0 = 1
y0 = 1
r =  5
h =  0.0001

v = [10., -1., -7., -2., -1., 4., 4., 4., -5., -3.]
p = [10., 20., 40., 30., 20., 10., 10., 10., 30., 20.]

def f(n):
  x = x0
  y = y0
  yield x,y
  for i in n:
    x = x + (r * x * int(x>0) - h * y - p[int(i)] - v[int(i)])
    y = y + v[int(i)]
    yield x,y
    
n = np.linspace(0, 9, 10)

_, ax = plot.subplots(figsize=(6, 6))
_, ax2 = plot.subplots(figsize=(6, 6))

positions = list(f(n))

ax.plot(list(map(lambda x: x[1], positions)), label="Składowana przenica(T)")
ax.plot(list(map(lambda x: x[0], positions)), label="Saldo konta")
ax2.plot(n, v, label="Tempo sprzedaży")
ax2.plot(n, p, label="Cena/T")
ax.legend()
ax2.legend()
plot.show()