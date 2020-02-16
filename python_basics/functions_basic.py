#normal function
def hello_world() :#define function call hello_world
	print("Hello World")

hello_world() #call the above function

#function with arguments
def add(x,y) : #x,y are arguments
	print(x,"+",y,"=",x+y)

add(3,4)

#function with return a value
def diff(x,y):
	return x+y #return value

print(diff(34,43))

#function with return multiple values
def add_sub(x,y):
	return x+y,x-y#return 2 values

add_result,sub_result = add_sub(54,56)
print("add",add_result)
print("sub",sub_result)
