import numpy as np
import matplotlib.pyplot as plt

n=np.arange(-100,101)
beta=100
w_n=np.pi*(2*n+1)/beta
G_iwn=1/(1J*w_n-1)

plt.plot(n, G_iwn.real, label='real', marker=".")
plt.plot(n, G_iwn.imag, label='imagine',marker=".")
plt.xlabel('w_n')
plt.ylabel('G_iwn')
plt.legend()
plt.show()
