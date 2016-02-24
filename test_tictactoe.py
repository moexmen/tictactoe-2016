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
    def test_humans_move(self):
        game = ""
        expected = ""

        # patch the input function to always return '2'
        with patch.object(tictactoe, "input", create=True,
                            return_value='2'):
            self.assertEqual(humans_move(game), expected)

    def test_computers_move(self):
        self.assertEqual(computer_move("EOEXXEEEE"),"OOEXXEEEE")
	
    def test_computer_move_1(self): 
        self.assertEqual(computer_move("XOOEXXEXE"),"XOOOXXEXE")

    def test_computer_move_2(self):
        self.assertEqual(computer_move("XOOXXXOXE"),"XOOXXXOXO")

    def test_check_winner(self):
        self.fail("not implemented")

if __name__ == '__main__':
    unittest.main()
