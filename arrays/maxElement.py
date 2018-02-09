#maxElement
def maxElement(arr):
	if len(arr) == 1:
		return arr[0]

	max_x = arr[0]

	for i in range(len(arr)):
		if arr[i] > max_x:
			max_x = arr[i]

	return max_x

if __name__ == "__main__":
	arr = [0, -12,-30, 1,-12, -54]
	print(maxElement(arr))