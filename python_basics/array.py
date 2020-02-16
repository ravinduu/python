#arrays are not fixed size in python
#can add elements
#flexible
#need to import array
#need to types to declare data type => b = int, B = int,..... u = char,...,f = float, i = int

#declare array using array inbuilt pkg
from array import *

value = array("i",[1,2,3,4,5]) #declare array
print(value)

for i in value :
	print(i)

#declare array using numpy
from numpy import *

value = array

length = int(input("Enter the length : "))

for i in range(length) :
	x = int(input("Enter value : "))
	value = append(value,x)

print(value)
