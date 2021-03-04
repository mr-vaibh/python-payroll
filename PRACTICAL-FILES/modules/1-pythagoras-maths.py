from math import sqrt

print('Calculate right triangle sides.')
print('Assume the sides are a, b, c and c is the hypotenuse (the side opposite the right angle')
formula = input('Which side (a, b, c) do you wish to calculate? side> ')

# I made this function so that we don't have to make code clean
def take_input(side):
	return float(input(f"Input the length of side {side}: "))

if formula == 'c':
	side_a = take_input('a')
	side_b = take_input('b')

	side_c = sqrt(side_a**2 + side_b**2)
	
	print(f'The length of side c is: {side_c} units')

elif formula == 'a':
	side_b = take_input('b')
	side_c = take_input('c')
	
	side_a = sqrt((side_c**2) - (side_b**2))

	print(f'The length of side a is: {side_a} units')

elif formula == 'b':
	side_a = take_input('a')
	side_c = take_input('c')
		
	side_b = sqrt(side_c**2 - side_a**2)
	
	print(f'The length of side b is: {side_b} units')

else:
	print('Please select a side between a, b, c')