#---main----

import numpy as np
import matplotlib.pyplot as plt



# what i struggled with : i made x_s an int object which must messed things up when being added to float v.
#i didnt have enough trials.
x_s = []
f_s = []
v_s = []
t_s = []
x = np.array([100.,70.])
v = np.array([-0.2, 0.3])
t = 0
dt = 2
G = 1
M = 10
m = 1

A = -G*M*m



#x is numpy
def update_f(x, A):
    f = A * x/((np.sqrt(np.sum(x**2))))**3
    return f


def update_x(x_0, v):
     return x_0 + dt*v


def update_v(v_0, f, m):
    return v_0 + dt * f / m

def update_t(t, dt):
    return t+dt



#i dont understand why changing the no. of iterations changes how the orbit looks
for i in range(10000):
    x_s.append(x)
    v_s.append(v)
    t_s.append(t)
    x = update_x(x, v)
    f = update_f(x,A)
    v = update_v(v, f, m)
    t = update_t(t, dt)

    #e = 1/2 *m* np.sqrt(v[0]**2+v[1]**2) - G*M*m/np.sqrt(np.sum(x**2))

    #E.append(e)

#plt.plot(t_s, E)
x = np.stack(x_s)
plt.plot(x[:,0], x[:,1])
plt.show()



#-------------------------leapfrog method---------------
x = np.array([100.,70.])
v = np.array([-0.2, 0.3])
t = 0

x_s = []
f_s = []
v_s = []
t_s = []

for i in range(10000):
    x_s.append(x)
    v_s.append(v)
    t_s.append(t)
    x = update_x(x, v/2)
    t = update_t(t, dt/2)

    f = update_f(x,A)

    v = update_v(v, f, m)

    x = update_x(x,v/2)

    t = update_t(t, dt / 2)

    #e_total = 1/2 *m* np.sqrt(v[0]**2+v[1]**2) - G*M*m/np.sqrt(np.sum(x**2))
    #E.append(e_total)
    #ke = 1/2 *m* np.sqrt(np.sum(v**2))
    #KE.append(ke)
    #gpe=-G*m*M/np.sqrt((np.sum(x**2)))
    #GPE.append(gpe)




x = np.stack(x_s)

plt.plot(x[:,0], x[:,1])      # x[:,0] = x-coordinate, x[:,1] = y-coordinate
plt.show()
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Orbit")


#---------------------different trajectories



v_list = [np.array([-0.2, 0.3]), np.array([0.2, -0.3]), np.array([-0.2, -0.3]), np.array([0.2, 0.3]), np.array([-0.3, 0.2]), np.array([0.3, -0.2])]



for v in v_list:
    x_s = []
    f_s = []
    v_s = []
    t_s = []
    t = 0
    x = np.array([100., 70.])
    for i in range(10000):
        x_s.append(x)
        v_s.append(v)
        t_s.append(t)
        x = update_x(x, v/2)
        t = update_t(t, dt/2)

        f = update_f(x,A)

        v = update_v(v, f, m)

        x = update_x(x,v/2)

        t = update_t(t, dt / 2)

        #e_total = 1/2 *m* np.sqrt(v[0]**2+v[1]**2) - G*M*m/np.sqrt(np.sum(x**2))
        #E.append(e_total)
        #ke = 1/2 *m* np.sqrt(np.sum(v**2))
        #KE.append(ke)
        #gpe=-G*m*M/np.sqrt((np.sum(x**2)))
        #GPE.append(gpe)

    x = np.stack(x_s)

    plt.plot(x[:, 0], x[:, 1])
    # x[:,0] = x-coordinate, x[:,1] = y-coordinate
plt.show()
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Orbit")

#--------------
#spaceman and the hammer

v_list = [np.array([-0.2, 0.3]), np.array([-0.21, 0.31]), np.array([-0.19, 0.29]),np.array([-0.19, 0.29]), np.array([-0.19, 0.31]), np.array([-0.21, 0.29]) ]





for v in v_list:
    x_s = []
    f_s = []
    v_s = []
    t_s = []
    t = 0
    x = np.array([100., 70.])
    for i in range(10000):
        x_s.append(x)
        v_s.append(v)
        t_s.append(t)
        x = update_x(x, v/2)
        t = update_t(t, dt/2)

        f = update_f(x,A)

        v = update_v(v, f, m)

        x = update_x(x,v/2)

        t = update_t(t, dt / 2)

        #e_total = 1/2 *m* np.sqrt(v[0]**2+v[1]**2) - G*M*m/np.sqrt(np.sum(x**2))
        #E.append(e_total)
        #ke = 1/2 *m* np.sqrt(np.sum(v**2))
        #KE.append(ke)
        #gpe=-G*m*M/np.sqrt((np.sum(x**2)))
        #GPE.append(gpe)

    x = np.stack(x_s)

    plt.plot(x[:, 0], x[:, 1])
    # x[:,0] = x-coordinate, x[:,1] = y-coordinate
