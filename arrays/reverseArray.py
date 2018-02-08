#reverseArray

def reverseArray(arr):
	if len(arr) == 1:
		return arr

	low = 0
	high = len(arr)-1

	while low < high:
		temp = arr[low]
		arr[low] = arr[high]
		arr[high] = temp
		low += 1
		high -= 1

	return arr

if __name__ == "__main__":
	arr = [1,2,3,4,5]
	x = reverseArray(arr)
	print(x)