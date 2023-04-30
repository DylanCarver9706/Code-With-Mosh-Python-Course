weight = int(input("Weight: ")) # input is a string type, so must be converted
lbs_or_kgs = input("(L)bs or (K)gs: ")
lbs_to_kg_conversion_rate = 0.453592
kgs_to_lbs_conversion_rate = 2.20462

if lbs_or_kgs.upper() == 'L':
    print(f"You are {weight * lbs_to_kg_conversion_rate} kilograms")
elif lbs_or_kgs.upper() == 'K':
    print(f"You are {weight * kgs_to_lbs_conversion_rate} pounds")
else:
    print("Please enter 'L' for pounds, or 'K' for kilograms" )
