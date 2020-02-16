def fact(x) :
	if x < 0 :
		print("Error, Enter positive number")
		return -1
	else:
		if x == 0 or x == 1:
			return 1
		else :
			return x * fact(x-1)
'''	result = 1
	for i in range(1,x+1) :
		result *= i
	
	return result
'''

fact = fact(int(input("Enter value :")))
print("factorial =",fact)
