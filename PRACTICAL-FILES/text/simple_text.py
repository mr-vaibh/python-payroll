file = open('student.txt', 'w')  # for writing

for i in range(5):
    name = input("Enter name of student: ")
    file.write(name + '\n')
file.close()

file = open('student.txt', 'r')  # for reading
data = file.read()

print(data)

file.close()