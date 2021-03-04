# Write a program to show elements of a two dimensional list in a 2-d array format.

import random

def make_matrix(rows, cols):
	List = []
	for i in range(rows):
		innerList = []
		for j in range(cols):
			innerList.append(random.randrange(1, 99))
		List.append(innerList)
	return List


input_rows = int(input("Number of rows: "))
input_cols = int(input("Number of columns: "))

matrix = make_matrix(input_rows, input_cols)

# List of list form
print("Raw Form:\n", matrix, "\n")


# Organised form of matrix
for row in matrix:
	for elem in row:
		print(elem, end=" ")
	print("")