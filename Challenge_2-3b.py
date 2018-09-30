# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 15:29:59 2018

@author: Ben
"""

import numpy as np

g = 9.8            # g acceleration
mass = 0.01        # mass of the particle          
v0 = 0.            # initial velocity
R = 6.37e6           # radius of Earth
dt = 0.1           # time step

class particle(object):
    
    def __init__(self, mass=1., y=0., v=0.):
        self.mass = mass
        self.y = y
        self.v = v
        
    def euler(self, f, dt):
        self.y = self.y + self.v*dt
        self.v = self.v + f/self.mass*dt
        
    def euler_cromer(self, f, dt):
        self.v = self.v + f/self.mass*dt
        self.y = self.y + self.v*dt
        
p = particle(mass, y0, v0)

y0_array = np.linspace(1500000,1600000,1000,endpoint=False)

for y0 in y0_array:
    y = [y0]                # since we do not know the size of the arrays, we define first a python list
    v = [v0]                # the append method is more efficient for lists than arrays
    t = [0.]
    
    p.y = y0
    p.v = v0

    while p.y > 0.:
    
        gforce = mass*g / (1+(p.y/R)**2)        # postition dependent gravitational force
        fy = -gforce
        p.euler(fy, dt)
        y.append(p.y)
        v.append(p.v)
        t.append(t[-1]+dt)
    
    t_data = np.array(t)              # we convert the list into a numpy array for plotting
    y_data = np.array(y)
    v_data = np.array(v)
    
    v1_f = v_data[len(v_data)-1] 
   
    y = [y0]                # since we do not know the size of the arrays, we define first a python list
    v = [v0]                # the append method is more efficient for lists than arrays
    t = [0.]
    
    p.y = y0
    p.v = v0
    
    while p.y > 0.:
    
        gforce = mass*g             # constant gravitational force 
        fy = -gforce
        p.euler(fy, dt)
        y.append(p.y)
        v.append(p.v)
        t.append(t[-1]+dt)
    
    t_data = np.array(t)            # we convert the list into a numpy array for plotting
    y_data = np.array(y)
    v_data = np.array(v)
    
    v2_f = v_data[len(v_data)-1] 
    
    percent_diff = abs((v2_f - v1_f)/v2_f)*100
    
    if (percent_diff >= 1):
        
        break
        
yp = y0 

print('y0 = %.f meters \n' % (yp))