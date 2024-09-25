# \n is an escape sequence wi=hich is used to insert new lines into strings
print("This is to show that comments are not printed\nor termed as syntax errors.")
# comments are basically used for communication or to remind us of the program in the future if we ever forget.
# comments can also be used to hide codes which may or may not be useful in special cases.
'''These can also be used as comments. Rather, they're more versatile 
since they are multiline comments!'''
"""Tripple Double qoutes also produce the same results!"""
# now about escape sequences
print("This is to show how to insert \"Double Quotes\" without producing a syntax error")
# here, \" is an escape sequence which
# can be used to insert double quotes into strings
'''So technically speaking, an escape character is a backslash \ 
followed by the character (using which would produce a syntax error)
that we want to insert'''
print("\nNow, More on print statements")
# here, "sep=" is a serparator.
print("\nHey", 5, 6, 7, "Bye", sep="-", end="-")
print("This is a Different code but in the previous line\n'end=' adds or more specifically, removes the default \ n that accompanies\nthe end of every code by the end statement of choice.")
