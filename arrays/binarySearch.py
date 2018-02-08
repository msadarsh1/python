#binarySearch

def binarySearch(low, high, arr, key):
	if len(arr) == 1 or arr[0] > key or arr[-1] < key :
		return -1

	middle = (low + high)//2

	if arr[middle] == key:
		return middle
	elif arr[middle] < key:
		return binarySearch(middle+1, high, arr, key)
	elif arr[middle] > key:
		return binarySearch(low, middle-1, arr, key)
	else:
		return -1

if __name__ == "__main__":
	arr = [1, 5, 11, 21, 56, 82, 93]
	key = 93
	x = binarySearch(0, len(arr)-1, arr, key)
	print(x)