# this program simply prints a string in vertical reverse order

string = str(input("Enter a string: "))
length = len(string)

initial = 0

# the range in the loop below basically deals with length
for i in range(-1, -(length + 1), -1):
	print(string[initial] + "\t" + string[i])
	initial += 1