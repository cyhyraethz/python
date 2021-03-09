import random
import math

while True:
  player_choice = input('Rock (1), Paper (2), Scissors (3): ')
  if player_choice.lower() == 'quit' or player_choice.lower() == 'exit':
    break
  if player_choice != '1' and player_choice != '2' and player_choice != '3':
    print('Error: invalid number\n')
    continue
  choices = ['', 'Rock', 'Paper', 'Scissors']
  player_choice = int(player_choice)
  computer_choice = math.floor(random.random() * 3 + 1)
  print(f'Player: {choices[player_choice]}\nComputer: {choices[computer_choice]}')
  if player_choice == 1:
    if computer_choice == 1:
      print('Draw.\n')
      continue
    elif computer_choice == 2:
      print('Computer won.\n')
      continue
    else:
      print('Player won.\n')
      continue
  if player_choice == 2:
    if computer_choice == 2:
      print('Draw.\n')
      continue
    elif computer_choice == 3:
      print('Computer won.\n')
      continue
    else:
      print('Player won.\n')
      continue
  if player_choice == 3:
    if computer_choice == 3:
      print('Draw.\n')
      continue
    elif computer_choice == 1:
      print('Computer won.\n')
      continue
    else:
      print('Player won.\n')
      continue