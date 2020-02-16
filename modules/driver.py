import calculator as cal

while True :
	num1 = int(input("Enter number : "))
	num2 = int(input("Enter number : "))
	ch = int(input("1 - add,2 - sub,3 - multi,4- div : "))

	if ch == 1 :
		result = cal.add(num1,num2)
		print(result)
	elif ch == 2:
		result = cal.sub(num1,num2)
		print(result)	
	elif ch == 3:
		result = cal.mult(num1,num2)
		print(result)
	elif ch == 4:
		result = cal.div(num1,num2)
		print(result)
	else : 
		break
	
