import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import curve_fit
from scipy.integrate import cumtrapz

#constants
pi=3.1415926
g=9.81

#variables
Rrot=0
omega=2*pi*25
psi=pi/360
mur=0.00005
theta=pi/90
r=0.0035
Rh=0.01325

omega=30

def odesys(t,S):
    phidot,phi=S
    return [-r*psi*(Rrot+Rh*np.cos(theta)-r)*omega*omega*np.cos((1-r/Rh)*psi)*np.sin(np.arctan(2*r*psi*np.tan(phi)/Rh))/(Rh*Rh*np.cos(psi)), phidot]

#init conditions
phidot0=0
phi0=pi/180
s0=(phidot0,phi0)

#solve the differential equation
t=np.linspace(0,100,1000)
sol=solve_ivp(odesys,(0,100),y0=s0,method="LSODA",t_eval=t)
phi_sol=sol.y[1]

#curve_fitting
f=lambda t,a,b: a*np.cos(b*t)
popt, pcov = curve_fit(f,t,phi_sol,p0=(0.2,6.3/57))

vert_vel=[Rh*omega*np.sin(phi_sol[i]) for i in range(len(t))]
vert_dis=cumtrapz(vert_vel,t,initial=0)

#plot data and fitted curve
plt.plot(t,phi_sol,label="phi")
plt.plot(t,f(t,popt[0],popt[1]))
#plt.plot(t,vert_dis,label="vertical displacement")
plt.legend()
plt.xlabel("time [sec]")
plt.ylabel("phi [rad]")
plt.grid()
plt.tight_layout()
plt.show()
print(popt[1])