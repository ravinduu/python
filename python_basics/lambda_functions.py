f = lambda value : value**2
'''
above lambda function is same as the function bellow
def square(value) : 
	return value**2
'''

result = f(3)
print("Square of 3 =",result)

'''
def is_even(n):
	return n%2==0
'''

nums = [1,2,3,4,5,678,9,9,0,3,65,3,4,43,3,233,45,6,]
#filter is inbuilt function
evens = list(filter(lambda n : n%2 == 0,nums))#lambda function == is_even
print(evens)
