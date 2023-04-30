temperature = 35

if temperature > 30: #
    print("It's a hot day!") # < <= > >= == !=
else:
    print("It's not a hot day")

name = input("What is your name? ")

if len(name) < 3:
    print("Your name mst be at least 3 characters")
elif len(name) > 50:
    print("Your name can't be more than 50 characters")
else:
    print("Name looks good!")