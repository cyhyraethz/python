import random

board = []
word_list = []
wrong_words = []
wrong_letters = []
guesses_remaining = 6

for word in open('words.txt', 'r'):
  word_list.append(word.rstrip())

word = random.choice(word_list).upper()

for i in word:
  board += '_'

def display_status():
  print()
  if wrong_words:
    print('Incorrect words: ' + ', '.join(wrong_words) + '\n')
  if wrong_letters:
    print('Incorrect letters: ' + ', '.join(wrong_letters) + '\n')
  print('Guesses remaining: ' + str(guesses_remaining) + '\n')
  print(f'Word ({len(word)} letters): ', ' '.join(board) + '\n'*3)

display_status()

while '_' in board and guesses_remaining > 0:
  guess = input('Your guess: ').upper()
  if len(guess) < 1:
    continue
  if len(guess) == len(word):
    if guess == word:
      for i in range(len(word)):
        board[i] = word[i]
      print(f'Word ({len(word)} letters): ', ' '.join(board) + '\n'*3)
      break
  elif len(guess) > 1:
    print('Error: guess contains multiple letters' + '\n' * 2)
    display_status()
    continue
  if not guess.isalpha():
    print('Error: not a valid letter' + '\n' * 2)
    display_status()
    continue
  if guess in wrong_letters:
    print(f'You already guessed {guess}. Please choose a different letter.' + '\n' * 2)
    display_status()
    continue
  if guess in word:
    for i in range(len(word)):
      if (word[i] == guess):
        board[i] = guess
  else:
    if len(guess) == 1:
      wrong_letters.append(guess)
    else:
      wrong_words.append(guess)
    guesses_remaining -= 1
  display_status()

if '_' not in board:
  print(f'You win! The word was \'{word.capitalize()}\'\n')
else:
  print(f'You lost! The word was \'{word.capitalize()}\'\n')