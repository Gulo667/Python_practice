ItemsInCart=0
#2 items will be added to cart

if ItemsInCart!=2: #raise Exception("Products Cart count not matching")
    pass

#2nd way is assert - the condition you set in brackets has to be always true
#if the condition is false, the assert will break tests and throw assertionError

#assert(ItemsInCart == 2)

#try, catch/except

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except:
    print("the file is out bro")

#catch the actual error from python
try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print("the file is out bro - ", e)
finally: #comes anyway if you try try and even exception is not used - this will be printed out anyway
    print("clean up resources")

try:
    with open('test.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print("the file is out bro - ", e)
finally: #comes anyway if you try try and even exception is not used - this will be printed out anyway
    #you can use it to get info that test is completed and delete the records
    #if the test gets stuck in exception part and you dont see this part, you know the test was stuck and was not finished
    print("passed case - clean up resources")