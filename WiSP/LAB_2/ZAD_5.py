import matplotlib.pyplot as plt
import numpy as np

m = float(input("Please provide m: "))
b = float(input("Please provide b: "))
k = float(input("Please provide k: "))
x0 = float(input("Please provide x0: "))

# F = m * d^2x/dt^2 + dx/dt + kx
# x(t) = X0e^(−bt/2m) cos(ωt+ϕ).
# ω=√(k/m−(b/2m)^2)
# rozpisac na kartce

def position(t):
  return x0 * np.e ** (-b*t/2*m) * np.cos(t * (np.sqrt((k/m) - ((b / (2 * m)) ** 2))))

t = np.linspace(0, 100, 1000)

_, ax = plt.subplots(figsize=(10, 5))

ax.plot(t, position(t), color="black", label="y=x")

ax.set_xlabel("time(seconds)")
ax.set_ylabel("position(m)")
ax.set_title("Wykres")
ax.legend()
plt.show()