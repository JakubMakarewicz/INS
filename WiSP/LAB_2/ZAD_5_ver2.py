import matplotlib.pyplot as plt
import numpy as np

m = float(input("Please provide m: "))
b = float(input("Please provide b: "))
k = float(input("Please provide k: "))
w = float(input("Please provide w: "))
F = float(input("Please provide F: "))
y = float(input("Please provide y: "))



# def position(t):
#   return F / (m* (k/m - w**2)) * np.cos(w* t - y) * np.exp(-b*t/(2*m))
# 
def cos(t): 
    return np.cos(w*t-y)

def sin(t):
    return np.sin(w*t - y)

n=b/(2*m)

def position(t):
  return (F * cos(t)) / (m * (k/m - w**2) * cos(t) - (2 * n * sin(t)))

t = np.linspace(0,5, 1000)

_, ax = plt.subplots(figsize=(10, 5))

ax.plot(t, position(t), color="black", label="y=x")

ax.set_xlabel("time(seconds)")
ax.set_ylabel("position(m)")
ax.set_title("Wykres")
ax.legend()
plt.show()