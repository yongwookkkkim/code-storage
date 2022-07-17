import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.integrate import cumtrapz

#variables
m=0.2
rrot=0.04
rh=0.1
r=0.02
omegap=15*np.pi
l=0.02
theta=np.pi/36
c=-1

def odesys(t,S):
    phidot, phi=S
    return [(-m*(rrot+rh*np.cos(theta)-r)*omegap*omegap*l*np.tan(phi)*np.sin(l*np.cos(phi)/(2*r))/2+c*phidot*m*(rrot+rh*np.cos(theta)-r)*omegap*omegap*l/2)/((1+np.cos(theta)*np.cos(theta)/2)*m*rh*rh), phidot]

#init condition
phidot0=0
phi0=-np.pi/36
s0=(phidot0,phi0)

#solve
t=np.linspace(0,10,10000)
sol=solve_ivp(odesys,(0,10),y0=s0,method="LSODA",t_eval=t)
phi_sol=sol.y[1]
phidot_sol=sol.y[0]
d_sol=cumtrapz(omegap*rh*np.sin(phi_sol),t)

plt.subplot(2,3,1)
plt.plot(t, phi_sol,label='phi')
plt.title('t-phi')

plt.subplot(2,3,2)
plt.plot(phi_sol,-m*(rrot+rh*np.cos(theta)-r)*omegap*omegap*l*np.tan(phi_sol)*np.sin(l*np.cos(phi_sol)/(2*r))/2+c*phidot_sol*m*(rrot+rh*np.cos(theta)-r)*omegap*omegap*l/2,label='torque')
plt.title('phi-torque')

plt.subplot(2,3,3)
plt.plot(phi_sol, phidot_sol, label='phase diagram')
plt.title('phase diagram (phi-phidot)')

plt.subplot(2,3,4)
plt.plot(np.linspace(0,10,9999),d_sol)
plt.title('vert displacement')

plt.subplot(2,3,5)
plt.plot(t,phidot_sol)
plt.title('t-phidot')

plt.subplot(2,3,6)
plt.plot(phidot_sol, -m*(rrot+rh*np.cos(theta)-r)*omegap*omegap*l*np.tan(phi_sol)*np.sin(l*np.cos(phi_sol)/(2*r))/2+c*phidot_sol*m*(rrot+rh*np.cos(theta)-r)*omegap*omegap*l/2)
plt.title('phidot-torque')
plt.show()