plt.show()
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Orbit")


#----------------

#perfect circle
#2nd, 5th, 6th and perhaps 7th experience change in period because they move away from sun and their semi mojor axes change which is what their timer period depends on
#all of these orbits return to starting place
#kick the planet parallel and along to its velocity, to make orbit larger and circular. kick parallel and opposite to velocity to make orbit smaller and circular. kick object at its aphelion to
#make it not come back with as little momentum as possible.

v_list = [np.array([0, 0.3]), np.array([0.01, 0.3]), np.array([-0.01, 0.3]),np.array([0, 0.29]), np.array([0.01, 0.31]),np.array([0.01, 0.29]), np.array([-0.01, 0.31]), np.array([-0.01, 0.29])]





for v in v_list:
    x_s = []
    f_s = []
    v_s = []
    t_s = []
    t = 0
    x = np.array([130., 0.])
    for i in range(10000):
        x_s.append(x)
        v_s.append(v)
        t_s.append(t)
        x = update_x(x, v/2)
        t = update_t(t, dt/2)

        f = update_f(x,A)

        v = update_v(v, f, m)

        x = update_x(x,v/2)

        t = update_t(t, dt / 2)

        #e_total = 1/2 *m* np.sqrt(v[0]**2+v[1]**2) - G*M*m/np.sqrt(np.sum(x**2))
        #E.append(e_total)
        #ke = 1/2 *m* np.sqrt(np.sum(v**2))
        #KE.append(ke)
        #gpe=-G*m*M/np.sqrt((np.sum(x**2)))
        #GPE.append(gpe)

    x = np.stack(x_s)

    plt.plot(x[:, 0], x[:, 1])
    # x[:,0] = x-coordinate, x[:,1] = y-coordinate

plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Orbit")
plt.axis('equal')
plt.show()


#------------from parallel

v_list = [np.array([-0.2, 0.3]), np.array([-0.2, 0.3])]
x_list = [np.array([300., 200.]), np.array([300., 180.])]
dt=2


G = 1
M = 10
m = 1

A = -G*M*m
#x is numpy
def update_f(x, A):
    f = A * x/((np.sqrt(np.sum(x**2))))**3
    return f


def update_x(x_0, v):
     return x_0 + dt*v


def update_v(v_0, f, m):
    return v_0 + dt * f / m

def update_t(t, dt):
    return t+dt


for v,x in zip(v_list, x_list):
    x_s = []
    f_s = []
    v_s = []
    t_s = []
    t = 0

    for i in range(50000):
        x_s.append(x)
        v_s.append(v)
        t_s.append(t)
        x = update_x(x, v/2)
        t = update_t(t, dt/2)

        f = update_f(x,A)

        v = update_v(v, f, m)

        x = update_x(x,v/2)

        t = update_t(t, dt / 2)

        #e_total = 1/2 *m* np.sqrt(v[0]**2+v[1]**2) - G*M*m/np.sqrt(np.sum(x**2))
        #E.append(e_total)
        #ke = 1/2 *m* np.sqrt(np.sum(v**2))
        #KE.append(ke)
        #gpe=-G*m*M/np.sqrt((np.sum(x**2)))
        #GPE.append(gpe)

    x = np.stack(x_s)

    plt.plot(x[:, 0], x[:, 1])
    # x[:,0] = x-coordinate, x[:,1] = y-coordinate
plt.show()
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Orbit")



#---------energy momentum graphs----------
x_s = []
f_s = []
v_s = []
t_s = []
x = np.array([100.,70.])
v = np.array([-0.2, 0.3])
t = 0
dt = 20
G = 1
M = 10
m = 1
A = -G*M*m


#x is numpy
def update_f(x, A):
    f = A * x/((np.sqrt(np.sum(x**2))))**3
    return f


def update_x(x_0, v):
     return x_0 + dt*v


def update_v(v_0, f, m):
    return v_0 + dt * f / m

def update_t(t, dt):
    return t+dt



