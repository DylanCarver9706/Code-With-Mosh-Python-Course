first = 'John'
last = 'Smith'
message = first + ' ' + ' [' + last + '] is a coder' # Not ideal for writing code
# John [Smith] is a coder
msg = f'{first} [{last}] is a coder' # Formatted string. Starts with f
print(msg)