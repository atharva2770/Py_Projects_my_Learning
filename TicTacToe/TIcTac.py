#Step 1: Write a function that can print out a board. Set up your board as a list,
# where each index 1-9 corresponds with a number on a number pad,
# so you get a 3 by 3 board representation.

def display_board(board):

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)

def player_input():

    marker = ''

    #Keep asking player 1 to choose X or O
    while marker != 'X' and marker != 'O':
        marker = input("Player 1, choose X or O: ").upper()
    #Assign Player 2, the opposite marker
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1,player2)

player1, player2 = player_input()
# print(player_input())
def place_marker(board, marker, position):
    board[position] = marker

# place_marker(test_board,'$',8)
# display_board(test_board)

def win_check(board,mark):
    #Win tic tac toe?
    #All Rows All Columns and 2 diagonals check

    return((board[1] == mark and board[2] == mark and board[3] == mark)or #column
    (board[4] == mark and board[5] == mark and board[6] == mark)or #column
    (board[7] == mark and board[8] == mark and board[9] == mark)or #column
    (board[1] == mark and board[5] == mark and board[9] == mark)or #diagonal
    (board[3] == mark and board[5] == mark and board[7] == mark)or #diagonal
    (board[1] == mark and board[4] == mark and board[7] == mark)or #row
    (board[2] == mark and board[5] == mark and board[8] == mark)or #row
    (board[3] == mark and board[6] == mark and board[9] == mark)) #row

# display_board(test_board)
# print(win_check(test_board,'X'))

import random

def choose_first():
    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):

    return board[position] == ' '

def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False  #Board is not full if it is False
    #Board is full if we return True
    return True

def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9) '))

    return position

def replay():
    choice = input("Play again? Enter Yes or No ").upper()
    return choice == 'Yes'  ##if input is Yes then only replay

### Main Logic

print("Welcome to Tic Tac Toe!")
#while loop to keep running the game
while True:
    #Play the Game

    ##Set up board
    the_board = [' ']*10
    player1, player2 = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input("Ready to Play? y or n ").lower()
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if turn == 'Player 1':

            display_board(the_board) #show the board

            position = player_choice(the_board) #choose position

            place_marker(the_board,player1,position)  #check the marker on the position

            if win_check(the_board,player1):
                display_board(the_board)
                print("PLAYER 1 HAS WON!!!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!!")
                    game_on = False
                else:
                    turn = "Player 2"
        else:

            display_board(the_board)  # show the board

            position = player_choice(the_board)

            place_marker(the_board, player2, position)

            if win_check(the_board, player2):
                display_board(the_board)
                print("PLAYER 2 HAS WON!!!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!!")
                    game_on = False
                else:
                    turn = "Player 1"

    if not replay():
        break
    #Break Out of the While Loop on replay()