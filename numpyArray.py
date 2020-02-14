'''
There are many ways to declare array using NumPy
ex:
	1)manually
	2)using linspace()
	3)using arange()
	4)using logspace()
	5)using zeros()
	6)using ones()
'''
from numpy import *

#manually
arr = array([1,2,3,4,5],float)

print(arr)
print(arr.dtype)

#linspace()
arr1 = linspace(0,15,20)#from 1 to 15, 20 elements
print(arr1)

#arange
arr2 = arange(1,15,2) #from 1 to 15, by 2 steps
print(arr2)

#logspace
arr3 = logspace(1,40,5)#log something
print(arr3)

#zeros
arr4 = zeros(5) #size 5 array all 0s 

#ones
arr5 = ones(1)#size 5 array all 1s
