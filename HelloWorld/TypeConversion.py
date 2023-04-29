# birth_year = input('Birth year: ') # output will be string. Will cause errors and needs to be converted
# age = 2023 - int(birth_year) # will convert to integer. also works for float(), bool(), etc.
# print(type(age)) # will dispaly the datatype of a variable
# print(age)

# exercise: Ask a user their weight (in pounds), convert it
# to kilograms and print on the terminal.

weight_lbs = int(input('Weight: '))
lbs_to_kg_conversion_rate = 0.453592
weight_kg = lbs_to_kg_conversion_rate * weight_lbs
print(weight_kg)