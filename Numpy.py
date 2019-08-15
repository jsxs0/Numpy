import numpy as np
np.random.seed(0) #seed for reproducibilty
x1=np.random.randint(10, size=6) #1D
x2=np.random.randint(10, size=(3,4,)) #2D
x3=np.random.randint(10, size=(3,4,5)) #3D
print("x3 ndim: ",x3.ndim)
print("x3 shape:",x3.shape)
print("x3 size:",x3.size)
print("dtype:",x3.dtype)
print("itemsize:",x3.itemsize,"bytes")
print("nbytes:",x3.nbytes,"bytes")
