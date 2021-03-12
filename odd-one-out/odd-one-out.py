from assets import *
import random

categories = {
  'shape': [],
  'filled': [],
  'circled': []
}

bool = random.choice([True, False])
odd = random.choice(list(categories))

for key, value in categories.items():
  if key == odd:
    categories[key].append(bool)
    for i in range(3):
      categories[key].append(not bool)
  else:
    for i in range(2):
      categories[key].append(bool)
      categories[key].append(not bool)

class Icon:
  def __init__(self, shape, filled, circled, unique):
    index = 0
    if circled == True:
      self.circled = 'Circled'
    else:
      self.circled = ''
      index += 1
    if filled == True:
      self.filled = 'Filled'
      index += 2
    else:
      self.filled = 'Empty'
    if shape == False:
      self.shape = 'Triangle'
      self.icon = triangle[index]
    else:
      self.shape = 'Square'
      self.icon = square[index]
    self.unique = unique
  def __repr__(self):
    return self.icon

icons = [0, 1, 2, 3]
length = 4

for i in range(len(icons)):
  unique = False

  index = int(random.random() * length)
  shape = categories['shape'][index]
  del categories['shape'][index]

  index = int(random.random() * length)
  filled = categories['filled'][index]
  del categories['filled'][index]

  index = int(random.random() * length)
  circled = categories['circled'][index]
  del categories['circled'][index]

  if odd == 'shape' and shape == bool:
    unique = True
  elif odd == 'filled' and filled == bool:
    unique = True
  elif odd == 'circled' and circled == bool:
    unique = True

  icons[i] = Icon(shape, filled, circled, unique)
  length -= 1


guess = 0
count = 0

while guess < 1 or guess > 4:
  if count > 0:
    print('Error: please enter a valid number between 1 and 4')
  lines = [icons[i].icon.splitlines() for i in range(4)]
  for l in zip(*lines):
    print(''.join(l))
  print('\n' + ' '*14 + '(1)' + ' '*26 + '(2)' + ' '*26 + '(3)' + ' '*26 + '(4)')
  try:
    guess = int(input('\nYour guess: '))
  except:
    pass
  finally:
    count += 1

if icons[guess - 1].unique:
  print('You win!')
else:
  print('You lose!')