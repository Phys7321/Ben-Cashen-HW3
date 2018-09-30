# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 13:35:11 2018

@author: Ben

Free fall of particle under influence of position dependent gravitational field 
with no drag force
"""

import numpy as np
from matplotlib import pyplot

g = 9.8            # g acceleration
mass = 0.01        # mass of the particle
y0 = 300.          # initial position
v0 = 0.            # initial velocity
vt = 30.           # terminal velocity
R = 6.37e6           # Radius of Earth
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

y = [y0] # since we do not know the size of the arrays, we define first a python list
v = [v0] # the append method is more efficient for lists than arrays
t = [0.]

while p.y > 0.:
    
    gforce = mass*g / (1+(p.y/R)**2) #Gravitational force depends on y 
    fy = -gforce
    p.euler(fy, dt)
    y.append(p.y)
    v.append(p.v)
    t.append(t[-1]+dt)
    
t_data = np.array(t) # we convert the list into a numpy array for plotting
y_data = np.array(y)
v_data = np.array(v)

#for i in range(0,t_data.size):
#    print (i,t_data[i], y_data[i], v_data[i])

pyplot.plot(t_data, v_data, color="#DC143C", ls='-', lw=3)
pyplot.xlabel('time(s)')
pyplot.ylabel('velocity(m/s)');

v_final = v_data[len(v_data)-1] 

print('Velocity of impact = %f m/s \n' % (v_final))
