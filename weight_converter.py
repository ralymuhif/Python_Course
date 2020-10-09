weight = int(input ("Weight: "))
unit_mesure = input ("(L)bs or (K)g: ")

if (unit_mesure.lower() == "l"):
   print(f"You are {weight * 0.45} Kilos")
elif (unit_mesure.lower() == "k"):
   print(f"You are {weight / 0.45} Pounds")