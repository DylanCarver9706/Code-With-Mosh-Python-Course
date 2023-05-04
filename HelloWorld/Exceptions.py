age = int(input('Age: '))
print(age)

# If I run this program and enter non integers, I should get this:

# ValueError: invalid literal for int() with base 10: 'asd'
# Translation: The wrong value type was passed in

# Process finished with exit code 1
# Anything besides an exit code of 0 is a crash

try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print("Invalid value passed in")


try:
    age = int(input('Age: '))
    income = 20000
    rick = income / age
    print(age)
except ValueError:
    print("Invalid value passed in")

# If I run this and pass in 0 for age, we get a crash

# Traceback (most recent call last):
#   File "C:\Users\Dylan\PycharmProjects\Code-With-Mosh-Python-Course\HelloWorld\Exceptions.py", line 22, in <module>
#     rick = income / age
# ZeroDivisionError: division by zero

#ZeroDivisionError = Cannot divide by 0 error

try:
    age = int(input('Age: '))
    income = 20000
    rick = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be zero')
except ValueError:
    print("Invalid value passed in")