# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 15:17:52 2018

@author: Ben
"""


import numpy as np
from matplotlib import pyplot 

euler = lambda y, f, dx: y + f*dx

tmax = 20
T0 = 10
r = 0.1
Ts = 83
n = 5
dt = np.zeros(n)
temp = np.zeros(n)
#my_color = ['#003366','#663300','#660033','#330066']
#my_color = ['red', 'green', 'blue', 'black']
for j in range(0,n):
    dt[j] = 1/(j+1)
    nsteps = int(tmax/dt[j])    #the arrays will have different size for different time steps
    my_time = np.linspace(dt[j],tmax,nsteps) 
    my_temp = np.zeros(nsteps)
    my_temp[0] = T0
    T = T0
    for i in range(1,nsteps):
        T = euler(T, -r*(T-Ts), dt[j])
        my_temp[i] = T
    temp[j] = my_temp[10*(j+1)]
        
    #pyplot.plot(my_time, my_temp, color=my_color[j-1], ls='-', lw=3)
pyplot.plot(dt, temp,'o')