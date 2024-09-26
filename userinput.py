# the input syntax will always consider the input as a string
a = input("Please enter the first number ")
b = input("Enter the second number ")
print("The input was", a, ",", b)
'''print(a+b)'''  # will print ab instead of a+b
x = int(a)  # this is to simplify the code so that we don't have to
# type int after every function if we're dealing with numbers
y = int(b)

# this will create an error if a word/letter was entered instead of a number
print(a, "+", b, "=", x+y)
print("Now, we'll try out all the operators we've learnt so far")
print(a, "+", b, "=", x+y)
print(a, "-", b, "=", x-y)
print(a, "/", b, "=", x/y)
print(a, "x", b, "=", x*y)
print(a, "to the power of", b, "=", x**y)
print("The remainder of ", a, "/", b, "=", x % y)
print(a, "/", b, "(Simplified) =", x//y)
