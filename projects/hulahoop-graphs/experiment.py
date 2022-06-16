import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

#radius
x=np.array([4, 5,7])
ye=np.array([5.7322656341144755, 4.004020715914333, 4.19785])
yo=np.array([6.123,4.32,4.66])
plt.scatter(x,ye,marker='*',label='Theoretical Values')
#plt.scatter(x,yo,marker='o',label='experimental values')
plt.legend()
plt.grid()
plt.xlabel('radius of ring [mm]')
plt.ylabel('period [s]')
plt.title("period of phi's oscillation vs. radius of the ring")
plt.show()

#omega
'''
x=np.array([15,20,25,30,35])
ye=np.array([])
yo=np.array([])
plt.scatter(x,ye,marker='*',label='Theoretical Values')
plt.scatter(x,yo,marker='o',label='experimental values')
plt.legend()
plt.grid()
plt.xlabel('angular velocity of the hoop [rad/s]')
plt.ylabel('period [s]')
plt.title("period of phi's oscillation vs. angular velocity of the hoop")
plt.show()
'''