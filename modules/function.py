from os import system, name
from .conn import db, cursor

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
	print("List of all employees\n")

def add_employee():
	print("---- Enter following information ----")
	name = str(input("Employee Name: "))
	contact = str(input("Contact  [email/phone]: ")).lower()
	gender = str(input("Gender: ")).upper()
	dob = str(input("Date of Birth [yyyy-mm-dd]: "))
	designation = str(input("Designation: ")).upper()
	department = str(input("Department: ")).upper()
	category = str(input("Category: ")).upper()
	basic = float(input("Basic (salary): "))

	hra = float(basic*0.5)
	conveyance = float(basic*0.15)
	tax = float(basic*0.18)
	gross = float(basic + hra + conveyance)

	net_salary = float(gross - tax)

	insert_query = f'''INSERT INTO `employees` (name, contact, gender, dob, designation, department, category,basic, hra, conveyance, tax, gross, net_salary) VALUES ('{name}', '{contact}', '{gender}', '{dob}', '{designation}', '{department}', '{category}', '{basic}', '{hra}', '{conveyance}', '{tax}', '{gross}', '{net_salary}')'''

	cursor.execute(insert_query)
	db.commit()

	print("New Employee added successfully\n")

def search_employee():
	cursor.execute("SELECT * FROM `employees`")

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
