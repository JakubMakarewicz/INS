import matplotlib.pyplot as plt
import numpy as np

r = float(input("Please provide r: "))
vr = float(input("Please provide Vp: "))
vl = float(input("Please provide Vl: "))

rotation = 1/r * (vr - vl)

x = np.linspace(0, 100, 100) 

_, ax = plt.subplots(figsize=(10, 5))

ax.plot(x, -rotation * x, color="yellow", label="y=x")

ax.set_xlabel("time(seconds)")
ax.set_ylabel("rotation(degrees)")
ax.set_title("Wykres")
ax.legend()
plt.show()