# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 16:42:19 2018
@author: Tom K
"""
import numpy as np
from matplotlib import pyplot as pyl

def rk2(func,a,b,N):
    h = (b-a)/N

    tpoints = np.arange(a,b,h)
    xpoints = []

    x = 0.0
    for t in tpoints:
        xpoints.append(x)
        k1 = h*func(x,t)
        k2 = h*func(x+0.5*k1,t+0.5*h)
        x += k2

    pyl.plot(tpoints,xpoints)
    pyl.xlabel("t")
    pyl.ylabel("x(t)")
    pyl.show()
    return xpoints

def rk4(func,a,b,N):
    h = (b-a)/N

    tpoints = np.arange(a,b,h)
    xpoints = []

    x = 10.0
    for t in tpoints:
        xpoints.append(x)
        k1 = h*func(x,t)
        k2 = h*func(x+0.5*k1,t+0.5*h)
        k3 = h*func(x+0.5*k2,t+0.5*h)
        k4 = h*func(x+k3,t+h)
        x += (k1+2*k2+2*k3+k4)/6

    #pyl.plot(tpoints,xpoints)
    #pyl.xlabel("t")
    #pyl.ylabel("x(t)")
    #pyl.show()
    return (xpoints, tpoints)

