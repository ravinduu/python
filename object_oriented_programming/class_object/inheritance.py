class Vehicle:
#parent class

	def __init__(self,make,model,engine_capacity,no_of_tyres,no_of_seats,has_AC,current_speed,current_direction):
	#all common attributes
		self.make = make
		self.model = model
		self.engine_capacity = engine_capacity
		self.no_of_tyres = no_of_tyres
		self.no_of_seats = no_of_seats
		self.has_AC = has_AC
		self.current_speed = current_speed
		self.current_direction = current_direction

	def start(self):
		print("\nstart.....")

	def drive(self):
		print("\ndrive.....")

	def horn(self):
		print("\nhorn......")


class Car(Vehicle):
#car class inherit from vehicle class
#it has all attributes and methods of vehicle class
	
	def __init__(self,make,model,has_AC):
		super().__init__(make,model,2500,4,5,has_AC,0,0)
		#call the constructor of parent class

	def print_details_car(self):
		print("\tCar\nmake:",self.make,"\nmodel",self.model,"\nengCC:",self.engine_capacity,"\ntyres",self.no_of_tyres,"\nseats",self.no_of_seats,"\nAC?:",self.has_AC)



class Truck(Vehicle):
#truck class inherit from vehicle class
#it has all attributes and methods of vehicle class
	
	def __init__(self,make,model,load_capacity):
	#load_capacity is special for only trucks
		super().__init__(make,model,5000,6,2,False,0,0)
		#call the constructor of parent class
		self.load_capacity = load_capacity

	def print_details_truck(self):
		print("\tTruck\nmake:",self.make,"\nmodel",self.model,"\nengCC:",self.engine_capacity,"\ntyres",self.no_of_tyres,"\nseats",self.no_of_seats,"\nAC?:",self.has_AC,"\nLoad capacity",load_capacity)


#create new car object
car1 = Car("Toyota","Yaris",True)

car1.print_details_car()

#all methods in vehical can access by car class
car1.start()
car1.drive()
car1.horn()


#create new truck object
trk1 = Truck("Tata","l001",10000)
#trk1.pirnt_details_truck()
