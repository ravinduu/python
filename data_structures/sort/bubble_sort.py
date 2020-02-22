import random

nums = [random.randint(1,999) for i in range(23)]

def sort(nums):
	for i in range(len(nums)):
		for j in range(len(nums)-i-1):
			if nums[j] > nums[j+1]:
				nums[j],nums[j+1] = nums[j+1],nums[j]

	return nums

print("not sort:",nums)

print("sorted  :",sort(nums))

