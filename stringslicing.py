string = "Hey Wassup??"
length = len(string)  # will provide the lenth og the string
print("The length of the string is", length)
# Including 0 but not 5. so basically 0 to 4
print("Now printing the initial 5 letters of the string", string[0:5])
print(string[0:-3])  # here the compiler will print 0 to len-3
print(string[:5])  # the missing 0 will automatically be understood
print(string[2:7])
print(string[-12])  # will print the first letter of the string
# nm = "Harry"
# print(nm[-4])
