# implementation of stack using list
stack = []
choice = 'y'

print('1. Push\n2. Pop\n3. Display elements of stack')

while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        elem = input("Enter your element which you want to push: ")
        stack.append(elem)
    elif choice == 2:
        if stack == []:
            print("Stack is empty... cannot delete element")
        else:
            print("Deleted element is: " + stack.pop())
    elif choice == 3:
        for i in range(len(stack) - 1, -1, -1):
            print(stack[i])
    else:
        print("Wrong input !!")
