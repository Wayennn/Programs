import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.integrate import odeint

def f(p, v, T, m):
    k = 1.380649*(10**(-23))
    pi = math.pi
    p = 4*pi*((m/(pi*k*T))**(3/2))*(v**2)*np.exp(-(m*(v**2))/(k*T))
    return p

v = np.arange(0, 10000, 1)
m = 1.67*(10**(-27))
T = np.arange(73, 1074, 200)
# y = [odeint(f, 0, v, args=(T[i], m)) for i in range(len(T))]

plt.title("Maxwell-Boltzmann Distribution")
for i in range(len(T)):
    plt.plot(v, [f(0, v1, T[i], m) for v1 in v], linewidth=2, label=str(T[i]) + " K")
    # plt.plot(v, y[i], linewidth=2, label=str(T[i]) + " K")
plt.xlabel("v (m/s)")
plt.ylabel("relative proportion")
plt.legend()
plt.show()