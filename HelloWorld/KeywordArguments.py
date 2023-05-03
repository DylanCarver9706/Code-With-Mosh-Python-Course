def greet_user(first_name, last_name): # function get defined all lowercase and with an underscore as a space
    # Parameter is same as name = John inside function
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')
# Add 2 line breaks after a function


print("Start")
greet_user("John", "Smith") # Parameters are positional arguments
greet_user(last_name="Smith", first_name="John") # Keyword argument
print("Finish")