#import matplotlib, numpy, scipy
import matplotlib.pyplot as plt
import numpy as np

#differential equations using odeint
from scipy.integrate import odeint
from scipy.optimize import curve_fit
import scipy.integrate

#constants
pi=3.14159

#variables
Rh=0.3
r=0.07
omega=50
theta=0.2*pi
Rrot=0.1
psi=pi/180

#steps
thetastep=0.05*pi
Rhstep=5
omegastep=1
rstep=1
sintheta=np.sin(theta)

#differential equation
def d2phidt2(t,S):
    phidot, phi = S
    return [-r*psi*(Rrot+Rh*np.cos(theta)-r)*omega*omega*np.cos((1-r/Rh)*psi)*np.sin(np.arctan(2*r*psi*np.tan(phi)/Rh))/(Rh*Rh*np.cos(psi)), phidot]

#initial conditions
phidot0=0
phi0=0.2
s0=(phidot0,phi0)

#solving the equations
t=np.linspace(0,100,1000)
sol=odeint(d2phidt2,y0=s0,t=t, tfirst=True)
phidot_sol=sol.T[0]
phi_sol=sol.T[1]

plt.plot(t,phi_sol,label="Phi")
vert_vel=[Rh*omega*np.sin(phi_sol[i]) for i in range(len(t))]
vert_dis=scipy.integrate.cumtrapz(vert_vel,t,initial=0)
plt.plot(t,Rh*omega*np.sin(phi_sol),label="vert vel")
plt.plot(t,vert_dis,label="vertical displacement")
plt.legend()
plt.ylabel("displacement [arbitrary unit]")
plt.xlabel("time [arbitrary unit]")
plt.tight_layout()
plt.show()