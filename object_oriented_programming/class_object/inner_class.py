class Employee:
	def __init__(self,name,ssn):
		self.name = name
		self.ssn = ssn
		self.dep = self.Department()#create an object of inner class

	def print_details(self):
		print("name:",self.name,"\nssn:",self.ssn,"\nDep:",self.dep)

	class Department:
	#inner class
		def __init__(self):
			self.d_name = "Accounts"



emp1 = Employee("John",1)
emp1.print_details()


emp2 = Employee("Cena",2)
dep2 = Employee.Department()#craete objects of inner class from out side of outter class


