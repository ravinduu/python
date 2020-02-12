from numpy import *

#manually
arr = array([1,2,3,4,5],float)

print(arr)
print(arr.dtype)

#linspace()
arr1 = linspace(0,15,20)#from 1 to 15, 20 elements
print(arr1)

#arange
arr2 = arange(1,15,2) #from 1 to 15, by 2
print(arr2)

#logspace
arr3 = logspace(1,40,5)#log something
print(arr3)

#zeros
arr4 = zeros(5) #size 5 array all 0s 

#ones
arr5 = ones(1)#size 5 array all 1s
