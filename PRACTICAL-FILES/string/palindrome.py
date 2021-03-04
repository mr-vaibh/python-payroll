# Write  a program to show entered string is a palindrome or not.

# You can also import this function from anywhere else
def check_palindrome(string):
	"""To check if the passed string can be read forward same as backward"""
	if string == string[::-1]:
		print(f"Yes, {string} is a palindrome.")
	else:
		print(f"No, {string} is NOT a palindrome.")


def main():
	user_input = str(input('Type a word: '))
	check_palindrome(user_input)


if __name__ == "__main__":
	while True:
		main()