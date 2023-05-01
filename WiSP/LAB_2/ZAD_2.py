import math
import numpy as np
import matplotlib.pyplot as plot


T = float(input("Provide T: "))
k = float(input("Provide k: "))


t = np.linspace(0, 15, 10000)

y = k * (1 - np.exp(-t/T))

y2 = (k/T) * np.exp(-t/T)

_, ax = plot.subplots(figsize=(10, 5))

ax.plot(t, y2, "black")
ax.plot(t, y, "yellow")
ax.legend()
ax.set_xlabel('time')
ax.set_ylabel('???')

plot.show()