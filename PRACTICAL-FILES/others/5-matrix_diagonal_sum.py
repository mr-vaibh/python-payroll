# WAP to show the sum of diagonals of a 2-d matrix.

def diagonal_sum(matrix):
	n = len(matrix)
	diagonal1 = diagonal2 = ""
	sum_of_diagonal1 = sum_of_diagonal2 = 0

	for i, j in zip(range(n), range(n)):
		diagonal1 += str(matrix[i][i]) + ", "
		sum_of_diagonal1 += matrix[i][i]
		
		diagonal2 += str(matrix[i][-(j+1)]) + ", "
		sum_of_diagonal2 += matrix[i][-(j + 1)]
	
	print(f"First Diagonal : {diagonal1}\nSecond Diagonal : {diagonal2}")
	return sum_of_diagonal1 + sum_of_diagonal2


def take_matrix_input():
	"""To take matrix input form user"""
	matrix = []
	dimension = int(input("Number of rows of SQUARE MATRIX: "))
	for i in range(1, dimension+1):
		while True:
			row = input(f"Row {i}: ").split(" ")
			# Convert string row into integer list
			row[:] = map(lambda x: int(x), row)
			
			if len(row) == dimension:
				matrix.append(row)
				break
			else:
				print(f"The input you entered is not {dimension}X{dimension}")
	return matrix

sum = diagonal_sum(take_matrix_input())
print("The sum of both the diagonals of given matrix is", sum)