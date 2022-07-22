#########################################
print("\nWay #1: \n")

with open("file_reader.txt") as file1:
    contents = file1.read()
    print(contents)

file1.close()

print("\n")

#########################################

print("\nWay #2: \n")

with open("file_reader.txt") as file2:
    contents = file2.readlines()    #readlines() returns an array of Strings
    for i in range(len(contents)):
        print(contents[i], end = "")

file2.close()

print("\n")

#########################################

print("\nWay #3: \n")

with open("file_reader.txt", "r") as file3:
    contents = file3.readlines()    #readlines() returns an array of Strings
    for i in range(len(contents)):
        print(contents[i], end = "")

file3.close()

print("\n")

#########################################

print("\nWay #4: \n")

file4 = open("file_reader.txt", "r")
print(file4.read())

file4.close()

print("\n")

#########################################

print("\nWay #5: \n")

file5 = open("file_reader.txt", "r")
file5 = file5.readlines()

for i in range(len(file5)):
    print(file5[i], end = "")

print("\n")

#########################################