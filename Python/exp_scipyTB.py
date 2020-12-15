import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

def f(p0, t,):
    p = p0
    #                     0eps,       1k,          2v,       3gam,   4mu_i,      5mu_t,    6h,    7A,      8mu,    9rho,   10w
    consta = np.array([0.129*24/23, 0.821*24/23, 0.075/20, 0.63/3, 0.2647358, 0.0210358, 0.21, 2192078, 1/67.862, 0.546, 0.0225])
    d_i = consta[4]-consta[8]
    d_t = consta[5]-consta[8]
    #                  0chi,1phi, 2i,  3eta, 4delt
    constb = np.array([0.49, 2, 0.8664, 0.7, 0.45])
    beta = 11.5
    c1 = beta*consta[9]*(p[2] + consta[6]*p[3])
    c2 = p[6] - consta[8] - d_i*p[2] - d_t*p[3]
    dLAdt = c1*(p[4]+constb[0]*(p[5]+p[1])) - p[0]*(consta[0]+consta[1]+consta[8]+c2)
    dLBdt = consta[1]*p[0] + consta[3]*p[2] - p[1]*(constb[0]*c1+consta[2]+consta[8]+c2)
    dIdt = consta[0]*p[0] + consta[2]*p[1] + consta[10]*p[3] - p[2]*(consta[3]+constb[4]+consta[4]+c2)
    dTdt = constb[4]*p[2] - p[3]*(constb[3]*constb[1]+consta[10]+consta[5]+c2)
    dSAdt = (1-constb[2])*p[6] - p[4]*(c1+consta[8]+c2)
    dSBdt = constb[2]*p[6] + constb[3]*constb[1]*p[3] - p[5]*(constb[0]*c1+consta[8]+c2)
    dNdt = -p[6]*c2
    return np.array([dLAdt, dLBdt, dIdt, dTdt, dSAdt, dSBdt, dNdt])

p0 = np.array([0.049, 0.5, 0.0053028, 0.0016072, 0.04409, 0.4, 1669442/83050000])
#       0,     1,    2,   3,    4,     5,    6
lb = ["L_A", "L_B", "I", "T", "S_A", "S_B", "N"]

t = np.arange(2003, 2013, 0.01)

# adjustment
p0[0] -= 0.021

y = odeint(f, p0, t)

plt.title("Tubercolosis")
# for i in range(np.shape(y)[1]):
#     plt.plot(t, y[:, i], linewidth=2, label=lb[i])

# plt.plot(t, y[:, 2], linewidth=2, label="I")
# plt.plot(t, y[:, 3], linewidth=2, label="T")

plt.plot(t, y[:, 3]+y[:, 2], linewidth=2, label="prevalence rate")
plt.plot(t, y[:, 3]/0.45, linewidth=2, label="incidence rate")
plt.xlabel("year")
plt.ylabel("population proportion")
plt.xticks(np.arange(2003, 2013.1, 1))
plt.yticks(np.arange(0, 0.0101, 0.0005))
plt.legend()
plt.show()

t = np.arange(2013, 2023, 0.001)

p1 = y[-1]