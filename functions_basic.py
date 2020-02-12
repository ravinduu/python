def hello_world() :#define function call hello_world
	print("Hello World")

hello_world() #call the above function

def add(x,y) : #with arguments
	print(x,"+",y,"=",x+y)

add(3,4)
	
def diff(x,y):
	return x+y #return value

print(diff(34,43))

def add_sub(x,y):
	return x+y,x-y#return 2 values

add_result,sub_result = add_sub(54,56)
print("add",add_result)
print("sub",sub_result)
