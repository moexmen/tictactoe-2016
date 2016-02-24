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
    pass

def check_winner(game_board):
    """
    Checks if there is a winner or if it is a draw.
    Returns one of the following strings when the game ends:
    - "Human Wins!" -- human player wins
    - "Computer Wins!" -- computer player wins
    - "Draw" -- the board is full and no one has won

    Returns None if there is no winner and moves are stil possible
    """
    def check_winner(game_board):
        
    s=game_board	
    if s[:3]=='XXX' or s[3:6]=='XXX' or s[6:9]=='XXX' or s[::3]=='XXX' or s[1::3]=='XXX' or s[2::3]=='XXX' or s[::4]=='XXX' or s[2:8:2]=='XXX':
        return "Human Wins!"
    elif s[:3]=='OOO' or s[3:6]=='OOO' or s[6:9]=='OOO' or s[::3]=='OOO' or s[1::3]=='OOO' or s[2::3]=='OOO' or s[::4]=='OOO' or s[2:8:2]=='OOO':
        return "Computer Wins!"
    elif s[0::]=='E' or s[1::]=='E' or s[2::]=='E' or s[3::]=='E' or s[4::]=='E' or s[5::]=='E' or s[6::]=='E' or s[7::]=='E' or s[8::]=='E':
        return None
    else:
        return "Draw!"

