from cmath import pi
import matplotlib.pyplot as plt
import numpy as np

#theta
#omega
Rrot=0.15
Rh=0.5
r=0.07
g=9.81

fig=plt.figure(1, figsize=(5,5))
delta=0.025
theta,omega=np.meshgrid(np.arange(0, np.pi/2,10/5000), np.arange(0.10,20,(20-0.5)/5000))
f=np.tan(theta)-g/((Rrot+Rh*np.cos(theta)-r)*omega*omega)
plt.contour(omega/(2*np.pi),180*theta/np.pi,f,[0]) 
plt.ylabel("theta [degrees]")
plt.xlabel("frequency [Hz}")
plt.show()