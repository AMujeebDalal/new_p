#HANGMAN_BY_AMUJEEB
import random 
from words import word_list
from hangman_art import logo, stages
from replit import clear

print(logo)

word = random.choice(word_list)
display = []
lives = len(stages) - 1
end_of_game = False
hangman = stages[6]

for i in word:
  display.append('_')
print(display)

while not end_of_game:
  guess = input("Guess a letter\n").lower()
  clear()
  x= -1
  test = display.copy()
  for i in word:
    x+=1
    if guess == i:
      display[x] = guess
  if test == display:
    repeat = 0
    for i in display:
      if guess == i:
         repeat = 1
    if repeat == 1:
      print("You have already entered this letter.")
    else:
      print("You have entered wrong letter, it's not in the word.")
      lives -=1
      
  hangman = stages[lives]
  print(display," ", hangman)

  if '_' not in display:
    end_of_game = True
    print("You win!")
  elif lives == 0:
    end_of_game = True
    print("You lose!")
