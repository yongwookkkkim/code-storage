import scipy as sp
import matplotlib.pyplot as plt
import numpy as np

from scipy.optimize import minimize
'''
#minimising a function
def f(x):
    return x**4 + x**3 -3*x**2 + 7*x - 9**2

res = minimize(f,4)

#minimising a function with 2 parameters, bound within some constraints
f = lambda x: (x[0]-1)**2 + (x[1]-2)**2
cons = ({'type': 'ineq', 'fun': lambda x: x[0]-2*x[1]+2},
        {'type': 'ineq', 'fun': lambda x: -x[0]-2*x[1]+6},
        {'type': 'ineq', 'fun': lambda x: -x[0]+2*x[1]+2})
bnds = ((0, None), (0, None))
res = minimize(f, [2,1], constraints=cons, bounds=bnds)
'''
'''
#interpolating data points
from scipy.interpolate import interp1d

x = np.linspace(0,10,10)
y = x**2 * np.sin(x)
f = interp1d(x,y,kind='cubic')
x_dense = np.linspace(0,10,100)
y_dense = f(x_dense)
plt.plot(x_dense,y_dense)
plt.show()
'''
'''
import numpy as np
from scipy.optimize import curve_fit
def f(x,a,b,c):
    return a*x**2 + b*x + c
x_data = np.linspace(0,10,10)
y_data = 6*x_data**2 - 8*x_data + 1 
popt, pcov = curve_fit(f, x_data, y_data,p0=(1,1,1))
print(popt)
'''
'''
t_data = np.array([time_data])
y_data = np.array([time_data])
def func(t,A,w,phi):
    return A*np.cos(w*t + phi)
popt, pcov = curve_fit(func, x_data, y_data, p0=(1,1,1))
A, w, phi = popt
t = np.linspace(0,10,100)
y = func(t, A, w, phi)
plt.scatter(t_data, y_data)
plt.plot(t,y)
plt.show()

import matplotlib.pyplot as plt
from scipy.misc import derivative
def f(x):
    return x**2 * np.sin(2*x)*np.exp(-x)
x = np.linspace(0,1,100)
plt.plot(x, f(x))
plt.plot(x, derivative(f,x,dx=1e-6, n=1))
plt.plot(x, derivative(f,x,dx=1e-6, n=2)) #n denotes the order of differentiation
plt.show()

from scipy.integrate import quad
integrand = lambda x: x**2 * np.sin(2*x) * np.exp(-x)
integral, integral_error = quad(integrand, 0, 1) #integration over the range [0,1]
print(integral)
print(integral_error)

from scipy.integrate import dblquad
integrand2 = lambda x, y: np.sin(x+y**2)
lwr_y = lambda x: -x
upr_y = lambda x: x**2
integral2, integral_error2 = dblquad(integrand2, 0, 1, lwr_y, upr_y) #the range of x -> the range of y
print(integral2)
print(integral_error2)

from scipy.integrate import nquad
'''
#differential equations using odeint
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
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