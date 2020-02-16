nums = [12,23,43,51,67,82,201] #list

for i in nums:
	if i%5==0:
		print("divisible by 5 => ",i)
		break
else :#this else is for for loop
	print("not found")

"<Summary>
we can use else with for loop in python,if any of the values will not satisfy the condition in IF condition it will print the message in else part"
