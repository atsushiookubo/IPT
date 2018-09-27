import numpy as np
import matplotlib.pyplot as plt

beta=100
t=np.arange(101)
G_t=-np.exp(-t)/(1+np.exp(-1*beta))


plt.plot(t, G_t, marker=".")
plt.show()
