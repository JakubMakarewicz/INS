import math
import numpy as np
import matplotlib.pyplot as plot


D = 2
T = float(input("Provide T: "))
k = float(input("Provide k: "))

#Ty ̇ + y = ku
#(y0 − k)e− tT + k
def y2(time):
  return -k * (1 - np.exp(-(time - D)/T)) * ((time - D) >= 0)


t = np.linspace(0, 1000, 10000)

y1 = k * (1 - np.exp(-t/T))
y2Func = np.vectorize(y2)
y2Calculated = y2Func(t)

_, ax = plot.subplots(figsize=(10, 5))


ax.plot(t, y1)
ax.legend()
ax.set_xlabel('time')
ax.set_ylabel('???')

plot.show()