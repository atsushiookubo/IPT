#２次関数の積分

from scipy import integrate
import numpy as np

# 関数定義
a = -2
b =  3
f = lambda x: x**2

#積分（真）
quad, quad_err = integrate.quad(f, a, b)

#積分（台形則）
n=1000  #分点の数
x=np.linspace(a, b, n, endpoint=True)
F=(np.delete(f(x),0)+np.delete(f(x),n-1))*(b-a)/(2*(n-1))
S=np.sum(F)

# 積分（ガウスルジャンドル）
n = 100 #n個の分点
x, w = np.polynomial.legendre.leggauss(n)  #x:分点、w:重み
X=(b-a)/2*x+(b+a)/2
gauss = (b-a)/2*sum(w * f(X))

# 積分(２重指数型積分)
h=1/20
m=np.arange(-100,101)
g=np.pi/2*np.sinh(m*h)
dDE=(b-a)/2*f((b-a)/2*np.tanh(g)+(a+b)/2)*np.cosh(m*h)/(np.cosh(g))**2
DE=np.pi*h/2*np.sum(dDE)


#積分値出力
print("真:{0}(推定誤差:{1})\n台形則:{2}\nガウスルジャンドル:{3}\n二重指数型積分:{4}".format(quad,quad_err,S, gauss,DE))
