import pickle

def write_data():
    with open('student.log', 'wb') as file:
        record = []
        no_of_rec = int(input("How many records to add: "))
        for i in range(no_of_rec):
            roll_no = int(input("Enter Roll No.: "))
            name = input("Enter Name: ")
            standard = input("Enter Standard: ")
            perc = float(input("Enter Percentage: "))
            data = [roll_no, name, standard, perc]

            record.append(data)
        pickle.dump(record, file)

def read_data():
    with open('student.log', 'rb') as file:
        data = pickle.load(file)

        for row in data:
            roll_no, name, standard, perc = row[0], row[1], row[2], row[3]
            print(roll_no, name, standard, perc)

def search_data():
    with open('student.log', 'rb') as file:
        data = pickle.load(file)

        roll_no = int(input("Search via Roll No.: "))

        for row in data:
            if row[0] == roll_no:
                print(row)



if __name__ == "__main__":
    print('1. Insert Student Record\n2. Display all students record\n3. Search for a student')

    while True:
        choice = input("Choice: ")
        if choice == "1":
            write_data()
        elif choice == "2":
            read_data()
        elif choice == "3":
            search_data()