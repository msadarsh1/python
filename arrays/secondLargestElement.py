#secondLargestElement
def secondLargest(arr):
	
	if len(arr) <= 1:
		return arr[0]

	largest, largest_2 = 0,0

	for i in range(0, len(arr)):
		if arr[i] > largest:
			largest_2 = largest
			largest = arr[i]

	return largest_2

if __name__ == "__main__":
	arr = [0, 23, 65, 23, 17, 3]
	print(secondLargest(arr))
