import matplotlib.pyplot as plt
import numpy as np

def f(x, _lamb, _d, _a):
    _t = np.pi*np.sin(x)/_lamb
    return ((np.cos(_t*_d))*(np.sin(_t*_a))/(_t*_a))**2

def g(x1, _lamb1, _a1):
    _t1 = np.pi*np.sin(x1)/_lamb1
    return ((np.sin(_t1*_a1))/(_t1*_a1))**2

x = np.arange(-2*np.pi, 2*np.pi, 0.0001)
lamb = 500*(10**(-9))
d = 0.0250*(10**(-3))
a = 0.0050*(10**(-3))

fig, ax = plt.subplots(figsize=(160, 8))
ax.plot(x, f(x, lamb, d, a), linewidth=2)
ax.plot(x, g(x, lamb, a), "r--", linewidth=2)
ax.set_xlim([-np.pi/2, np.pi/2])
ax.set_xticks(np.arange(-np.pi/2, np.pi/2, np.pi/18))
ax.set_ylim([0, 1])
ax.set_xlabel("Angle in radians")
ax.set_ylabel("Fraction of maximum intensity")
plt.show()