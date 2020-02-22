nums = [32,43,123,12,43,5743,9438,4343,4321,1,32,54,437,672,65,34,163,781,32,4983,56,68,80,9,7,66,6]

def binary_search(nums,val):
	nums.sort()
	lower = 0
	upper = len(nums)-1

	while lower <= upper :
		mid = (lower+upper)//2
		if nums[mid] == val:
			return True
		else:
			if nums[mid] > val:
				upper = mid-1
			else:
				lower = mid+1
	return False



val = int(input("Enter value to search :"))

if binary_search(nums,val):
	print(val,"Found")
else:
	print(val,"not Found")
