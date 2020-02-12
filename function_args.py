def update(x) :
	x = 8
	print(x)

a = 10
update(a)
print(a)

def persion(name,age = 16) :#in here the sequance of args is important 
	print(name)
	print(age)

persion("ravindu",23)
persion(age = 32,name = "dilshan")#keyword args
persion("name")#age is default set to 16


#def sum(a,*b) : # *b is to multiple vales... can pass any values

def persion_details(name,**data) : #in here when we pass the data we need to specify the keyword
	print(name)
	print(data)

persion_details("ravindu",age=23,uni="UOP",school="SSCK",major="CS")
