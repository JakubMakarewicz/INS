import numpy as np
import matplotlib.pyplot as plot

m = float(input("Please provide m: "))

t = np.linspace(0, 100000, 1000)
T = 5730


# oszacowac k (po x latach po prostu)
y = m * np.exp(np.log(1/2) * (t / T))

_, ax = plot.subplots(figsize=(10, 5))

ax.plot(t, y)
ax.legend()
ax.set_xlabel('Time(year)')
ax.set_ylabel('Mass')

plot.show()