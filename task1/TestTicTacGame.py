import unittest
from TicTacGame import TicTacGame


class TestTicTacGame(unittest.TestCase):
    def setUp(self):
        self.tic_tac = TicTacGame()

    def test_show_board(self):
        self.assertEqual(self.tic_tac.validate_input("5"), True)
        self.assertEqual(self.tic_tac.validate_input("111"), False)
        self.assertEqual(self.tic_tac.validate_input("0"), False)
        self.assertEqual(self.tic_tac.validate_input("10"), False)
        self.assertEqual(self.tic_tac.validate_input("AAA"), False)
        self.assertEqual(self.tic_tac.validate_input(6), False)
        self.assertEqual(self.tic_tac.validate_input("a"), False)
        self.assertEqual(self.tic_tac.validate_input("___"), False)
        self.assertEqual(self.tic_tac.validate_input(False), False)


if __name__ == '__main__':
    unittest.main()
