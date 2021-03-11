# -*- coding: utf-8 -*-
"""

johnwoates
CPSC 223P-01
Thu Feb 18 13:14:07 2021
joates@fullerton.edu

"""

import random 
keepLooping = True
comp_wins = 0
user_wins = 0
draw = 0

#creating player's choices
def player_choices():
  userinput = input("Make your choice: (R, P, S, Q) > ")
  if userinput in ["Rock", "rock", "r", "R"]:
    userinput = "r"
  elif userinput in ["Paper", "paper", "p", "P"]:
    userinput = "p"
  elif userinput in ["scissors", "Scissors", "s", "S"]:
    userinput = "s"
  elif userinput in ["Quit", "quit", "q", "Q"]:
    userinput = "q"
  else:
    print("Invalid choices, try again")
    player_choices()

  return userinput

#creating computer's choice with random
def computer_choices():
  computer = random.choice(["r", "p", "s"])
  return computer

#checks to see who wins
def winner():
  if comp_wins > user_wins:
    print("Computer Wons!")
  elif comp_wins < user_wins:
    print("You Won!")
  else:
    print("You tied")

#runs loop and keeps going until player inputs q
while keepLooping:
  user_choice = player_choices()
  computer_choice = computer_choices()

  if user_choice == "r":
    if computer_choice == "r":
      print("Computer chose Rock. Call it a draw.")
      draw += 1
    elif computer_choice == "p":
      print("Computer chose Paper. Computer wins.")
      comp_wins += 1
    elif computer_choice == "s":
      print("Computer chose Scissors. You win.")
      user_wins += 1
  
  if user_choice == "p":
    if computer_choice == "r":
      print("Computer chose Rock. You win.")
      user_wins += 1
    elif computer_choice == "p":
      print("Computer chose Paper. Call it a draw.")
      draw += 1
    elif computer_choice == "s":
      print("Computer chose Scissors. Computer wins.")
      comp_wins += 1

  if user_choice == "s":
    if computer_choice == "r":
      print("Computer chose Rock. Computer wins.")
      comp_wins += 1
    elif computer_choice == "p":
      print("Computer chose Paper. You win.")
      user_wins += 1
    elif computer_choice == "s":
      print("Computer chose Scissors. Call it a draw.")
      draw += 1

  if user_choice == "q":
    break

#print result
print("Computer: %i" % comp_wins )
print("You: %i" % user_wins)
print("Ties: %i" % draw)
winner()
