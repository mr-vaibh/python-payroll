import pickle

def save_todo():
    # take user input to take the amount of data
    number_of_data = int(input('Enter the number of data : '))
    data = []

    for i in range(1, number_of_data+1):
        raw = input('Type the task '+str(i)+' : ')
        data.append(raw)

    with open('memo.dat', 'wb') as file:
        pickle.dump(data, file)

def load_todo():
    # open a file, where you stored the pickled data
    with open('memo.dat', 'rb') as file:
        data = pickle.load(file)

    print('Here are all your reminders:')

    cnt = 1
    for item in data:
        print('Your no. ', cnt, ' task is : ', item)
        cnt += 1

if __name__ == "__main__":
    print('1. Add Task\n2. Show all To-do(s)')
    
    while True:
        choice = input("Choice: ")
        if choice == "1":
            save_todo()
        elif choice == "2":
            load_todo()
