from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import math

def f(x0, t, r):
    x, dxdt = x0
    k = 9.8/r
    d2xdt2 = -k*math.sin(x)
    return [dxdt, d2xdt2]

t = np.arange(0, 10, 0.01)
r = 1
x0 = [math.pi-0.01, 0]
y = odeint(f, x0, t, args=(r,))

plt.title("Yieeet")
plt.plot(t, y[:,0], "r-", linewidth=2, label="x")
plt.plot(t, y[:,1], "b-", linewidth=2, label="dx/dt")
plt.xlabel("time")
plt.ylabel("radians")
plt.legend()
plt.show()