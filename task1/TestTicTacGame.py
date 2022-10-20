import unittest
from TicTacGame import TicTacGame


class TestTicTacGame(unittest.TestCase):
    def setUp(self):
        self.tic_tac = TicTacGame()

    def test_validate_input(self):
        self.assertEqual(self.tic_tac.validate_input("5"), True)
        self.assertEqual(self.tic_tac.validate_input("111"), False)
        self.assertEqual(self.tic_tac.validate_input("0"), False)
        self.assertEqual(self.tic_tac.validate_input("10"), False)
        self.assertEqual(self.tic_tac.validate_input("AAA"), False)
        self.assertEqual(self.tic_tac.validate_input(6), False)
        self.assertEqual(self.tic_tac.validate_input("a"), False)
        self.assertEqual(self.tic_tac.validate_input("___"), False)
        self.assertEqual(self.tic_tac.validate_input(False), False)

    def test_pick_cell(self):
        self.assertIn(self.tic_tac.pick_cell(), range(1, 10))

    def test_check_winner(self):
        self.assertEqual(self.tic_tac.check_winner(), False)

    def test_start_game(self):
        self.assertIn(self.tic_tac.start_game(),
                      ["Draw!", "Xs win!", "Os win!"])

    def test_auto_pick_cell(self):
        self.assertIn(self.tic_tac.auto_pick_cell(), range(1, 10))

    def test_p2p_mode(self):
        self.assertIn(self.tic_tac.p2p_mode(), ["Draw!", "Xs win!", "Os win!"])

    def test_p2c_mode(self):
        self.assertIn(self.tic_tac.p2c_mode(), ["Draw!", "Xs win!", "Os win!"])

    def test_c2c_mode(self):
        self.assertIn(self.tic_tac.c2c_mode(), ["Draw!", "Xs win!", "Os win!"])


if __name__ == '__main__':
    unittest.main()
