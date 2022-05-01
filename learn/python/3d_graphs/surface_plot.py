import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm # imports colour map tools

f = lambda x, y: np.sin(x) * np.cos(y)
X = Y = np.linspace(-3, 3)
x, y = np.meshgrid(X, Y)
F = f(x, y)

fig = plt.figure(figsize = [12, 8])
ax = fig.gca(projection = '3d') #set up the axis as a 3d plot
ax.plot_surface(x, y, F, cmap=cm.coolwarm) 
#coolwarm, copper, cubehellix, Dark2, flag, dated, copper

plt.show()