"""
The idea to solve SDE from 
https://www.pik-potsdam.de/members/franke/lecture-sose-2016/introduction-to-python.pdf
"""

import numpy as np
import matplotlib.pyplot as plt
"""
Potential 


"""
def x_t(x, t):
    return x-x*x*x

"""
cosine term
"""
def cos_t(y, t,w):
    return math.cos(w*t)

"""
Gaussian proces
"""
def dW(delta_t):
    return np.random.normal(0, 1)

"""
Parameters
"""
N=1000
dt=0.002
ts =np.linspace(0,N*dt,N)
ys = np.zeros(N + 1)
y_init=np.random.normal(0,1)
ys[0] = y_init
t_init =0
w=10
D=45
K=100
A=320
for i in range(1, ts.size):
    t = t_init + (i - 1) * dt
    y = ys[i - 1]
    ys[i] = y + (K*x_t(y, t)+A*cos_t(y,t,w))*dt + D*dt*dW(dt)
plt.plot(ts[0:N], ys[0:N])
