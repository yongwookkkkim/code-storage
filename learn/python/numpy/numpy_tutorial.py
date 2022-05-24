import numpy as np

#a=np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
#b=np.array([1,2,3,4,5,6], dtype='int8') #you can customise the type of the array
#c=np.array([[[1,2], [3,4]], [[5,6], [7,8]]])

#get dimension
#print(a.ndim)

#get shape
#print(a.shape)

#get type
#print(a.dtype)

#the number of bytes each item takes up
#print(b.itemsize)

#the number of bytes the array takes up
#print(a.nbytes)

#get a specific element (wokrds outside in)
#print(a[1,:]) # negative index also possible
#[startindex:endindex:stepsize]

#change an element
#a[1,2]=20.0
#a[:,2]=5 # or [1.0, 2.0]

#all 0s matrix
#zeros=np.zeros((5,5,5)) #or a single number tossed in

#all 1s matrix
#onees=np.ones((4,2,2), dtype='int8')

#any other number
#s99=np.full((2,2), 99) # the dimension and the number you want to fill it with

#same dimension as another array
#samedim=np.full_like(c, 6)

#random decimal numbers
#randoms=np.random.rand(4,2) # not a tuple!

#random data, same dimension
#randsamedim=np.random.random_sample(c.shape)

#random integer values
#randints=np.random.randint(4,7,size=(3,3)) # random int between 4 and 7

#identity matrix
#eyes=np.identity(5)

#repeating another array
#arr=np.array([[1,2,3]])
#r1=np.repeat(arr, 3, axis=0)

#practice
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 9 0 1
# 1 0 0 0 1
# 1 1 1 1 1
#base=np.full((5,5), 1)
#base[1:-1, 1:-1]=0
#base[2,2]=9

#deep and shallow copy
#x=np.array([1,2,3])
#y=x #this creates a shallow copy
#y=x.copy() #this creates a deep copy

#element-wise operations
#x=np.array([1,2,3,4])
#x=x+2
#x=np.sin(x) # all of these result in element-wise operations

#linear algebra
#a=np.ones((2,3))
#b=np.full((3,2),2)
#print(np.matmul(a,b)) # matrix multiplication

#determinant
#c=np.identity(3)
#print(np.linalg.det(c))
#eigenvalue, inverse of matrix, etc are available

#statistics
#stats=np.array([[1,2,3], [4,5,6]])
#print(np.min(stats), axis=0) #maximum, axis=0 to print mins of each column
#print(np.min(stats)) #minimum
#print(np.sum(stats)) #sum

#reorganising arrays
#before=np.array([[1,2,3,4],[5,6,7,8]])
#after=before.reshape((8,1))

#vertically stacking vector
v1=np.array([9,8,7,6])
v2=np.array([1,2,3,4])

print(np.vstack([v1,v2]))