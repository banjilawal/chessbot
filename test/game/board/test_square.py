import unittest
from unittest.mock import Mock

from game.board.board_square import GameBoardSquare


class TestGameBoardSquare(unittest.TestCase):

    # ID tests
    def test_valid_id(self):
        """Test square creation with valid ID"""
        squares_cell = GameBoardSquare(id=1, row=0, column=0)
        self.assertEqual(squares_cell.id, 1)

    # Row tests
    def test_valid_row(self):
        """Test square creation with valid row"""
        squares_cell = GameBoardSquare(id=1, row=0, column=0)
        self.assertEqual(squares_cell.row, 0)

    def test_invalid_row(self):
        """Test square creation with invalid row"""
        with self.assertRaises(ValueError):
            GameBoardSquare(id=1, row=-1, column=0)

    # Column tests
    def test_valid_column(self):
        """Test square creation with valid column"""
        squares_cell = GameBoardSquare(id=1, row=0, column=0)
        self.assertEqual(squares_cell.column, 0)

    def test_invalid_column(self):
        """Test square creation with invalid column"""
        with self.assertRaises(ValueError):
            GameBoardSquare(id=1, row=0, column=-1)


if __name__ == '__main__':
    unittest.main()




