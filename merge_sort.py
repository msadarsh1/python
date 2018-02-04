def merge_sort(nums):
	if len(nums) <= 1:
		return

	middle_index = len(nums)//2
	left_half = nums[:middle_index]
	right_half = nums[middle_index:]

	merge_sort(left_half)
	merge_sort(right_half)

	i,j,k = 0,0,0
	
	while i < len(left_half) and j < len(right_half):
		if left_half[i] <= right_half[j]:
			nums[k] = left_half[i]
			i += 1

		else:
			nums[k] = right_half[j]
			j += 1

		k+= 1

	while i < len(left_half):
		nums[k] = left_half[i]
		i += 1
		k += 1

	while j < len(right_half):
		nums[k] = right_half[j]
		j += 1
		k += 1

if __name__ == "__main__":
	x = [30, 19, 87, 22, -1, 0, 937, 48, 1]
	merge_sort(x)
	print(x)