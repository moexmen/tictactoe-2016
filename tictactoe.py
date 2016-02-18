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

def humans_move(game_board):
    """
    Displays the game board to the user, then
    gets the human player's move and executes it.
    """
    pass
