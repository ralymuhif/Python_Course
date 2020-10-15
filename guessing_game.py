secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
   guess_number = int (input("Guess: "))
   guess_count += 1
   if guess_number == secret_number:
      print("You got it! It is " + secret_number)
      break
else:
   print("Sorry you failed!")

      
