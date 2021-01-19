from modules.login import __IS_LOGGEDIN
from modules.function import *

def main():
	show_menu()

	while 1:
		choice = str(input("User choice: ")).lower()
		
		if choice == "1":
			list_employees()
		elif choice == "2":
			add_employee()
		elif choice == "3":
			search_employee()
		elif choice == "4":
			edit_employee()
		elif choice == "5":
			delete_employee()
		elif choice == "6":
			delete_all_employees()
		elif choice == "7":
			payroll_master()
		elif choice == "8":
			payslip_all()
		elif choice == "9":
			payslip_one()
		elif choice == "c":
			clear_terminal()
		elif choice == "m":
			show_menu()
		elif choice == "q":
			exit()
		else:
			print("Invalid Option")


if __name__ == "__main__" and __IS_LOGGEDIN:
	main()