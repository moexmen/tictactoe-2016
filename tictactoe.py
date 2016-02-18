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
    Gets the human player's move and executes it.
    """
    pass

def computers_move(game_board):
    """Executes the computers player's move if empty cell exists"""
    pass

def check_winner(game_board):
    """
    Checks if there is a winner or if it is a draw.
    Returns one of the following strings as appropriate:
    - "Human Wins!"
    - "Computer Wins!"
    - "Draw"
    """
    pass

# TODO: add missing stub

