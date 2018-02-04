
def bubble_sort(nums):


	for i in range(0,len(nums),1):
		for j in range(1, len(nums)-i,1):
			if nums[j-1] > nums[j]:
				swap(nums,j-1,j)

	return nums


def swap(nums, i, j):
	nums[i], nums[j] = nums[j], nums[i]

if __name__ == "__main__":
	x = [30, 19, 87, 22, -1, 0, 937, 48, 1]
	y = bubble_sort(x)
	print(y)