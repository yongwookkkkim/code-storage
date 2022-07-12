import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

phi=np.linspace(-0.5, 0.5)
muk=np.linspace(-0.5, 0.5)
l=0.01
r=0.15
p,m=np.meshgrid(phi,muk)
f=lambda phi,muk: np.tan(phi)*np.sin(l*np.cos(phi)/(2*r))-muk


plt.contour(p,m,f(p,m),[0])
plt.grid()
plt.ylim(-0.1, 0.1)
plt.xlabel('phi_eq')
plt.ylabel('muk')
plt.title('relationship between phi_eq and muk')
plt.show()
'''
fig = plt.figure(figsize = [12, 8])
ax = fig.gca(projection = '3d') #set up the axis as a 3d plot
ax.plot_surface(m, p, f(m,p), cmap=cm.coolwarm) 
plt.xlabel('muk')
plt.ylabel('phi')
plt.show()
'''