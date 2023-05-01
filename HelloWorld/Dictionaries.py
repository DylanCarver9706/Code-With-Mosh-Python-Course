customer = { # Objects in JavaScript. Must be unique
    #Key / Value pairs
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])
# John Smith

numbers = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}

input = input("Phone #: ")
# print(numbers["1"])
output = ""
for map in input:
    output += numbers.get(map, "Not a number") + " " # .get works the same as numbers[{key}]
print(output)
