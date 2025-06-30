import unittest

from game.model.board.game_board import GameBoard
from game.exception.exception import InvalidNumberOfRowsError, InvalidNumberOfColumnsError


class TestGameBoard(unittest.TestCase):
    def test_init(self):
        """Test basic board initialization with valid values"""
        board = GameBoard(id=1, num_rows=3, num_columns=3)
        self.assertIsNotNone(board)
        self.assertEqual(board.num_rows, 3)
        self.assertEqual(board.num_columns, 3)
        self.assertIsNotNone(board.squares)

    # Rows tests
    def test_valid_rows(self):
        """Test board creation with valid number of num_rows"""
        board = GameBoard(id=1, num_rows=3, num_columns=3)
        self.assertEqual(board.num_columns, 3)

    def test_invalid_rows(self):
        """Test board creation with invalid number of num_rows"""
        with self.assertRaises(InvalidNumberOfRowsError):
            GameBoard(id=1, num_rows=-1, num_columns=3)

    # Columns tests
    def test_valid_columns(self):
        """Test board creation with valid number of num_columns"""
        board = GameBoard(id=1, num_rows=3, num_columns=3)
        self.assertEqual(board.columns, 3)

    def test_invalid_columns(self):
        """Test board creation with invalid number of num_columns"""
        with self.assertRaises(InvalidNumberOfColumnsError):
            GameBoard(id=1, num_rows=3, num_columns=-1)

if __name__ == '__main__':
    unittest.main()