str="something something"
print(str[:9])

str1="anything"

print(str+str1)
print("{} and {}".format(str, str1)) #this one adds strings with space between because you can do whatever you want between and more smoothly

str3="something" #validate if str includes it

print(str3 in str)
print(str1 in str)
var = str.split(" ")
print(var[0])
str4 = "    great        "
#str4.strip()
print(str4)
#remove only ending  white spaces
str4.rstrip()
print(str4)