# Use `with` function whenever possible for clean code

with open('text_file.txt', 'w+') as file:
    file.write('The output is \nMy work-status is')
    file.flush()

    status = 'OK'

    file.write(status)
    file.write('\n')

    file.write('Finally over\n')
    file.flush()

print("File successfully created !")