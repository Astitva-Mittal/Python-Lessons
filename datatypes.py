# first, lets talk about variables, eg a, b, c, "strings", etc.
a = 1  # integer data type (Numeric Data)
print(a)
print("The type of a is", type(a))
b = True  # Boolean data (True/False)
print(b)  # here, it will print True
print("The type of b is", type(b))
c = "String"  # string data type
print(c)  # here it will print "string"
print("The type of c is", type(c))
d = None  # None type
print(d)
print("The type of d is", type(d))
e = complex(1, 2)  # complex data type (Numeric Data)
print(e)
print("The type of e is", type(e))
list = [2, 3, 4, 2.5, [-4, 5], ["damn"]]  # List data, Sequential, Mutable
print(list)

tuple = (("Josh", "is"), "smart")
# tuple data, Sequential, immutable(can't be changed within a program ig)
print(tuple)
