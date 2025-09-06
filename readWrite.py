file = open('test.txt')

#read all the contents of txt file
#print(file.read())

#read only first 2 characters from file
#print(file.read(2))

#read 5 letters from file
#print(file.read(5)) #tab before switching to other line also counts as one character, so only 4 letters will be printed out

#read linebyline:
#print(file.readlines())

#read line by line - the first will read 1st line, 2nd will read 2nd line:
# print(file.readline())
# print(file.readline())

#print line by line using readline method:

# line = file.readline()

# while line !="":
#     print(line)
#     line = file.readline()

#readlines printed out as list
#print(file.readlines())

for line in file.readlines():
    print(line)

file.close()