import random
import math

print('I\'m thinking of a number between 1 and 10...')
num = math.floor(random.random() * 10 + 1)

while True:
  guess = int(input('Your guess: '))
  if guess < num:
    print('too small')
  elif guess > num:
    print('too big')
  else:
    print('you won!')
    break