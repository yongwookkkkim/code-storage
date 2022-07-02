import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

rm=1
rn=6
l=23
h=20
d=5.5

phi, theta= np.meshgrid(np.linspace(0,np.pi/18, 10000), np.linspace(0,np.pi/18, 10000))
f=(h+rm*np.sin(theta)-rn*np.sin(phi))**2+(rn*np.cos(phi)-d-rm*np.cos(theta))**2-h**2-(rm-rn+d)**2
plt.contour(phi, theta, f, [0])
plt.xlabel('phi')
plt.ylabel('theta')
plt.xlim(-0.1, 0.4)
plt.ylim(-0.1, 0.4)
plt.show()