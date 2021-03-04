# Write  a program to sort a list of items using BUBBLE SORT.

def bubble_sort(array):
	"""Sorts the list using bubble sort algorithm"""

	# Outer loop for number of iterations
	for i in range(len(array) - 1):
		# Inner loop for swapping the numbers
		# will leave those last numbers which are fixed and sorted
		for j in range(len(array) - (i+1)):
			if array[j] > array[j+1]:
				array[j], array[j + 1] = array[j + 1], array[j]
	return array


new_array = bubble_sort([5, 3, 8, 6, 988, 8, 23, 54, 9, 7, 2])
print(new_array)
