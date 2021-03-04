# This function prints a pyramid
def make_pyramid(n):
	k = n - 1 # for spaces
 
	# loop for number of rows
	for i in range(0, n):
		# loop for number spaces
		for j in range(0, k):
			print(end=" ")
		k -= 1
	 
		# loop for number of columns
		for j in range(0, i+1):
			print("* ", end="")
		print("\r")

n = int(input("Enter pyramid size in numeric: "))
make_pyramid(n)