import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

f = lambda x, y: np.sin(x) * np.cos(y)
x = y = np.linspace(-3, 3)
x, y = np.meshgrid(x, y)
F =  f(x, y)

def plotter(E, A):
    fig = plt.figure(figsize = [12, 8])
    ax = fig.gca(projection = '3d')
    ax.plot_surface(x, y, F, cmap=cm.coolwarm)
    ax.view_init(elev=E, azim=A)
    plt.show()


from ipywidgets import interactive
iplot = interactive(plotter, E = (-90, 90, 5), A = (-90, 90, 5))
iplot