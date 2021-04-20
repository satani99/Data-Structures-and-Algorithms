def bubblesort(arr):
	for i in range(len(arr)-1):
		for j in range(len(arr)-1-i):
			if arr[j] > arr[j+1]:
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp

		return arr

arr = [5, 9, 1, 2, 7, 3, 8, 2]
print(bubblesort(arr))
arr.sort()
print(arr)