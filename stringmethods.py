a = "wow!!"
print(len(a))  # strings are immutable
print(a.upper())  # it makes a new string temporarily which is uppercase
print(a)
b = "WOW!!"
print(b.lower())
print(b)
print(a.rstrip("!"))  # strips trailing characters specified
print(a.replace("w", "b"))  # replaces characters
print(a.replace("w", "b").rstrip("!").upper())  # experiment
c = "damn thats crazy!"
print(c.split(" "))
# so strip will be the last method to be used. IG
print(c.upper().rstrip("!").split(" "))
print(c.capitalize())  # truns the first character into uppercase
print(c.capitalize().center(60))
# will basically add the specified number of spaces before the string
print(c.endswith("!"))  # checks if the string ends with the specified character
print(c.endswith("@"))  # checks if the string ends with the specified character
print(c.endswith("thats", 3, 10))  # can also check inbetween strings like this
print(c.find("s"))  # easy stuff
# print(c[9]) #can check it with this
print(c.find("is"))  # will show -1 if characters not found
# print(c.index("is"))
# will show error if the searched character is not available in the string
print(c.isalnum())  # is the string alphanumeric
d = "18"
print(d.isalnum())
e = "hey"
print(e.isalpha())  # is it alphabetical
print(e.isprintable())
f = "hola\n"  # \n is an invisible nonprintable item
print(f.isprintable())  # will return false
"""issapce"""
print(c.isspace())  # will only detect wide spaces
g = "         "
print(g.isspace())
print(g.istitle())  # will detect if the first letter of each word is caps
h = "Hey Whatsup!"
print(h.istitle())
print(g.startswith("Hey"))
print(h.startswith("Hey"))
print(h.swapcase())
print(c.title())
"""DONE"""
