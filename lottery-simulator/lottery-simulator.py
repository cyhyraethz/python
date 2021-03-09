import random

player_numbers_chosen = 0
player_numbers = []
draws = []

while player_numbers_chosen < 6:
  try:
    chosen_number = int(input(f'Number #{player_numbers_chosen + 1}: '))
  except ValueError:
    print('Please choose a number between 1 and 49')
    continue
  if chosen_number < 1 or chosen_number > 49:
    print('Please choose a number between 1 and 49')
    continue
  if chosen_number in player_numbers:
    print(f'You have already picked {chosen_number} as one of your choices.\nPlease pick a different number for your next choice.')
    continue
  player_numbers.append(chosen_number)
  player_numbers_chosen += 1

print(f'Your numbers: {player_numbers}')

draws_generated = 0

while draws_generated < 3:
  draw = []
  winning_numbers_generated = 0
  while winning_numbers_generated < 6:
    winning_number = random.choice(range(1, 50))
    if winning_number not in draw:
      draw.append(winning_number)
      winning_numbers_generated += 1
  draws.append(draw)
  draws_generated += 1

for i in range(3):
  matching_numbers = []
  result = 'You did not win this time!'
  for j in player_numbers:
    if j in draws[i]:
      matching_numbers.append(j)
  if len(matching_numbers) > 1:
    result = f'You won! Matching numbers: {matching_numbers}'
  print(f'Draw {i + 1} - winning numbers: {draws[i]} - {result}')