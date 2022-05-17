import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
from scipy.integrate import solve_ivp
import scipy.integrate

#constants
pi=3.1415926
g=9.81

#variables
r=1
Rh=3
Rrot=0.5
omega=2
psi=0.05*pi
mur=0.03


def odesys(t,S):
    phidot,phi,omega=S
    return [-2*r*(Rh+Rrot)*omega*omega*psi*np.tan(phi)/(Rh*Rh*np.cos(psi)), phidot, -2*mur*(Rh+Rrot)/(Rh*(1/(r*omega*omega) + 1/np.sqrt(g*g+r*r*omega*omega*omega*omega)))]

#init conditions
phidot0=0
phi0=0.2
omega0=2
s0=(phidot0,phi0,omega0)

#solve the differential equation
t=np.linspace(0,100,1000)
sol=solve_ivp(odesys,(0,100),y0=s0,method="LSODA",t_eval=t,)
phidot_sol=sol.y[0]
phi_sol=sol.y[1]
omega_sol=sol.y[2]

#vertical velocity and displacement derived from v_z=Rh omega sin(phi)
vel_sol=[omega_sol[i]*Rh*np.sin(phi_sol[i]) for i in range(len(t))]
displacement_sol=scipy.integrate.cumtrapz(vel_sol, t, initial=0)

#plot data
plt.plot(t,phi_sol,label="phi")
plt.plot(t,phidot_sol,label="phidot")
plt.plot(t,vel_sol,label="vel")
plt.plot(t,displacement_sol,label="displacement")
plt.plot(t,omega_sol,label="omega")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()