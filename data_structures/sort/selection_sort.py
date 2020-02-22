import random

nums = [random.randint(1,999) for i in range(23)]

def sort(nums):
	for i in range(len(nums)-1):
		min_pos = i
		for j in range(i,len(nums)):
			if nums[j] < nums[min_pos]:
				min_pos = j

		nums[i],nums[min_pos] = nums[min_pos],nums[i]

	return nums

print("not sort:",nums)
 
print("sorted  :",sort(nums))
