def quick_sort(nums, low, high):
	if low >= high:
		return

	pivot_index = partition(nums, low, high)
	quick_sort(nums,low, pivot_index -1)
	quick_sort(nums, pivot_index+1, high)


def partition(nums, low, high):

	if low >= high:
		return

	pivot_index = (low + high) // 2
	i = low
	swap(nums, high, pivot_index)

	for j in range(low,high,1):
		if nums[j] < nums[high]:
			swap(nums, j, i)
			i += 1

	swap(nums, high, i)

	return i


def swap(nums, i, j):
	nums[i], nums[j] = nums[j], nums[i]


if __name__ == "__main__":
	x = [49, 23, 4, 0, -12, 42, 99, 124, -142, 1]
	quick_sort(x,0,len(x)-1)
	print(x)