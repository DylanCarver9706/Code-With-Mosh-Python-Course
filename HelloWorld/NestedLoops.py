for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

numbers = [5, 2, 5, 2, 2]

# easy way; not a nested loop
for j in numbers:
    print('x' * j)

for i in numbers:
    output = ''
    for count in range(i):
        output += 'x'
    print(output)