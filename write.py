# file=open('test.txt')


# file.close()

#the command to open file which automatically gets closed
#read the file and store all the lines in list
#reverse the list
#write all the list back in text file

with open('test.txt', 'r') as reader:
    content = reader.readlines() #['abc\n', 'bvdsf\n', 'cat\n', 'dog\n', 'elephand']
    print(content) #['abc\n', 'bvdsf\n', 'cat\n', 'dog\n', 'elephand']
    print(reversed(content))
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line) #if the last line is not ending with """\n""" part, the last two values will be written together in reversed
