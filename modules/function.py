from os import system, name
from .conn import cursor

def show_menu():
	print(f'''{"*"*57}\n*\t\t Welcome to MRV Payroll \t\t*\n{"*"*57}\n
\t1. List ALL Employees
\t2. Add Employee
\t3. Search Employee
\t4. Edit Employee
\t5. Delete Employee
\t6. Delete ALL Employees
\t7. Payroll Master
\t8. Pay Slip (for ALL Employees)
\t9. Pay Slip (for single Employees)\n
[C to clear screen]
[M to print Menu again]
[Q to quit]
''' )


def clear_terminal(): 
	"Clears the terminal"
	if name == 'nt':
		_ = system('cls') # for windows 
	else:
		_ = system('clear')  # for mac and linux(here, os.name is 'posix')


def list_employees():
	name = str(input("Employee Name: "))
	contact = str(input("Contact  [email/phone]: "))
	gender = str(input("Gender: "))
	dob = str(input("Date of Birth [dd-mm-yyyy]: "))
	designation = str(input("Designation: "))
	department = str(input("Department: "))
	category = str(input("Category: "))
	basic = float(input("Basic (salary): "))
	hra = float(input("HRA: "))
	conveyance = float(input("Conveyance: "))
	bonus = float(input("Bonus: "))
	print("List of all employees\n")

def add_employee():
	print("Add an employee\n")

def search_employee():
	print("Search employee\n")

def edit_employee():
	print("Edit an employee\n")

def delete_employee():
	print("Delete an employee\n")

def delete_all_employees():
	print("Delete all the employees\n")

def payroll_master():
	print("Payroll Master\n")

def payslip_all():
	print("Payslip of all employees\n")

def payslip_one():
	print("Payslip of one employee")
