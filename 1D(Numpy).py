from numpy import random as rn
import numpy as np
n = 6
m = 3
A=rn.randint(5,size=(n+m))
M=np.array([1,2,3])

A[n:n+m]=0
print("Array = ",A)
print("Mask =",M)
print("Matrix B = [",end=' ')
for i in range(n):
    B=np.sum(A[i:i+m]*M[0:m])
    print(B,end=' ')
print(" ]")