course1 = "Python's Course for Beginners" # Need double quotes is string variable contains an apostrophe
course2 = 'Python for "Beginners"' # Will put the word in double quotes in the string variable
course3 = ''' 
Hi Dylan,

Here is our first email to you.

Thanke,
The Support Team
'''


course = 'Python for Beginners'

# print(course[0]) # Strings are indexed like JavaScript arrays ([0] = first character, [-1] = last)
# print(course[0:3]) # Will return letters at inted 0-2, but not 3: 'Pyt'
print(course[2:]) # Will return from tha index to the end: thon for Beginners
# print(course[:]) # Will return copy of string. Assumes: Index of 0:Sting Length
name = 'Jennifer'
print(name[1:-1]) # Will start from index of 1 and end at -1 (The first index going backwards): ennife
print(course)
