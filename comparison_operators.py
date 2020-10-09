temperature = 35

if (temperature > 30):
   print("It's a hot day!")
elif (temperature < 10):
   print("It's a cold day!")
else:
   print("It's neither hot nor cold!")


# Exercise

name = "Ralph"
print(len(name))

if (len(name) < 3):
   print("Name must be at least 3 characters long!")
elif (len(name) > 50):
   print("Name can be a maximum of 50 characters!")
else:
   print("Name looks good!")