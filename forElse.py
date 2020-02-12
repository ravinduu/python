nums = [12,23,43,51,67,82,201] #list

for i in nums:
	if i%5==0:
		print("divisible by 5 => ",i)
		break
else :#this else is for for loop
	print("not found")
