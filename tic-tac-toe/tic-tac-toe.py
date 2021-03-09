board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
turn = 0

def check_win(board):
  for i in range(3):
    if board[i][0] != '-' and board[i][0] == board[i][1] and board[i][1] == board[i][2]:
      print(f'{board[i][0]} wins!')
      return True
    for j in range(3):
      if board[0][j] != '-' and board[0][j] == board[1][j] and board[1][j] == board[2][j]:
        print(f'{board[0][j]} wins!')
        return True
  if board[1][1] != '-':
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
      print(f'{board[1][1]} wins!')
      return True
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
      print(f'{board[1][1]} wins!')
      return True
  return False

def display(board):
  rows = ''
  for i in board:
    rows += ' '.join(i) + '\n'
  print(rows)

def play(board, player):
  row = 0
  while row < 1 or row > 3:
    try:
      row = int(input('row: '))
    except ValueError:
      print('Please enter a number between 1 and 3')
  col = 0
  while col < 1 or col > 3:
    try:
      col = int(input('column: '))
    except ValueError:
      print('Please enter a number between 1 and 3')
  if board[row - 1][col - 1] == '-':
    board[row - 1][col - 1] = player
  else:
    print('Error: please select an empty square')
    play(board, player)

while not check_win(board):
  player = ''
  if turn % 2 == 0:
    print('X\'s turn')
    player = 'X'
  else:
    print('O\'s turn')
    player = 'O'
  play(board, player)
  display(board)
  turn += 1