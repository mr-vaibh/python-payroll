# Take the range and print all the non-prime numbers in the given range

def non_prime(start_range, end_range):
	for i in range(start_range, end_range+1):
		for j in range(2, i):
			if (i % j == 0):
				print(i, "is a non-prime number.")
				break

user_input1 = int(input("Enter the starting range : "))
user_input2 = int(input("Enter the starting range : "))
non_prime(user_input1, user_input2)