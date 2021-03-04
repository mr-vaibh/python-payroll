# Using RECURSION, WAP to calculate factorial of entered numbers

def factorial(num):
	return (1 if num == 0 else num * factorial(num - 1))

while True:
	user_input = int(input("Enter any positive number: "))
	answer = factorial(user_input)
	
	print(answer)