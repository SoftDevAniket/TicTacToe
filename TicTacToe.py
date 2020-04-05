import random


def display_board(board):
    print('\n'*100)
    print(" "+ board[7] + "|" + board[8] + "|" + board[9])
    print("---" + "--" + "--")
    print(" " + board[4] + "|" + board[5] + "|" + board[6])
    print("---" + "--" + "--")
    print(" "+ board[1] + "|" + board[2] + "|" + board[3])


def player_input():
    marker = ""
    while ( marker != "X" and marker!= "O"):
        marker = input("Player1:Please pick a marker 'X' or 'O':")
    
    player1 = marker
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    return (player1,player2)


def place_marker(board, marker, position):
    board[position] = marker

   
def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:
        return True
    elif board[4] == board[5] == board[6] == mark:
        return True
    elif board[7] == board[8] == board[9] == mark:
        return True
    elif board[1] == board[4] == board[7] == mark:
        return True
    elif board[2] == board[5] == board[8] == mark:
        return True
    elif board[3] == board[6] == board[9] == mark:
        return True
    elif board[1] == board[5] == board[9] == mark:
        return True
    elif board[7] == board[5] == board[3] == mark:
        return True
    else:
        return False


def choose_first():
    p = random.randint(1,2)
    return "Player1"


def space_check(board, position):
    if board[position] == " ":
        return True
    else:
        return False
    

def game_on():
    c = input("Are you ready to play,Enter Yes or No:")
    if c == "Yes":
        return True
    else:
        return False


def full_board_check(board):
    for i in board:
        if i == " ":
            return False
        else:
            return True


def player_choice(board):
    PlayerChoice = int(input("Enter the postion choice(1-9):"))
    while PlayerChoice in range(1,10):
        if space_check(board,PlayerChoice) == True:
            return PlayerChoice
    
        
def replay():
        PlayAgain = input("Do you want to Play Again[Yes or No]:")
        if PlayAgain == "Yes":
            return True
        else:
            return False


print('Welcome to Tic Tac Toe!')

while True:
    test_board = [" "]*10
    player1,player2 = player_input()
    First = choose_first()
    print("{} will go first".format(First))
    BoolValue = game_on()
    while BoolValue == True:
            print("Player 1:")
            p1 = player_choice(test_board)
            if full_board_check(test_board) == False:
                place_marker(test_board, player1, p1)
                display_board(test_board)
                if win_check(test_board, player1) == True:
                    print("Player1 won the Game")
                    break
            print("Player 2:")
            p2 = player_choice(test_board)
            if full_board_check(test_board) == False:
                place_marker(test_board, player2, p2)
                display_board(test_board)
                if win_check(test_board, player2) == True:
                    print("Player2 won the Game")
                    break
    if not replay():
       	break