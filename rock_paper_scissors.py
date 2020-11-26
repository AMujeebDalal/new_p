rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

user_choice = int(input("What do you want to choose? 0 for Rock, 1 for paper and 2 for scissors "))

if user_choice == 0:
  print("You chose "+ rock)
elif user_choice == 1:
  print("You chose "+ paper)
elif user_choice == 2: 
  print("You chose "+ scissors)

r = random.randint(0,2)

if r == 0:
  print("Computer chose "+ rock)
elif r == 1:
  print("Computer chose "+ paper)
elif r == 2:
  print("Computer chose "+ scissors)

if user_choice == 0 and r == 2:
  print("You Won!")
elif user_choice == 0 and r == 1:
  print("You lost!")
elif user_choice == 1 and r == 0:
  print("You Won!")
elif user_choice == 1 and r == 2:
  print("You lost!")
elif user_choice == 2 and r == 1:
  print("You Won!")
elif user_choice == 2 and r == 0:
  print("You lost!")
else:
  print("Draw!")  
