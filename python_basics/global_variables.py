a = 10 #global variable

def update():
	a = 9 #local variable
	
	x = globals()["a"] #function that use to access global variables
	print("inside function",a)
	print("global vriable from inside function",x)


update()
print("outside function",a)
