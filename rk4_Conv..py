# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 18:38:09 2018

@author: Ben
"""

import numpy as np
from matplotlib import pyplot as pyl
from diffeq import rk4

f = lambda T,t : -r*(T-Ts)
tmax = 60.
T0 = 10.
r = 0.1
Ts = 83.
n = 5
dt = np.zeros(n)
temp = np.zeros(n)

for j in range(0,n):
    dt[j] = 1/(j+1)
    nsteps = int(tmax/dt[j])    #the arrays will have different size for different time steps
    T = T0
    my_temp , my_time = rk4(f,0,tmax, nsteps)
    temp[j] = my_temp[10*(j+1)]

pyl.plot(dt, temp,'o')
pyl.xlabel('dt')
pyl.ylabel('Temp.')