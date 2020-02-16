def fibonacci(x):
	print("Fibonacci series for ",x)
	prev_no = 0
	next_no = 1
	for i in range(2,x) :
		return(fibonacci(prev))
"	if x <= 2 :
		print(prev,end = "")
	elif x == 1	or x == 2:
		print(next_no,end = "")
	else :
		print(prev_no,"",next_no,end = "")
		for i in range(2,x):
			sum_no = prev_no + next_no
			prev_no = next_no
			next_no = sum_no
			print(next_no,end = "")
"

fibonacci(int(input("Enter a number : ")))
