from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def f(p,t, a, b):
    s, i, r = p
    dSdt = -a*i*s
    dIdt = a*i*s - b*i
    dRdt = b*i
    return [dSdt, dIdt, dRdt]

t = np.arange(0, 10, 0.0001)

p0 = [0.99999, 0.000001, 0]
a = 10
b = 1
y = odeint(f, p0, t, args=(a, b))
plt.title("S-I-R Model of [insert disease]")
plt.plot(t,y[:,0],'y-',linewidth=2, label="Susceptibles")
plt.plot(t,y[:,1],'r-',linewidth=2, label="Infected")
plt.plot(t,y[:,2],'g-',linewidth=2, label="Removed")
plt.xlabel("time")
plt.ylabel("Relative population")
plt.legend()
plt.show()