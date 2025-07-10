import unittest

from model.grid import Grid
from src.exception.exception import InvalidNumberOfRowsError, InvalidNumberOfColumnsError


class TestGameBoard(unittest.TestCase):
    def test_init(self):
        """Test basic board initialization with valid values"""
        board = Grid(id=1, row_count=3, column_count=3)
        self.assertIsNotNone(board)
        self.assertEqual(board.row_count, 3)
        self.assertEqual(board.column_count, 3)
        self.assertIsNotNone(board.squares)

    # Rows tests
    def test_valid_rows(self):
        """Test board creation with valid number of num_rows"""
        board = Grid(id=1, row_count=3, column_count=3)
        self.assertEqual(board.column_count, 3)

    def test_invalid_rows(self):
        """Test board creation with invalid number of num_rows"""
        with self.assertRaises(InvalidNumberOfRowsError):
            Grid(id=1, row_count=-1, column_count=3)

    # Columns tests
    def test_valid_columns(self):
        """Test board creation with valid number of num_columns"""
        board = Grid(id=1, row_count=3, column_count=3)
        self.assertEqual(board.columns, 3)

    def test_invalid_columns(self):
        """Test board creation with invalid number of num_columns"""
        with self.assertRaises(InvalidNumberOfColumnsError):
            Grid(id=1, row_count=3, column_count=-1)

if __name__ == '__main__':
    unittest.main()