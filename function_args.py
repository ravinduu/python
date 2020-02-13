#normal function that update given value
def update(x) :
	x = 8
	print(x)

a = 10
update(a)
print(a)

#function with two arguments
def persion(name,age = 16) :#in here the sequance of args are important 
	print(name)
	print(age)

persion("name1",23)#normal way to call the function
persion(age = 32,name = "name2")#call the function using keyword args
persion("name3")#age is default set to 16


#def sum(a,*b) : # *b is to multiple vales... can pass any values

def persion_details(name,**data) : #in here when we pass the data we need to specify the keyword ,by using ** we can pass multiple args
	print(name)
	print(data)# the ** will take values as a list

persion_details("name",age=23,uni="uni",school="school",major="major")#name is required,others are user define, but need to use keywords
