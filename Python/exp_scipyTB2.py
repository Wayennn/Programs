import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)
import numpy as np
from scipy.integrate import odeint

def f(p0, t, consta, constb, beta):
    p = p0
    d_i = consta[4]-consta[8]
    d_t = consta[5]-consta[8]
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

def ploti(_ax, yr=2013, d=False):
    _ax.set_xlabel("year")
    _ax.set_ylabel("population proportion")
    _ax.set_xticks(np.arange(yr, yr+11, 1))
    if yr==2003:
        _ax.set_yticks(np.arange(0, 0.00401, 0.0005))
        _ax.yaxis.set_minor_locator(MultipleLocator(0.00025))
    elif yr==2013:
        _ax.set_yticks(np.arange(0.00140, 0.00281, 0.0002))
        _ax.yaxis.set_minor_locator(MultipleLocator(0.0001))
    if d:
        _ax.set_yticks(np.arange(0, 0.00251, 0.0005))
        _ax.yaxis.set_minor_locator(MultipleLocator(0.0001))
    _ax.legend()

def plotp(_ax, yr=2013):
    _ax.set_xlabel("year")
    _ax.set_ylabel("population proportion")
    _ax.set_xticks(np.arange(yr, yr+11, 1))
    if yr==2003:
        _ax.set_yticks(np.arange(0, 0.00901, 0.0010))
        _ax.yaxis.set_minor_locator(MultipleLocator(0.0005))
    elif yr==2013:
        _ax.set_yticks(np.arange(0.00250, 0.00501, 0.0005))
        _ax.yaxis.set_minor_locator(MultipleLocator(0.0001))
    _ax.legend()

def fnd(_y1, par, delt):
    if par=="inci":
        return _y1[:, 3]/delt
    elif par=="preva":
        return _y1[:, 3]+_y1[:, 2]

consta = np.array([0.129*24/23, 0.821*24/23, 0.075/20, 0.63/3, 0.2647358, 0.0210358, 0.21, 2192078, 1/67.862, 0.546, 0.0225])
constb = np.array([0.49, 2, 0.8664, 0.7, 0.45])
beta = 11.5

p0 = np.array([0.049, 0.5, 0.0053028, 0.0016072, 0.04409, 0.4, 1669442/83050000])
lb = ["L_A", "L_B", "I", "T", "S_A", "S_B", "N"]
p0[0] = 0.022
t = np.arange(2003, 2013, 0.01)

y = odeint(f, p0, t, args=(consta, constb, beta))

fig, ax = plt.subplots(1, 2, figsize=(15, 6))
fig.suptitle("Fitted Model for Years (2003-2013)", fontsize=20)
ax[0].set_title("Tuberculosis Incidence Rate in the Philippines")
ax[1].set_title("Tuberculosis Prevalence Rate in the Philippines")
ax[0].plot(t, y[:, 3]/constb[4], linewidth=2, label="Incidence rate")
ax[1].plot(t, y[:, 3]+y[:, 2], linewidth=2, label="Prevalence rate")
ploti(ax[0], 2003)
plotp(ax[1], 2003)

t1 = np.arange(2013, 2023, 0.01)

fig1, axs1 = plt.subplots(2, 2, figsize=(15, 10))
fig1.suptitle("Simulated Incidence Rates (Years 2013-2023)", fontsize=20)
axs1[0, 0].set_title("Varied Partial Immunity")
axs1[0, 1].set_title("Varied Vaccine Coverage")
axs1[1, 0].set_title("Varied Treatment Success")
axs1[1, 1].set_title("Varied Treatment Duration")
fig2, axs2 = plt.subplots(2, 2, figsize=(15, 10))
fig2.suptitle("Simulated Prevalence Rates (Years 2013-2023)", fontsize=20)
axs2[0, 0].set_title("Varied Partial Immunity")
axs2[0, 1].set_title("Varied Vaccine Coverage")
axs2[1, 0].set_title("Varied Treatment Success")
axs2[1, 1].set_title("Varied Treatment Duration")

for i in range(2):
    ax[i].set_xlim([2003, 2013])
    for j in range(2):
        axs1[i, j].set_xlim([2013, 2023])
        axs2[i, j].set_xlim([2013, 2023])

constbv = constb.copy()
for i in range(6):
    y1 = odeint(f, y[-1], t1, args=(consta, constbv, beta))
    y1i = fnd(y1, "inci", constbv[4])
    y1p = fnd(y1, "preva", constbv[4])
    axs1[0, 0].plot(t1, y1i, linewidth=2, label="Partial immunity = {:.2f}".format(constbv[0]))
    axs2[0, 0].plot(t1, y1p, linewidth=2, label="Partial immunity = {:.2f}".format(constbv[0]))
    ploti(axs1[0, 0])
    plotp(axs2[0, 0])
    constbv[0] -= 0.04

constbv = constb.copy()
for i in range(6):
    y1 = odeint(f, y[-1], t1, args=(consta, constbv, beta))
    y1i = fnd(y1, "inci", constbv[4])
    y1p = fnd(y1, "preva", constbv[4])
    axs1[0, 1].plot(t1, y1i, linewidth=2, label="Vaccine Coverage = {:.2f}".format(constbv[2]))
    axs2[0, 1].plot(t1, y1p, linewidth=2, label="Vaccine Coverage = {:.2f}".format(constbv[2]))
    ploti(axs1[0, 1])
    plotp(axs2[0, 1])
    constbv[2] += 0.1336/6

constbv = constb.copy()
for i in range(7):
    y1 = odeint(f, y[-1], t1, args=(consta, constbv, beta))
    y1i = fnd(y1, "inci", constbv[4])
    y1p = fnd(y1, "preva", constbv[4])
    axs1[1, 0].plot(t1, y1i, linewidth=2, label="Treatment Success = {:.2f}".format(constbv[3]))
    axs2[1, 0].plot(t1, y1p, linewidth=2, label="Treatment Success = {:.2f}".format(constbv[3]))
    ploti(axs1[1, 0])
    plotp(axs2[1, 0])
    constbv[3] += 0.04

constbv = constb.copy()
for i in range(7):
    y1 = odeint(f, y[-1], t1, args=(consta, constbv, beta))
    y1i = fnd(y1, "inci", constbv[4])
    y1p = fnd(y1, "preva", constbv[4])
    axs1[1, 1].plot(t1, y1i, linewidth=2, label="Treatment Duration = {:.2f} months".format(12/constbv[1]))
    axs2[1, 1].plot(t1, y1p, linewidth=2, label="Treatment Duration = {:.2f} months".format(12/constbv[1]))
    ploti(axs1[1, 1], d=True)
    plotp(axs2[1, 1])
    if constbv[1]==12:
        constbv[1] = 24
    else:
        constbv[1] = (constbv[1]*12)/(12-constbv[1])

plt.show()