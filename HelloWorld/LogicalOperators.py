has_high_income = True
has_good_credit = False
has_criminal_record = False

if has_high_income and not has_criminal_record: # and / or / not
    # not operator switches current booloean value to opposite
    print("Elidigable for loan!")

if has_high_income or has_good_credit:
    print("Elidigable for loan!")