# Conversion of one data type to another data type
# through the use of typecasting functions
a = "12"
b = "3"
print(a+b)  # will print 123
print(int(a)+int(b))  # will print 15
# functions work if the data type of the function matches with the data type we're trying to convert
c = "thor"
d = 2
# print(int(c)+int(d))      #will show a value error
'''this was an example of explicit typecasting'''

# implicit typecasting
x = 1.2
y = 2
# automatically converts y to float. this is done b/c float lies higher in the data type hierarchy within python itself.
print(x+y)  # print(int(x+y)) will print 3 instead of 3.2
z = x+y
print(type(x))
print(type(y))
print(type(z))  # z will be float even though y is int
