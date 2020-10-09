has_high_income = True
has_good_credit = True
has_criminal_record = False

# if (has_high_income or has_good_credit):
#    print (" The buyer is eligible for a loan cause they qualify for at least one  conditions!!")

# if (has_high_income and has_good_credit):
#    print (" The buyer is eligible for a loan cause they qualify for both conditions!")

if (has_good_credit and not has_criminal_record):
   print (" The buyer is eligible for a loan cause they qualify for both conditions!")