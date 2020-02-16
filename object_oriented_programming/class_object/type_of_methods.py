#1) instance methods
#2) class methods
#3) static method

class Car:
	wheels = 4
	doors = 5
	
	def __init__(self,brand,model,year):
		self.brand = brand
		self.model = model
		self.year = year
	
	def details(self):
	#instace method, it works only with objects
	#use self
		print(self.brand,self.model,self.year)

	def get_brand(self):
	#getter
		return self.brand

	def set_brand(self):
	#setter
		self.brand = brand

	@classmethod 
	#@classmethod reqired
	def extra_details(cls):
	#class method, use class variable
	#use cls
		return cls.wheels,cls.doors

	@staticmethod
	def info():
	#static method
		print("Whatever")

car1 = Car("BMW","M5",2019)
car2 = Car("Audi","R8",2018)

car1.details() #call instance method

print(Car.extra_details())#call class method

Car.info() #call static method


