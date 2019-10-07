def list_count(nums):
	count = 0
	for num in nums:
		if num==1:
			count=count+1
	return count
print(list_count([1,4,6,7,3,1,1]))

