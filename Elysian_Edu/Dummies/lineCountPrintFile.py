lines = []
with open("file_reader.txt") as file:
    lines = file.readlines()

count = 0
for line in lines:
    count += 1
    print(f"line {count}: {line}")