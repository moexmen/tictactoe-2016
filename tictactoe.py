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
        else:
            game = computers_move(game)
            humans_turn = True
        game_result = check_winner(game)
    print(game_result)

def new_game():
    """Returns a representation of an empty game grid"""
    pass

def humans_move(game_board):
    """
    Gets the human player's move and updates the board.
    """
    pass

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