E =[]
KE =[]
GPE=[]
P =[]
for i in range(10000):
    x_s.append(x)
    v_s.append(v)
    t_s.append(t)
    x = update_x(x, v)
    f = update_f(x, A)
    v = update_v(v, f, m)
    t = update_t(t, dt)

    e_total = 1/2 *m* np.sqrt(v[0]**2+v[1]**2) - G*M*m/np.sqrt(np.sum(x**2))
    E.append(e_total)
    ke = 1/2 *m* np.sqrt(np.sum(v**2))
    KE.append(ke)
    gpe=-G*m*M/np.sqrt((np.sum(x**2)))
    GPE.append(gpe)
    p = m* np.sqrt(np.sum(v**2))* np.sqrt(np.sum(x**2))
    P.append(p)

plt.plot(t_s, E, label='E')
plt.plot(t_s, KE, label='KE')
plt.plot(t_s, GPE, label='GPE')

plt.legend()
plt.show()

plt.plot(t_s, P)
plt.show()



#-----------E-P for leapfrog

x_s = []
f_s = []
v_s = []
t_s = []
x = np.array([100.,70.])
v = np.array([-0.2, 0.3])
t = 0
dt = 20
G = 1
M = 10
m = 1
A = -G*M*m


#x is numpy
def update_f(x, A):
    f = A * x/((np.sqrt(np.sum(x**2))))**3
    return f


def update_x(x_0, v):
     return x_0 + dt*v


def update_v(v_0, f, m):
    return v_0 + dt * f / m

def update_t(t, dt):
    return t+dt



E =[]
KE =[]
GPE=[]
P =[]
for i in range(10000):
    x_s.append(x)
    v_s.append(v)
    t_s.append(t)
    x = update_x(x, v / 2)
    t = update_t(t, dt / 2)

    f = update_f(x, A)

    v = update_v(v, f, m)

    x = update_x(x, v / 2)

    t = update_t(t, dt / 2)

    e_total = 1/2 *m* np.sqrt(v[0]**2+v[1]**2) - G*M*m/np.sqrt(np.sum(x**2))
    E.append(e_total)
    ke = 1/2 *m* np.sqrt(np.sum(v**2))
    KE.append(ke)
    gpe=-G*m*M/np.sqrt((np.sum(x**2)))
    GPE.append(gpe)
    p = m* np.sqrt(np.sum(v**2))* np.sqrt(np.sum(x**2))
    P.append(p)

plt.plot(t_s, E, label='E')
plt.plot(t_s, KE, label='KE')
plt.plot(t_s, GPE, label='GPE')

plt.legend()
plt.show()

plt.plot(t_s, P)
plt.show()

#---------------runge_kutta

import numpy as np
import matplotlib.pyplot as plt
x = np.array([100.,70.])
v = np.array([-0.2, 0.3])



#i can't really tell a difference in terms of energy and trajectory between the different methods. Not sure if ive gotten something wrong.
t = 0
dt = 2
G = 1
M = 10
m = 1

A = -G*M*m
def a(x):
    f = A * x/((np.sqrt(np.sum(x**2))))**3
    return f/m

x_s=[]
KE=[]
E=[]
GPE=[]
P=[]
t_s=[]
t=0
for i in range(10000):
    t_s.append(t)
    t+=1

    k1_x = v
    k1_v = a(x)

    k2_x = v + 0.5 * dt * k1_v
    k2_v = a(x + 0.5 * dt * k1_x)

    k3_x = v + 0.5 * dt * k2_v
    k3_v = a(x + 0.5 * dt * k2_x)

    k4_x = v + dt * k3_v
    k4_v = a(x + dt * k3_x)
    x += dt/6 * (k1_x + 2*k2_x + 2*k3_x + k4_x)
    v += dt/6 * (k1_v + 2*k2_v + 2*k3_v + k4_v)
    x_s.append(x.copy())

    e_total = 1 / 2 * m * np.sqrt(v[0] ** 2 + v[1] ** 2) - G * M * m / np.sqrt(np.sum(x ** 2))
    E.append(e_total)
    ke = 1 / 2 * m * np.sqrt(np.sum(v ** 2))
    KE.append(ke)
    gpe = -G * m * M / np.sqrt((np.sum(x ** 2)))
    GPE.append(gpe)
    p = m * np.sqrt(np.sum(v ** 2)) * np.sqrt(np.sum(x ** 2))
    P.append(p)

plt.plot(t_s, E, label='E')
plt.plot(t_s, KE, label='KE')
plt.plot(t_s, GPE, label='GPE')

plt.legend()
plt.show()

plt.plot(t_s, P)
plt.show()



x=np.stack(x_s)
plt.plot(x[:,0], x[:,1])
plt.show()
