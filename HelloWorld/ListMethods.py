numbers = [5,2,1,7,5,4]
print(numbers)
numbers.append(20) # add to end
print(numbers)
numbers.insert(0, 10) # 1: which index to add to, 2: value to add
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(numbers.count(5))
numbers.remove(5) # removes first instance of that value
print(numbers)
numbers.remove(5)
print(numbers)
numbers.pop() # remove from the end
print(numbers)

numbers.clear() # deletes all values in list
print(numbers)

print('Remove duplicates')
numbers = [5,2,1,7, 2,5,4, 1]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

