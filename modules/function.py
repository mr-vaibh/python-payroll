from os import system, name
from .conn import db, cursor
from tabulate import tabulate

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
	try:
		cursor.execute("SELECT * FROM employees")
		all_rows = cursor.fetchall()
		if len(all_rows) == 0:
			print("No employee record found")
		else:
			table = tabulate(all_rows, headers=["Emp No", "Name", "Gender", "DOB", "Designation", "Department", "Category", "Basic", "HRA", "Conveyance", "Tax", "Gross", "Net Salary"], tablefmt="fancy_grid")
			print(table)
			print(f"{cursor.rowcount} employee record(s) found")
	except Exception as e:
		print("Encountered an ERROR:", e, "\n")


def add_employee():
	try:
		print("---- Enter following information (Ctrl+C to go back) ----")
		name = str(input("Employee Name: "))
		gender = str(input("Gender: ")).upper()
		dob = str(input("Date of Birth [yyyy-mm-dd]: "))
		designation = str(input("Designation: "))
		department = str(input("Department: "))
		category = str(input("Category: ")).upper()
		basic = float(input("Basic (salary): "))

		hra = float(basic*0.5)
		conveyance = float(basic*0.15)
		tax = float(basic*0.18)
		gross = float(basic + hra + conveyance)

		net_salary = float(gross - tax)

		insert_query = f"INSERT INTO `employees` (name, gender, dob, designation, department, category,basic, hra, conveyance, tax, gross, net_salary) VALUES ('{name}', '{gender}', '{dob}', '{designation}', '{department}', '{category}', '{basic}', '{hra}', '{conveyance}', '{tax}', '{gross}', '{net_salary}')"

		cursor.execute(insert_query)
		db.commit()

		print("New Employee ADDED successfully\n")
	except Exception as e:
		print("Encountered an ERROR:", e, "\n")


def search_employee():
	try:
		emp_id = int(input("Enter Employee ID: "))
		cursor.execute(f"SELECT * FROM `employees` WHERE id='{emp_id}' ")
		all_rows = cursor.fetchall()
		if len(all_rows) == 0:
			print("No employee record found")
		else:
			table = tabulate(all_rows, headers=["Emp No", "Name", "Gender", "DOB", "Designation", "Department", "Category", "Basic", "HRA", "Conveyance", "Tax", "Gross", "Net Salary"], tablefmt="fancy_grid")
			print(table)
	except Exception as e:
		print("Encountered an ERROR:", e)


def edit_employee():
	print("Edit an employee\n")


def delete_employee():
	try:
		emp_id = int(input("Enter Employee ID: "))

		cursor.execute(f"DELETE FROM `employees` WHERE id={emp_id}")
		db.commit()

		print("Employee DELETED successfully\n")
	except Exception as e:
		print("Encountered an ERROR:", e, "\n")


def delete_all_employees():
	try:
		cursor.execute(f"DELETE FROM `employees`")
		db.commit()

		print("All employee record DELETED successfully\n")
	except Exception as e:
		print("Encountered an ERROR:", e, "\n")


def payroll_master():
	print("Payroll Master\n")


def payslip_all():
	print("Payslip of all employees\n")


def payslip_one():
	print("Payslip of one employee")
