#how to create class
#Student class
class Student:
	
	def __init__(self,name,age,email) :
	#like constructor, this will call automatically when object creation
	#use to insert data
		self.name = name #self == this in java
		self.age = age
		self.email = email

	def print_details(self) :
	#a method to prind details of an object
		print("Student details [",self.name,self.age,self.email,"]")


stu1 = Student("name1",20,"name1@email.com")#calls the constructor in Student class
stu2 = Student("name2",22,"name2@email.com")#create objects
stu3 = Student("name2",23,"name3@email.com")


print(type(stu1))#prints the type of the comp

stu2.print_details()#call the method in Computer class
Student.print_details(stu3)#another way to call functions in pthon
