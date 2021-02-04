from os import system, name
import datetime
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
			print("No employee record found\n")
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
		cursor.execute(f"SELECT * FROM `employees` WHERE emp_id='{emp_id}' ")
		all_rows = cursor.fetchall()
		if len(all_rows) == 0:
			print("No employee record found")
		else:
			table = tabulate(all_rows, headers=["Emp No", "Name", "Gender", "DOB", "Designation", "Department", "Category", "Basic", "HRA", "Conveyance", "Tax", "Gross", "Net Salary"], tablefmt="fancy_grid")
			print(table)
	except Exception as e:
		print("Encountered an ERROR:", e)


def edit_employee():
	emp_id = int(input("Enter Employee ID: "))
	cursor.execute(f"SELECT * FROM `employees` WHERE emp_id='{emp_id}' ")
	emp_record = cursor.fetchone()
	if cursor.rowcount < 0:
		print("Employee does not exist")
	else:
		table = tabulate([emp_record], headers=["Emp No", "Name", "Gender", "DOB", "Designation", "Department", "Category", "Basic", "HRA", "Conveyance", "Tax", "Gross", "Net Salary"], tablefmt="fancy_grid")
		print(table)
		print("\n\t\t1->Name    4->Designation  7->Basic       10->Tax\n\
\t\t2->Gender  5->Department   8->HRA         11->Gross\n\
\t\t3->DOB     6->Category     9->Conveyance  12->Net Salary" )
		while True:
			to_modify = int(input("Which field is to modify? [1-12] :"))
			if to_modify == 1:
				field_to_be_modified = "name"
				modified_value = str(input("Enter new Name: "))
			elif to_modify == 2:
				field_to_be_modified = "gender"
				modified_value = str(input("Enter new Gender: ")).upper()
			elif to_modify == 3:
				field_to_be_modified = "dob"
				modified_value = str(input("Enter new DOB [yyyy-mm-dd]: "))
			elif to_modify == 4:
				field_to_be_modified = "designation"
				modified_value = str(input("Enter new Designation: "))
			elif to_modify == 5:
				field_to_be_modified = "department"
				modified_value = str(input("Enter new Department: "))
			elif to_modify == 6:
				field_to_be_modified = "category"
				modified_value = str(input("Enter new Category: ")).upper()
			elif to_modify == 7:
				field_to_be_modified = "basic"
				modified_value = int(input("Enter new Basic: "))
			elif to_modify == 8:
				field_to_be_modified = "hra"
				modified_value = int(input("Enter new HRA: "))
			elif to_modify == 9:
				field_to_be_modified = "conveyance"
				modified_value = int(input("Enter new Conveyance: "))
			elif to_modify == 10:
				field_to_be_modified = "tax"
				modified_value = int(input("Enter new Tax: "))
			elif to_modify == 11:
				field_to_be_modified = "gross"
				modified_value = int(input("Enter new Gross: "))
			elif to_modify == 12:
				field_to_be_modified = "net_salary"
				modified_value = int(input("Enter new Net Salary: "))
			
			if isinstance(modified_value, str):
				cursor.execute(f"UPDATE employees SET {field_to_be_modified} = '{modified_value}' WHERE emp_id={emp_id}")
			elif isinstance(modified_value, int):
				cursor.execute(f"UPDATE employees SET {field_to_be_modified} = {modified_value} WHERE emp_id={emp_id}")
				 
			db.commit()
			print("Employee successfully modified")

			if input("Do you want to modify more in this record? (y/n): ") != "y":
				break


def delete_employee():
	try:
		emp_id = int(input("Enter Employee ID: "))

		cursor.execute(f"DELETE FROM `employees` WHERE emp_id={emp_id}")
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
	try:
		cursor.execute("SELECT * FROM employees")
		all_rows = cursor.fetchall()
		print("\n\n" + 148 * "*" + "\n\t\t\t\t\t\t\t\t Payroll Master" + "\n" + 148 * "*")
		print("Date and Time: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		print(148 * "-")
		
		table = tabulate(all_rows, headers=["Emp No", "Name", "Gender", "DOB", "Designation", "Department", "Category", "Basic", "HRA", "Conveyance", "Tax", "Gross", "Net Salary"])
		print(table)
		print(148 * "-" + "\n")
	except Exception as e:
		print("Encountered an ERROR:", e, "\n")


def payslip_all():
	try:
		cursor.execute("SELECT emp_id, name, designation, basic, hra, conveyance, tax, gross, net_salary FROM employees")
		all_rows = cursor.fetchall()
		print("\n\n" + 100 * "*" + "\n\t\t\t\t  Payslip (ALL EMPLOYEES)" + "\n" + 100 * "*")
		print("Date and Time: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		print(100 * "-")
		
		table = tabulate(all_rows, headers=["Emp No", "Name", "Designation", "Basic", "HRA", "Conveyance", "Tax", "Gross", "Net Salary"])
		print(table)
		print(100 * "-" + "\n")
	except Exception as e:
		print("Encountered an ERROR:", e, "\n")


def payslip_one():
	try:
		emp_id = int(input("Enter Employee ID: "))
		cursor.execute(f"SELECT emp_id, name, designation, basic, hra, conveyance, tax, gross, net_salary FROM employees WHERE emp_id={emp_id}")
		emp_record = cursor.fetchone()
		print("\n\n" + 100 * "*" + "\n\t\t\t\t  Payslip (ALL EMPLOYEES)" + "\n" + 100 * "*")
		print("Date and Time: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		print(100 * "-")
		
		table = tabulate([emp_record], headers=["Emp No", "Name", "Designation", "Basic", "HRA", "Conveyance", "Tax", "Gross", "Net Salary"])
		print(table)
		print(100 * "-" + "\n")
	except Exception as e:
		print("Encountered an ERROR:", e, "\n")