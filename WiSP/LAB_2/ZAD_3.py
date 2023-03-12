import numpy as np
import matplotlib.pyplot as plt

# pobranie wartości parametrów od użytkownika
T = float(input("Podaj stałą czasową inercji T: "))
K = float(input("Podaj wzmocnienie członu całkującego K: "))

# funkcja obliczająca odpowiedź skokową
def step_response(t):
    y = np.zeros_like(t)
    for i in range(len(t)):
        if t[i] >= 0:
            y[i] = (1/K)*(1 - (1/np.sqrt(1-4*T/K))*np.exp(-t[i]/(2*T)*(1+np.sqrt(1-4*T/K))) + 
                    (1/np.sqrt(1-4*T/K))*np.exp(-t[i]/(2*T)*(1-np.sqrt(1-4*T/K))))
    print(y)
    return y

# funkcja obliczająca odpowiedź impulsową
def impulse_response(t):
    y = np.zeros_like(t)
    y[0] = 1/K
    for i in range(1,len(t)):
        y[i] = y[i-1] + (1/K)*(t[i]-t[i-1])*y[i-1]/T
    return y

# czas symulacji
t = np.linspace(0,10,1000)

# wywołanie funkcji i rysowanie wykresów
plt.subplot(2,1,1)
plt.plot(t, step_response(t))
plt.title("Odpowiedź skokowa")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")

plt.subplot(2,1,2)
plt.plot(t, impulse_response(t))
plt.title("Odpowiedź impulsowa")
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda")

plt.tight_layout()
plt.show()