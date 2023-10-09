chose1 = input('You\'re at a cross road. Where do yo go? "left" or "right". \n')

if chose1 == "left" or chose1 == "Left":
    chose2 = input('You came to lake. There is an island in the middle of lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n')
    if chose2 == "wait" or chose2 == "Wait":
      chose3 = input('You arrive at the island unharmed. There is house with 3 doors. One "red", one "yellow" and one "blue". Which color do you choose? \n')
      if chose3 == "red" or chose3 == "Red":
        print("Burned by fire. Game Over.")
      elif chose3 == "blue" or chose3 == "Blue":
        print("Easten bu beasts. Game Over.")
      elif chose3 == "yellow" or chose3 == "Yellow":
        print("You Win!")
      else:
        print("Game Over")     
    else:
      print("Game over")
else:
  print("Game Over")