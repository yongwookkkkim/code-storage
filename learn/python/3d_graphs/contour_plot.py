import numpy as np
import matplotlib.pyplot as plt

Y = X = np.linspace(-3, 3)
x, y = np.meshgrid(X, Y)
F = np.sin(X) * np.cos(y)

no = 15

plt.contour(x, y, F, no)

#the higher the value of no, the more lines it will show

plt.xlabel("x")
plt.ylabel("y")

plt.show()