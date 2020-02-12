from numpy import *

matrix = array([[1,2,3],[2,4,5]])

print(matrix)

print(matrix.dtype) #datatype

print(matrix.ndim) #diamension
print(matrix.shape) #number of colmns and rows

arr2 = matrix.flatten() #convert 2D to 1D array
print(arr2)

matrix2 = arr2.reshape(3,2)#convert 1D array to 2D array ==> (rows,columns)
print(matrix2)


