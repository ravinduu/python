nums = [1,23,54,123,64,76,75,45,32,12,324,4556,67,87,89,98]


def l_search(nums,n):
#using while loop
	i = 0
	while i < len(nums):
		if nums[i] == n:
			return True
		i += 1

	return False


def l_search(nums,n):
#using For loop
	for i in nums:
		if n == i:
			return True
	return False

try:
	srch_val = int(input("Enter value : "))

	if l_search(nums,srch_val):
		print(srch_val,"Found")
	else:
		print(srch_val,"Not Found")

except Exception as e:
	print(e)

