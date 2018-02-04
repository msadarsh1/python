def insertion_sort(nums):
	for i in range(1,len(nums),1):
		j = i

		while j > 0 and nums[j-1] > nums[j]:
			swap(nums,j, j-1)
			j -= 1

	return nums

def swap(nums, i, j):
	nums[i], nums[j] = nums[j], nums[i]

if __name__ == "__main__":
	x = [4, 76, 23,5,0,-234, 53, 2,1]
	print(insertion_sort(x))