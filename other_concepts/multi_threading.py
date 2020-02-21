from threading import *
from math import *

class CalPi1(Thread):
#	it = 100000000

	def run(self):
		it = 100000000
		result = 0
		for i in range(it):
			result += pow(-1, i + 1) / ((2 * i) - 1)

		result *= 4
		
		print("PI value:",result-4,"for",it)

class CalPi2(Thread):

	def run(self):
		it = 200000000
		result = 0
		for i in range(it):
			result += pow(-1, i + 1) / ((2 * i) - 1)

		result *= 4
		
		print("PI value:",result-4,"for",it)

class CalPi3(Thread):

	def run(self):
		it = 300000000
		result = 0
		for i in range(it):
			result += pow(-1, i + 1) / ((2 * i) - 1)

		result *= 4
		
		print("PI value:",result-4,"for",it)


class CalPi4(Thread):

	def run(self):
		it = 400000000
		result = 0
		for i in range(it):
			result += pow(-1, i + 1) / ((2 * i) - 1)

		result *= 4
		
		print("PI value:",result-4,"for",it)

#create thread objects
t1 = CalPi1()
t2 = CalPi2()
t3 = CalPi3()
t4 = CalPi4()

#start threads
#automatically call run method when start
t1.start()
t2.start()
t3.start()
t4.start()


#wait until all thread end
t1.join()
t2.join()
t3.join()
t4.join()

print("Stop...")
