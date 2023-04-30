for item in 'Python':
    print(item)

for item in ['John', 'Mosh', 'Sarah']: # List
    print(item)

for item in range(10): # Will print numbers 1-9. Range is an object
    print(item)

for item in range(5, 10): # Will print numbers 5-9
    print(item)

for item in range(5, 10, 2): # Adding step. Will print numbers 5,7,9
    print(item)

prices = [10, 20, 30]
total = 0

for item in prices:
    total += item
print(f"Total: {total}") # Need to put this outside of the for loop so it doesnt total after each pass


