# Write  a program to show statistics of characters in the given line(to counts the number of alphabets, digits, uppercase, lowercase, spaces and other characters).

import csv

# FUNCITON DECLARATION
def analyse_string(string):
	"""Make a report of a string passed by user"""
	alphanumerics = alphabets = digits = spaces = uppercases = lowercases = special_chars = 0
	for char in string:
		if char.isalnum():
			alphanumerics += 1
			if char.isalpha():
				alphabets += 1
				if char.isupper():
					uppercases += 1
				elif char.islower():
					lowercases += 1
			elif char.isdigit():
				digits += 1
		elif char.isspace():
			spaces += 1
		else:
			special_chars += 1
	
	print(f'''Total number of characters, {len(string)}
No.of Alphabets and Digits, {alphanumerics})
No.of Alphabets ONLY, {alphabets}
No. of Digits ONLY, {digits}
No.of Capital letters, {uppercases}
No. of Small Letters, {lowercases}
No. of Spaces, {spaces}
No of Special/Other characters, {special_chars}\n''' )

	# Making an array of data
	string_object = {
		"Total number of characters": len(string),
		"No.of Alphabets and Digits": alphanumerics,
		"No.of Alphabets ONLY": alphabets,
		"No. of Digits ONLY": digits,
		"No.of Capital letters": uppercases,
		"No. of Small Letters": lowercases,
		"No. of Spaces": spaces,
		"No of Special/Other characters": special_chars
	}

	# Ternary Operator for typical if/else statement
	generate_report(string, string_object) if input("Generate Report (y/n): ") == 'y' else print("\n")



def generate_report(string, string_object):
	"""Generate CSV file saving the analytics of the `string given by user` """

	try:
		with open('report.csv', mode='w', newline="") as file:
			writer = csv.writer(file)

			writer.writerow([string])

			for key in string_object:
				writer.writerow([key, string_object[key]])
		print('Report File exported')
	except:
		print('Error: Please check and remove if a file named `report.csv` already exists.')

			

# ENTRY POINT
user_input = str(input("Enter a string: "))
analyse_string(user_input)