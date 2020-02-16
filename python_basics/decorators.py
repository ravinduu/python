def div(a,b) :
	return a/b


#decorator for div
#add addition method from outside
#decos_div accept function
def decos_div(func) :
	def inner(a,b) :
		if a < b :
			a,b = b,a

		return func(a,b)
	return inner

div = decos_div(div)
print(div(2,6))
