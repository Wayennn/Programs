import matplotlib.pyplot as plt
import numpy as np

n = np.arange(10)
dat = np.random.randint(0, 500, size=(3, n.size))
yrs = 2000 + n

fig, ax = plt.subplots(figsize=(5, 3))
ax.stackplot(yrs, dat, labels=["luzon", "visayas", "mindanao"])
ax.set_title("blebleble")
ax.legend(loc="upper left")
ax.set_ylabel("blelbe amount")
ax.set_xlim(xmin=yrs[0], xmax=yrs[-1])
fig.tight_layout()
plt.show()
