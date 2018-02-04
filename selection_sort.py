def selection_sort(nums):
	for i in range(0,len(nums),1):
		index = i

		for j in range(i+1, len(nums),1):
			if nums[index] > nums[j]:
				index = j

		if index != i:
			swap(nums, i, index)

	return nums

def swap(nums, i, j):
	nums[i], nums[j] = nums[j], nums[i]


if __name__ == "__main__":

	x = [12, 0, 93, -12, -94, 83]
	print(selection_sort(x))