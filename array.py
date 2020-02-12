#arrays are not fixed size in python
#can add elements
#flexible
#need to import array
#need to types to declare data type => b = int, B = int,..... u = char,...,f = float, i = int

#import array

#from numpy import *


#value = array([1,2,3,4,5])
#print(value)

#for i in value :
#	print(i)

from numpy import *

value = array

length = int(input("Enter the length : "))

for i in range(length) :
	x = int(input("Enter value : "))
	value = append(value,x)

print(value)
