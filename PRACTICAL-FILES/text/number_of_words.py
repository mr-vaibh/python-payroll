#WAP to show and count the number of words in a file which is starting or ending with an letters ‘v’.

with open("data.txt", "r") as file1:
    file_data = file1.read()
print("All Data of file in string : \n", file_data)
print("=" * 30)

starts_v = ends_v = 0

words = file_data.split()
print("All Words: ", words, ", length is  ", len(words), "\n\n")
for word in words:
    if word.lower().startswith("v") == True:
        starts_v += 1
    if word.lower().endswith("v") == True:
          ends_v += 1
        
print("Words start with 'v' is ", starts_v)
print("Words ends with 'v' is ", ends_v)