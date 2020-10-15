command = ""
started = False
while True:
   command = input("> ").lower()
   if command == "start":
      if started == True:
         print("The car already started!")
      else:
         print("Car started... Ready to go!")
         started = True
   elif command == "stop":
      if started == False:
         print("The car already stopped!")
      else:
         print("Car stopped!")
         started = False
   elif command == "help":
      print("""
start - to start the car
stop - to stop the car
quit - to quit the game
""")
   elif command == "quit":
      break
   else:
      print("I don't understand that!")   
