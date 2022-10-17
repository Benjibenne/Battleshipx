import random




""" introduction funtion which introduce """
def introduction():
    print("--------------------------------------------------------------------------------------")
    print("                           Hello and welcome to Battleshipx!")
    print("--------------------------------------------------------------------------------------")
    print(" This is my first attempt in making this type of game hopes it works and is enjoyable.")
    print("--------------------------------------------------------------------------------------")
    print("")
    print("")
    print("                            Press ENTER to start the game")
    print(input(""))


""" empty boarder funtion """
def create_board():
    board = [
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
    ]

    letters_to_numbers = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
    }

    # We want 5 battleships, so we use a for loop to ask for a ship 5 times!
    for n in range(4):
        print("Where do you want ship ", n + 1, "?")
        column = input("column (a to d):")
        if column not in "abcd":
            print("That column is wrong! It should be a, b, c, or d")
        row = input("row (1 to 4):")
        if row not in "1234":
            print("That row is wrong! it should be 1, 2, 3, or 4")  
        # columns are letters, so here we use the dictionary to get the number corresponding to the
        # letter
        column_number = letters_to_numbers[column]
        # The player enters numbers from 1 to 4, but we have to substract 1 to use python lists that
        # start on zero.
        row_number = int(row) - 1
    # Check that there are no repeats
    if board[row_number][column_number] == 'X':
        print("That spot already has a battleship in it!")
        board[row_number][column_number] = 'X'

        # Show the board, one row at a time
        for row in board:
            print(row)  

""" main funtion to call up the funtion made """
def start_game():
    introduction()
    create_board()


start_game()