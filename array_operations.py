'''
NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of data
'''
from numpy import *

arr1 = array([1,2,3,4,5])
arr2 = array([3,4,5,6,7])

print(arr1+arr2) #addition

print(sin(arr1))#get sin value

print(sqrt(arr1))#get sqare root value

print(min(arr1))#get min value

print(sort(arr1))#sort array

arr3 = arr1 #copy array (shallow copy) values are change in both when edit one

arr4 = arr2.view()#create different array and copy elements(deep copy)
