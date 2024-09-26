a = "wassup"
print("Yo,", a)
b = 'He said, "Oh what a beautiful day!"'  # understandable.
c = "He said, \"Oh what a beautiful day!\""  # another way for the same result
print(b)
print(c)
d = """Rohan: Hey man! How you doin'?
John: Nothing much mate! 'tis gettin' pretty hot nowadays innit?"""  # multiple line strings. same result with 3 single quotes
print(d)
# this can be used with \n for some nice organised text ig
x = "Google"
print(x[0])  # this will give us the first letter in the string x
print(x[1])  # so on and on till the characters end
print(x[2])
print(x[3])
print(x[4])
print(x[5])
# print(x[6]) # index error
# a better way to execute this is for loops
print("Let's use a for loop now")
for character in x:
    print(character)
