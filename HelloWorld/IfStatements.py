is_hot = False
is_cold = True

if is_hot: # if is_hot = True
    print("It's a hot day!")
    print("Drink plenty of water")
elif is_cold: # else if
    print("It's a cold day!")
    print("Wear warm clothes")
else:
    print("It's a lovely day!")
print("Enjoy your day!") # gets run regardless. Just another line


house_price = 1000000
good_credit_status = False

if good_credit_status:
    print(f'Your down payment will be ${int(house_price * .1)}')
else:
    print(f'Your down payment will be ${int(house_price * .2)}')