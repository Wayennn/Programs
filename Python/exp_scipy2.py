from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

def f(x0, t, m, k, b):
    x, dxdt = x0
    d2xdt2 = -(b*dxdt+k*x)/m
    return [dxdt, d2xdt2]

t = np.arange(0, 10, 0.0001)
x0 = [100, 0]
m = 5
k = 10
b = 2
y = odeint(f, x0, t, args=(m, k, b))

plt.title("Yieeet")
plt.plot(t, [0 for i in np.arange(len(t))], "b:", linewidth=1)
plt.plot(t, y[:,0], "r-", linewidth=2, label="x")
plt.plot(t, y[:,1], "b-", linewidth=2, label="dx/dt")
plt.xlabel("time")
plt.ylabel("meters and meters/second")
plt.legend(loc="upper right")
plt.show()

# def f(x0, t, b):
#     x, v = x0
#     acc = -2*b*t
#     return [v, acc]
#
# a = 4
# b = 2
# x0 = [0, a]
# t = np.arange(0, 4, 0.001)
#
# y = odeint(f, x0, t, args=(b,))
#
# plt.title("Graph of position, velocity, and acceleration")
# plt.plot(t, [0 for i in np.arange(len(t))], "b:", linewidth=1)
# plt.plot(t, y[:,0], "y-", linewidth=1, label="x(t)")
# plt.plot(t, y[:,1], "r-", linewidth=1, label="v(t)")
# plt.plot(t, f(x0, t, b)[1], "b-", linewidth=2, label="a(t)")
# plt.xlabel("time")
# plt.ylabel("meters and meters/second")
# plt.legend()
# plt.show()