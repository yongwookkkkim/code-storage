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
Rh=4
r=1
omega=1
theta=0.05*pi

#steps
thetastep=0.05*pi
Rhstep=5
omegastep=1
rstep=1
sintheta=np.sin(theta)

#arrays
thetaarray=[]
amplitudearray=[]
angfrequencyarray=[]

'''
#increase variables
omega+=omegastep
r+=rstep
Rh+=Rhstep
theta+=thetastep
sintheta=np.sin(theta)
'''

#differential equation
def d2phidt2(t,S):
    phidot, phi = S
    return [-(Rh-r)*omega*omega*sintheta*sintheta*np.sin(2*phi)*np.sqrt(1+sintheta*sintheta*np.cos(phi)*np.cos(phi))/Rh, phidot]

#initial conditions
phidot0=0
phi0=0.2
s0=(phidot0,phi0)

#solving the equations
t=np.linspace(0,100,1000)
sol=odeint(d2phidt2,y0=s0,t=t, tfirst=True)
phidot_sol=sol.T[0]
phi_sol=sol.T[1]


'''
#fitting
f = lambda x,a,b: a*np.cos(b*x)
popt,pcov=curve_fit(f,t,phi_sol,p0=(0.1,0.25))
 
#add data to the arrays
thetaarray.append(theta)
amplitudearray.append(popt[0])
angfrequencyarray.append(popt[1])
'''

plt.plot(t,phi_sol,label="Phi")
vert_vel=[Rh*omega*np.sin(phi_sol[i]) for i in range(len(t))]
vert_dis=scipy.integrate.cumtrapz(vert_vel,t,initial=0)
plt.plot(t,Rh*omega*np.sin(phi_sol),label="vert vel")
plt.plot(t,vert_dis,label="vert displacement")
plt.legend()
plt.show()

'''
#plotting the graph
plt.plot(t, phi_sol, label="phi")
plt.plot(t,f(t,popt[0],popt[1]),label="fit")

#plotting the linear regression 
#plt.plot(np.cos(popt[1]*t), phi_sol)

plt.legend()
plt.show()
'''