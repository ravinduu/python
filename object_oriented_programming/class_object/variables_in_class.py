class Car:
	
	wheels = 4
	seats = 5
	doors = 5
	#this variables are class variables
	#they are same for all objects
	
	def __init__(self):
		self.brand = "AUDI"
		self.model = "Q8"
		self.engine_capacity = 1000
		self.engine_type = "V8"
		self.bhp = 300
		#these variables are instance variable
		#they can change according to object
