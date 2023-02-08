# this code generates a "choose your own adventure" story
# getting familiar with if/elif/else in python syntax


print("THE PRIZE\n")
print("A choose your own adventure story.")
input("Press any key to begin...")

choice1 = input("\nYou won a contest!\nYou can either choose to receive a misterious prize that is sent to your house by mail, or go participate in a TV show where you get to choose a door and receive a prize.\n\nDo you choose MAIL or DOORS?\n\n").lower()
if choice1 == 'mail':
  print("\nThe TV show host wasn't happy that you didn't want to meet him. He sent you a pair of socks, so you can stay comfortable at home.")
elif choice1 == 'doors':
  choice2 = input("\nYou need to travel to the TV show studio.\nIt's a 1 hour flight or 8 hours drive, and they can either send you a plane ticket or a fancy motorhome with a driver.\n\nDo you choose to travel by AIR or by ROAD?\n\n").lower()
  if choice2 == 'air':
    print("\nUnlucky you! The plane crashed.")
  elif choice2 == 'road':
    choice3 = input("\nYou enjoyed your road trip and got to your destination one day before the show.\nThis gives you time to explore the city, but you can also eat dinner at the hotel and rest a bit.\n\nDo you go for REST our TOUR?\n\n").lower()
    if choice3 == 'rest':
      print("\nEveryone who ate at the hotel's restaurant that evening got food poisoning.\n\nThe show was cancelled and you were sent back home with a 'Get Well Soon' ballon for a prize.")         
    elif choice3 == 'tour':
      choice4 = input("\nA local adverts you that this is a dangerous city, and offers to take you to a safe, hidden gem.\n\nDo you go with the LOCAL or continue your tour ALONE?\n\n").lower()
      if choice4 == 'alone':
        print("\nYou got lost in the city. You ended up where you shouldn't be.\n\nNow you just can't stop thinking that maybe you should've gone with the local. Too late.") 
      elif choice4 == 'local':
        choice5 = input("\nYou had such a great time!\nBut today is another day. Now you are in the studio with three doors in front of you.\n\nWhich door do you choose: 1, 2 or 3?\n\n")
        if choice5 == "1":
          print("\nYou won a box with 100 colored pencils!")
        elif choice5 == "2":
          print("\nYou won $1,000,000!")
        elif choice5 == "3":
          print("\nYou won a handmade ugly christimas sweater!")
        else:
          print("\nFor choosing an option that is not valid, the host opened a backdoor and now there's a tiger chasing you.\nGood luck!")
      else:
       print("\nInvalid option. Game Over.")
    else:
      print("\nInvalid option. Game Over.")
  else:
    print("\nInvalid option. Game Over.")
else:
  print("\nInvalid option. Game Over.")