# WAP to print a fibonacci string USING FACTORIAL

def fibonacci(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		return(fibonacci(n-1) + fibonacci(n-2))


limit = int(input("Enter the no of numbers: "))
print("Here is the fabonacci series till", limit, "numbers")

for i in range(1, limit+1):
	print(fibonacci(i), end=" ")
