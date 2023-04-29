course = 'Python for Beginners'
print(len(course)) # General purpose function to count things. In this case, strings characters
print(course.upper()) # Method when talking about strings. Does not change the variable state, only modify for method use
print(course.lower())
print(course.find('o')) # method to return the index of the first instance of the parameter. Case sensetive
# 4
print(course.find('Beginners')) #returns inted of where the string starts. Returns -1 if not found
# 11
print(course.replace('Beginners', 'Absolute Beginners')) # Find first instance and replace
# 'Python for Absolute Beginners'
print('Python' in course) # Boolean expression
# True
