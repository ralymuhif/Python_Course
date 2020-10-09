is_hot = True
is_cold = False

if (is_hot):
   print("It's a hot day. Please drink water!")
elif (is_cold):
   print("It's a cold day. Please wear warm clothes")
else:
   print("It's a lovely day.")

# Exercise
price_house = 1000000
has_good_credit = False
down_deposit = 0

if (has_good_credit):
   down_deposit = price_house*10/100
else:
   down_deposit = price_house*20/100
print(f"The down deposit is : ${down_deposit}")
