import numpy as np
import matplotlib.pyplot as plt

beta=100
#変換後のG_t
t=np.arange(101)
G_t=-np.exp(-t)/(1+np.exp(-1*beta))

#フーリエ級数型のG_t
n=np.arange(-1000,1001)
w_n=np.pi*(2*n+1)/beta
G_t_real=np.empty(0)
G_t_imag=np.empty(0)
for i in range(101):
    dg=np.exp(-1J*w_n*i)*(1/(1J*w_n-1)-1/(1J*w_n))      #2001個のnumpy配列
    g=np.sum(dg)/beta-1/2
    G_t_real=np.append(G_t_real, g.real)
    G_t_imag=np.append(G_t_imag, g.imag)

#グラフ
plt.plot(t, G_t, label='G_t', marker=".")
plt.plot(t, G_t_real, label='real',marker=".")
plt.plot(t, G_t_imag, label='imagine',marker=".")
plt.legend()
plt.show()
