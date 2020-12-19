
LOGO = """ 
888    d8b          888                     888                    
888    Y8P          888                     888                    
888                 888                     888                    
888888 888  .d888 8b888888 8888b.   .d888 8b888888 .d88b.   .d88b.  
888    888 d88P"    888       "88b d88P"    888   d88""88b d8P  Y8b 
888    888 888      888   .d888888 888      888   888  888 88888888 
Y88b.  888 Y88b.    Y88b. 888  888 Y88b.    Y88b. Y88..88P Y8b.     
 "Y888 888  "Y8888P  "Y888"Y888888  "Y8888P  "Y888 "Y88P"   "Y8888  

"""

SOLUTION = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))


# Function to print Tic Tac Toe
def print_tic_tac_toe(grid):
    print("\tPositions from 1 to 9 from ---> upper row.\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(grid[0], grid[1], grid[2]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(grid[3], grid[4], grid[5]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(grid[6], grid[7], grid[8]))
    print("\t     |     |")
    print("\n")


# Function to print the score-board
def print_scoreboard(score):
    print("\t=================================")
    print("\t           SCOREBOARD            ")
    print("\t=================================")

    players = list(score.keys())
    print("\t   ", players[0], "\t    ", score[players[0]])
    print("\t   ", players[1], "\t    ", score[players[1]])

    print("\t==================================\n")


# Function for a single game of Tic-Tac-Toe
def play(symbol, player_info):
    # Represents the Tic Tac Toe
    grid = [' ' for x in range(9)]

    # Stores the positions of X and O
    player_pos = {'X': [], 'O': []}

    # Game Loop for a single game
    while True:
        print_tic_tac_toe(grid)

        # Try exception block for input
        try:
            print(f"{player_info[symbol]}'s turn. Which position for {symbol}? : ", end="")
            move = int(input())
        except ValueError:
            print("Wrong Input! Try Again")
            continue

        if move < 1 or move > 9:
            print("Wrong Input! Try Again")
            continue

        # Check if the box is already filled
        if grid[move - 1] != ' ':
            print("Position already filled! Try again.")
            continue

        # Updating grid
        grid[move - 1] = symbol

        # Updating player positions
        player_pos[symbol].append(move)

        # Checking result
        for i in SOLUTION:
            if all(j in player_pos[symbol] for j in i):
                print_tic_tac_toe(grid)
                return player_info[symbol]
        if len(player_pos['X']) + len(player_pos['O']) == 9:
            print_tic_tac_toe(grid)
            return None

        # Switch player moves
        if symbol == 'X':
            symbol = 'O'
        else:
            symbol = 'X'


if __name__ == "__main__":

    print(LOGO)
    print("\nPlayer 1")
    player1 = input("Enter your name : ")

    print("\nPlayer 2")
    player2 = input("Enter your name : ")
    print("\n")

    # Stores the players info
    current_player = player1
    player_choice = {'X': "", 'O': ""}

    # Stores the score
    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)

    # Game Loop
    while True:
        print("Turn to choose for", current_player)
        print("Enter X for X, O for O & Q to Quit")
        # Try exception block for input
        try:
            choice = input().upper()
        except ValueError:
            print("Wrong Input! Try Again\n")
            continue
        if choice == 'X':
            player_choice['X'] = current_player
            if current_player == player1:
                player_choice['O'] = player2
            else:
                player_choice['O'] = player1
        elif choice == 'O':
            player_choice['O'] = current_player
            if current_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1
        elif choice == 'Q':
            print("Final Scores")
            print_scoreboard(score_board)
            print("Bye Bye")
            break
        else:
            print("Wrong Input! Try Again\n")
            continue

        winner = play(choice, player_choice)

        if winner is not None:
            print(f"{winner} has won this game!\n")
            score_board[winner] = score_board[winner] + 1
        else:
            print("Game Drawn\n")

        print_scoreboard(score_board)

        # Switch player who plays first
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1
