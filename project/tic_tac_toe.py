###Create a Tic Tac Toe game. You are free to use any IDE you like
###2 players should be able to play the game (both sitting at the same computer)
###The board should be printed out every time a player makes a move
###You should be able to accept input of the player position and then place a symbol on the board

##Notes 
##if someone already replaces a value in the list it should not replace again

import sys

def game_on():
    """User input to play the Game to stop"""
    game = False
    while game == False:
        user_request = input("Enter 'Y' to start the game, 'N' to stop: ").upper()
        if user_request == 'Y':
            return True
        elif user_request == 'N':
            print("Thanks for Playing... Good Bye...")
            game = True
        else:
            print("Wrong choice! Select either Y or N")
            game = False

test_board = ['0','1','2','3','4','5','6','7','8','9']
def display_board(board):
    """Tic_Tac_Toe board to play, it will be displayed with numbers which user can select to replace the box in the board"""
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[7]+'|'+board[8]+'|'+board[9])

def player_1():
    """Player_1 input to select the specific box"""
    choice = 'Wrong'
    while choice.isdigit() == False:
        choice = input("Player_1 enter a number between 1 to 9: ")
        if choice.isdigit() == False:
            print("Enter the given number in the range 1 to 9: ")
    return int(choice)

def player_2():
    """Player_2 input to select the specific box"""
    choice = 'Wrong'
    while choice.isdigit() == False:
        choice = input("Player_2 enter a number between 1 to 9: ")
        if choice.isdigit() == False:
            print("Enter a given number in the range 1 to 9")
    return int(choice)

def update_user_input_player_1(test_board,position):
    """Player_1 input will be replaced with X """
    # replacement = input("If it's player 1 enter X, if it's player 2 enter O: ")
    test_board[position] = 'X'
    return test_board

def update_user_input_player_2(test_board,position):
    """Player_1 input will be replaced with Y """
    # replacement = input("If it's player 1 enter X, if it's player 2 enter O: ")
    test_board[position] = 'Y'
    return test_board

###Still don't know how to put a draw if the list still has numbers
def winner_announcement(test_board):
    """Winner will be analysed and established"""
    validate = True
    # print(validate)
    while validate == True:
        if ('X' in test_board[1] and 'X' in test_board[2] and 'X' in test_board[3]) or ('X' in test_board[4] and 'X' in test_board[5] and 'X' in test_board[6]) or ('X' in test_board[7] and 'X' in test_board[8] and 'X' in test_board[9]) or ('X' in test_board[1] and 'X' in test_board[5] and 'X' in test_board[9]) or ('X' in test_board[3] and 'X' in test_board[5] and 'X' in test_board[7]):
            print("Player 1 is the winner")
            sys.exit()
        elif ('Y' in test_board[1] and 'Y' in test_board[2] and 'Y' in test_board[3]) or ('Y' in test_board[4] and 'Y' in test_board[5] and 'Y' in test_board[6]) or ('Y' in test_board[7] and 'Y' in test_board[8] and 'Y' in test_board[9]) or ('Y' in test_board[1] and 'Y' in test_board[5] and 'Y' in test_board[9]) or ('Y' in test_board[3] and 'Y' in test_board[5] and 'Y' in test_board[7]):
            print("Player 2 is the winner")
            sys.exit()
        else:
            print("Game Draw")
            validate = False
        
###Function call
play = game_on()
while play == True:
    display_board(test_board)
    player__1_result = player_1()
    update_user_input_player_1(test_board,player__1_result)
    winner_announcement(test_board)
    display_board(test_board)
    player_2_result = player_2()
    update_user_input_player_2(test_board,player_2_result)
    winner_announcement(test_board)