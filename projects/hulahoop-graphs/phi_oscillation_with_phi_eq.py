import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.integrate import cumtrapz

#variables
m=1.5
rrot=0.10
rh=0.45
r=0.15
omegap=2*np.pi
l=0.06
theta=np.pi/12
c=-0.01

def odesys(t,S):
    phidot, phi=S
    return [-m*(rrot+rh*np.cos(theta)-r)*omegap*omegap*l*np.tan(phi)*np.sin(l*np.cos(phi)/(2*r))/2+c*phidot*m*(rrot+rh*np.cos(theta)-r)*omegap*omegap*l/2, phidot]

#init condition
phidot0=0
phi0=np.pi/36
s0=(phidot0,phi0)

#solve
t=np.linspace(0,1000,10000)
sol=solve_ivp(odesys,(0,1000),y0=s0,method="LSODA",t_eval=t)
phi_sol=sol.y[1]
phidot_sol=sol.y[0]
d_sol=cumtrapz(omegap*rh*np.sin(phi_sol),t)

plt.subplot(2,2,1)
plt.plot(t, phi_sol,label='phi')
plt.title('t-phi')

plt.subplot(2,2,2)
plt.plot(phi_sol,-m*(rrot+rh*np.cos(theta)-r)*omegap*omegap*l*np.tan(phi_sol)*np.sin(l*np.cos(phi_sol)/(2*r))/2+c*phidot_sol*m*(rrot+rh*np.cos(theta)-r)*omegap*omegap*l/2,label='torque')
plt.title('phi-torque')

plt.subplot(2,2,3)
plt.plot(phi_sol, phidot_sol, label='phase diagram')
plt.title('phase diagram')

plt.subplot(2,2,4)
plt.plot(np.linspace(0,1000,9999),d_sol)
plt.title('vert displacement')

plt.show()