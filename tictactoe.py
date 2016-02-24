def tictactoe():
    """
    Human plays a single Tic-Tac-Toe game against an AI
    """
    game = new_game()
    humans_turn = get_starting_player()
    game_result = None

    while game_result is None:
        if humans_turn:
            game = humans_move(game)
            humans_turn = False
            print_board(game)
        else:
            game = computers_move(game)
            print_board(game)
            humans_turn = True
        game_result = check_winner(game)
    print(game_result)

def new_game():
    """Returns a representation of an empty game grid"""
    return "EEEEEEEEE"

def humans_move(game_board):
    """
    Gets the human player's move and updates the board.
    """
    valid_move = False
    
    while valid_move == False:
        move = int(input("Enter a game board position (0 - 8) to make a move: "))
        if move < 0 or move > 8:
            print("Position out of range. Please try again.")
        elif game_board[move] != "E":
            print("Position not empty. Please try again.")
        else:
            front = game_board[:move]
            back = game_board[move+1:]
            front = front + "X"
            game_board = front + back
            valid_move = True

    return game_board

def computers_move(game_board):
    """Update the board with the computer player's move if an empty cell exists"""
    num=len(game_board)
    for i in range(num):
        if game_board[i]!='E':
            pass
        else:
           start=game_board[0:i]
           end=game_board[i+1:]
           game_board = start + "O" + end
           break
    return(game_board)

def check_winner(game_board):
    """
    Checks if there is a winner or if it is a draw.
    Returns one of the following strings when the game ends:
    - "Human Wins!" -- human player wins
    - "Computer Wins!" -- computer player wins
    - "Draw" -- the board is full and no one has won

    Returns None if there is no winner and moves are stil possible
    """
    pass

def get_starting_player():
    """
    Returns True if Human starts, False if computer starts.
    """
    pass

def print_board(boardplay):
    pretty_board = boardplay[:3] + "\n" + boardplay[3:6] + "\n" + boardplay[6:]
    return pretty_board

if __name__ == "__main__":
    tictactoe()
