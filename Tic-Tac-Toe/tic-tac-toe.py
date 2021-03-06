# import modules
from termcolor import colored


def tic_tac_toe():
    # creating the game board
    board = [" _ ", " _ ", " _ ",
             " _ ", " _ ", " _ ",
             " _ ", " _ ", " _ ", ]

    def display_board():
        print(board[0] + " | " + board[1] + " | " + board[2])
        print(board[3] + " | " + board[4] + " | " + board[5])
        print(board[6] + " | " + board[7] + " | " + board[8])

    # first print
    display_board()
    print("The game starts with 'X'")

    # entry of positions 'X' and 'O'
    def input_position_X():
        position = int(input("Choose a position from 1 to 9: ")) - 1
        if board[position] == " _ ":
            board[position] = " X "
            display_board()
            return True
        else:
            print("The position is busy!")
            print("Try again")
            input_position_X()

    def input_position_O():
        position = int(input("Choose a position from 1 to 9: ")) - 1
        if board[position] == " _ ":
            board[position] = " O "
            display_board()
            return True
        else:
            print("The position is busy!")
            print("Try again")
            input_position_O()

    # determine the winners
    def winner_X():
        if (board[0] == board[1] == board[2] == " X " or
                board[0] == board[3] == board[6] == " X " or
                board[0] == board[4] == board[8] == " X " or
                board[1] == board[4] == board[7] == " X " or
                board[2] == board[5] == board[8] == " X " or
                board[3] == board[4] == board[5] == " X " or
                board[2] == board[4] == board[6] == " X " or
                board[6] == board[7] == board[8] == " X "):
            return True

    def winner_O():
        if (board[0] == board[1] == board[2] == " O " or
                board[0] == board[3] == board[6] == " O " or
                board[0] == board[4] == board[8] == " O " or
                board[1] == board[4] == board[7] == " O " or
                board[2] == board[5] == board[8] == " O " or
                board[3] == board[4] == board[5] == " O " or
                board[2] == board[4] == board[6] == " O " or
                board[6] == board[7] == board[8] == " O "):
            return True

    # start the game
    i = 0
    while i < 10:
        if i % 2 == 0:
            if input_position_X() == True:
                if winner_X() == True:
                    print(colored("Player X win!", 'blue'))
                    question = input(colored("Do you want play again? (y/n): ", "green"))
                    if question == 'y' or question == 'yes':
                        tic_tac_toe()
                    else:
                        exit()
                    break
                else:
                    i += 1
        elif i % 2 == 1:
            if input_position_O() == True:
                if winner_O() == True:
                    print(colored("Player O win!", 'yellow'))
                    question = input(colored("Do you want play again? (y/n): ", "green"))
                    if question == 'y' or question == 'yes':
                        tic_tac_toe()
                    else:
                        exit()
                    break
                else:
                    i += 1


tic_tac_toe()