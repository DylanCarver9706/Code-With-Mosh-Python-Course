customer = { # Objects in JavaScript. Must be unique
    #Key / Value pairs
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])
# John Smith

numbers = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}

input = input("Phone #: ")
print(input)

if input in numbers:
    print(numbers[input])
