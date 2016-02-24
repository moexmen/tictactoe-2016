import unittest
from unittest.mock import patch

import tictactoe
from tictactoe import *

class TestGameSetup(unittest.TestCase):
    def test_new_game(self):
        self.assertEqual(new_game(),"EEEEEEEEE")

    def test_get_starting_player(self):
        self.assertIsInstance(get_starting_player(), bool)

class TestGamePlay(unittest.TestCase):
    def test_humans_move_01(self):
        game = "EEEEEEEEE"
        expected = "EEXEEEEEE"

        # patch the input function to always return '2'
        with patch.object(tictactoe, "input", create=True,
                            return_value='2'):
            self.assertEqual(humans_move(game), expected)

    def test_humans_move_02(self):
        game = "EEEEEEEEE"
        expected = "EEEEEEEXE"

        # patch the input function to always return '7'
        with patch.object(tictactoe, "input", create=True, return_value='7'):
            self.assertEqual(humans_move(game), expected)

    def test_computers_move(self):
        self.assertEqual(computers_move("EOEXXEEEE"),"OOEXXEEEE")
    
    def test_computer_move_1(self): 
        self.assertEqual(computers_move("XOOEXXEXE"),"XOOOXXEXE")

    def test_computer_move_2(self):
        self.assertEqual(computers_move("XOOXXXOXE"),"XOOXXXOXO")

    def test_human_wins(self):
        self.assertEqual(check_winner('XXXEOEEOO'), 'Human Wins!')  

    def test_computer_wins(self):
        self.assertEqual(check_winner('EEOXEOXXO'), 'Computer Wins!')

    def test_draw(self):    
        self.assertEqual(check_winner('XOXOXOOXO'), 'Draw!')

    def test_none(self):    
        self.assertEqual(check_winner('EEEEEOXEX'), None)       

    def test_print_1(self):
        game = "EEEEEEEEE"
        self.assertEqual(print_board(game),"EEE\nEEE\nEEE")

    def test_print_2(self):
        game = "EXEEOEXEE"
        self.assertEqual(print_board(game),"EXE\nEOE\nXEE")

if __name__ == '__main__':
    unittest.main()
