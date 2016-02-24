import unittest
from unittest.mock import patch

import tictactoe
from tictactoe import *

class TestGameSetup(unittest.TestCase):
    def test_new_game(self):
        self.fail("not implemented")

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
        self.assertEqual(computer_move("EOEXXEEEE"),"OOEXXEEEE")
	
    def test_computer_move_1(self): 
        self.assertEqual(computer_move("XOOEXXEXE"),"XOOOXXEXE")

    def test_computer_move_2(self):
        self.assertEqual(computer_move("XOOXXXOXE"),"XOOXXXOXO")

    def test_check_winner(self):
        self.fail("not implemented")

    def test_print_1(self):
        game = "EEEEEEEEE"
        self.assertEqual(print_board(game),"EEE\nEEE\nEEE")

    def test_print_2(self):
	game = "EXEEOEXEE"
	self.assertEqual(print_board(game),"EXE\nEOE\nXEE")
