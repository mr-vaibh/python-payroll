from .function import clear_terminal

__IS_LOGGEDIN = False

while True:
	username = str(input("Enter username: "))
	password = str(input("Enter password: "))

	if username == "admin" and password == "admin1183":
		__IS_LOGGEDIN = True
		clear_terminal()
		break
	else:
		clear_terminal()
		print("Access denied, Wrong Credentials\n")