#example for Exceptions

try:
	a = int(input("Enter First Number:"))
	b = int(input("Enter Second Number:"))
	print("Answer",a/b)

except ValueError as ve:
	print("Error,",ve)

except ZeroDivisionError as ze:
	print("Error,",ze)

except Exception as e:
	print("Error,",e)

finally:
	print("Exiting.....")
