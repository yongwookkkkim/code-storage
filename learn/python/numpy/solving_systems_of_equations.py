import numpy as np

#say we have
''' 
3x + y + z = 5
2x + 2y + z = 5
x -y + 6z = 5
'''

A = np.array([[3, 1, 1], [2, 2, 1], [1, -1, 6]])
b = np.array([[5], [5], [5]])

print(np.linalg.solve(A, b))