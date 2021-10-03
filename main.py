from random import randint

game_board = [[' ',' ',' '],
              [' ',' ',' '],
              [' ',' ',' ']]
winner = None
piece_placed = []


def print_board(board):
    display = ''
    for i in range(0, len(board)):
     for j in range(0, len(board[0])):
         if j < 2:
             display += board[i][j]+'|'
         else:
             display += board[i][j]
     if i < 2:
         display += '\n-+-+-\n'
    print(display)

def place_piece(board, location, player):
    if player == 'user':
        piece = 'X'
    else:
        piece = 'O'

    if location == 1:
        board[0][0] = piece
    elif location == 2:
        board[0][1] = piece
    elif location == 3:
        board[0][2] = piece
    elif location == 4:
        board[1][0] = piece
    elif location == 5:
        board[1][1] = piece
    elif location == 6:
        board[1][2] = piece
    elif location == 7:
        board[2][0] = piece
    elif location == 8:
        board[2][1] = piece
    elif location == 9:
        board[2][2] = piece

def check_winner(piece):
    if piece == 'X':
        return 'YOU'
    else:
        return 'CPU'

def check_win(board):
    row1 = board[0][0] == board[0][1] == board[0][2] != ' '
    row2 = board[1][0] == board[1][1] == board[1][2] != ' '
    row3 = board[2][0] == board[2][1] == board[2][2] != ' '

    col1 = board[0][0] == board[1][0] == board[2][0] != ' '
    col2 = board[0][1] == board[1][1] == board[2][1] != ' '
    col3 = board[0][2] == board[1][2] == board[2][2] != ' '

    dia1 = board[0][0] == board[1][1] == board[2][2] != ' '
    dia2 = board[0][2] == board[1][1] == board[2][0] != ' '

    global winner
    if row1:
        winner = check_winner(board[0][0])
        return True
    if row2:
        winner = check_winner(board[1][0])
        return True
    if row3:
        winner = check_winner(board[2][0])
        return True

    if col1:
        winner = check_winner(board[0][0])
        return True
    if col2:
        winner = check_winner(board[0][1])
        return True
    if col3:
        winner = check_winner(board[0][2])
        return True

    if dia1:
        winner = check_winner(board[0][0])
        return True
    if dia2:
        winner = check_winner(board[0][2])
        return True
    return False

print_board(game_board)
while True:
    user_choice = None

    try:
        user_choice = int(input("Choose where to place? (1-9): "))
        if user_choice < 0 or user_choice > 9 or user_choice in piece_placed:
            raise Exception()
    except Exception as e:
        print("Invalid input")
        continue

    place_piece(game_board, user_choice, 'user')
    piece_placed.append(user_choice)
    print_board(game_board)
    if check_win(game_board):
        print(winner, "WON!")
        break

    cpu_choice = randint(1, 9)
    while cpu_choice in piece_placed:
        cpu_choice = randint(1, 9)
    place_piece(game_board, cpu_choice, 'cpu')
    piece_placed.append(cpu_choice)
    print("CPU has placed:")
    print_board(game_board)
    if check_win(game_board):
        print(winner, "WON!!")
        break
