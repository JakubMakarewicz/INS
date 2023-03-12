import numpy as np
import matplotlib.pyplot as plt

# Parametry członu
T = float(input("Podaj czas stały inercji T: "))
k = float(input("Podaj wzmocnienie k: "))

# Czas symulacji
dt = 0.01  # krok czasowy
t = np.arange(0, 25*T, dt)  # czas symulacji

# Wejście skokowe (jednostkowe)
u = np.ones(len(t))

# Rozwiązanie równania różniczkowego metodą Eulera
x = np.zeros(len(t))  # wyjście członu
for i in range(1, len(t)):
    dxdt = (k*u[i-1] - x[i-1])/T
    x[i] = x[i-1] + dxdt * dt

# Odpowiedź skokowa
plt.plot(t, x)
plt.xlabel('Czas [s]')
plt.ylabel('Wyjście członu')
plt.title('Odpowiedź skokowa')
plt.grid(True)
plt.show()

# Wejście impulsowe (delta Diraca)
u = np.zeros(len(t))
u[0] = 1/dt

# Rozwiązanie równania różniczkowego metodą Eulera
x = np.zeros(len(t))  # wyjście członu
for i in range(1, len(t)):
    dxdt = (ku[i-1] - x[i-1])/T
    x[i] = x[i-1] + dxdt*dt

# Odpowiedź impulsowa
plt.plot(t, x)
plt.xlabel('Czas [s]')
plt.ylabel('Wyjście członu')
plt.title('Odpowiedź impulsowa')
plt.grid(True)
plt.show()