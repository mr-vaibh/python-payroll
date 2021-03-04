from pyfiglet import Figlet

# Using Figlet class
figlet_obj = Figlet(font='slant')

def make_magic():
	word = str(input("Type text... : "))
	print(figlet_obj.renderText(word))
	
	make_magic()

# word = 'Vaibhav is a BLESSED soul'
make_magic()