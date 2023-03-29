import numpy as np
import matplotlib.pyplot as plot

m = float(input("Please provide m0: "))

t = np.linspace(0, 100000, 1000)
T = 5730
k = np.log2(1/2)/5730

y = m * np.exp(k*t)

_, ax = plot.subplots(figsize=(10, 5))

ax.plot(t, y)
ax.legend()
ax.set_xlabel('Time(year)')
ax.set_ylabel('Mass')

plot.show()