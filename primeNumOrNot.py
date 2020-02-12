num = int(input("Enter number : "))

if num == 0 or num ==1:
	print(num,"is not prime")
for i in range(2,num):
	if num%i==0:
		print(num,"is not prime")
		break
else:
	print(num,"is prime number")
