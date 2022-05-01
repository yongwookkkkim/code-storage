from matplotlib import pyplot as plt
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
import numpy as np

def dvdt(v, t):
    return 3*v**2 - 5
v0 = 0
t = np.linspace(0,1,100)
sol = odeint(dvdt, y0=v0, t=t, tfirst=True)
print(sol.T) #traspose the solution
print(sol.T[0]) #the first row(it's a multidimensional matrix)
sol2 = solve_ivp(dvdt, t_span=(0,max(t)), y0=[v0], t_eval=t)
plt.plot(t, sol2[0])
plt.show()