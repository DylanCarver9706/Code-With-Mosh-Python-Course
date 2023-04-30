names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names)
print(names[2])
print(names[2:-1])
names[0] = 'Jon'
print(names)

numbers = [15, 3, 89, 20, 18]
max = 0
for i in numbers:
    if i > max:
        # print(i)
        max = i
print(max)