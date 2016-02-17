import unittest

from tictactoe import *

class TestGameSetup(unittest.TestCase):
    def test_new_game(self):
        self.fail("not implemented")

    def test_get_starting_player(self):
        self.assertIsInstance(get_starting_player(), bool)

class TestGamePlay(unittest.TestCase):
    def test_humans_move(self):
        self.fail("not implemented")

    def test_computers_move(self):
        self.fail("not implemented")

    def test_check_winner(self):
        self.fail("not implemented")

if __name__ == '__main__':
    unittest.main()
