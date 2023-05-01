import matplotlib.pyplot as plt
import numpy as np

m = float(input("Please provide m: "))
b = float(input("Please provide b: "))
k = float(input("Please provide k: "))
F = float(input("Please provide F: "))

def A(t): return (b/(2*m*np.sqrt(k/m-(b**2/(4*m**2))))) * np.exp(-(b*t)/(2*m))
def B(t): return np.sin(np.sqrt(k/m - (b**2/(4*m**2)) * t))
C = (np.tan(np.sqrt(k/m - (b**2/(4*m**2)) / (b/(2*m)))))**(-1)

def position(t):
  return F/m * m/k * (1 - A(t) * B(t) + C)


print(position(int(input("Gimme x: "))))



t = np.linspace(0, 10, 100)
_, ax = plt.subplots(figsize=(10, 5))

ax.plot(t, position(t), color="black", label="y=x")

ax.set_xlabel("time(seconds)")
ax.set_ylabel("position(m)")
ax.set_title("Wykres")
ax.legend()
plt.show()