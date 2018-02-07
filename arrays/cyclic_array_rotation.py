#cyclic rotation of array by n times.
def rotate(arr, n):
	if len(arr) <= 1 or n == 0:
		return arr


	for i in range(0,n,1):
		temp = arr[-1]
		for j in range(len(arr)-1,0,-1):
			arr[j] = arr[j-1]

		arr[0] = temp


# Driver function

if __name__ == "__main__":
	arr= [1, 2, 3, 4, 5]

	print ("Given array is")
	for i in range(0, len(arr)):
	    print (arr[i], end = ' ')
	 
	n = 2
	rotate(arr, n)
	 
	print ("\nRotated array is")
	for i in range(0, len(arr)):
	    print (arr[i], end = ' ')