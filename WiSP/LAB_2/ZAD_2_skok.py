import math
import numpy as np
import matplotlib.pyplot as plot


T = float(input("Provide T: "))
k = float(input("Provide k: "))


t = np.linspace(0, 1000, 10000)

y = k * (1 - np.exp(-t/T))

_, ax = plot.subplots(figsize=(10, 5))

ax.plot(t, y)
ax.legend()
ax.set_xlabel('time')
ax.set_ylabel('???')

plot.show()