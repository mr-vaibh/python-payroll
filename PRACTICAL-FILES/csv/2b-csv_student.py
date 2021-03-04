import csv

def write_record():
    with open('student.csv', 'w', newline='') as file:
        file_writer = csv.writer(file)
        file_writer.writerow(['Roll No', 'Name', 'Class', 'Marks'])

        record = []

        while True:
            roll_no = int(input("Enter Roll No:"))
            name = input("Enter Name: ")
            student_class = input("Enter Class: ")
            marks = input("Enter Marks: ")

            student_array = [roll_no, name, student_class, marks]
            record.append(student_array)

            choice = input("Want to enter more records? (y/n): ")
            if choice.lower() == "n":
                break
        
        file_writer.writerows(record)

def read_data():
    with open('student.csv', 'r') as file:
        file_reader = csv.reader(file)

        for row in file_reader:
            print(row)


if __name__ == "__main__":
    print('1. Insert record\n2. Display record')

    while True:
        choice = input("Choice: ")
        if choice == "1":
            write_record()
        elif choice == "2":
            read_data()