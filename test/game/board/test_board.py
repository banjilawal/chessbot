import unittest

from game.board.board_square import GameBoardSquare
from game.board.game_board import GameBoard


class TestGameBoardSquare(unittest.TestCase):
    def test_init(self):
        """Test basic initialization with valid values"""
        square = GameBoardSquare(id=1, row=0, column=0)
        self.assertIsNotNone(square)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.row, 0)
        self.assertEqual(square.column, 0)

    # ID tests
    def test_valid_id(self):
        """Test square creation with valid ID"""
        squares_cell = GameBoardSquare(id=1, row=0, column=0)
        self.assertEqual(squares_cell.id, 1)

    def test_invalid_id(self):
        """Test square creation with invalid ID"""
        with self.assertRaises(ValueError):
            GameBoardSquare(id=-1, row=0, column=0)

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


class TestGameBoard(unittest.TestCase):
    def test_init(self):
        """Test basic board initialization with valid values"""
        board = GameBoard(rows=3, columns=3)
        self.assertIsNotNone(board)
        self.assertEqual(board.rows, 3)
        self.assertEqual(board.columns, 3)
        self.assertIsNotNone(board.squares)

    # Rows tests
    def test_valid_rows(self):
        """Test board creation with valid number of rows"""
        board = GameBoard(rows=3, columns=3)
        self.assertEqual(board.rows, 3)

    def test_invalid_rows(self):
        """Test board creation with invalid number of rows"""
        with self.assertRaises(ValueError):
            GameBoard(rows=-1, columns=3)

    # Columns tests
    def test_valid_columns(self):
        """Test board creation with valid number of columns"""
        board = GameBoard(rows=3, columns=3)
        self.assertEqual(board.columns, 3)

    def test_invalid_columns(self):
        """Test board creation with invalid number of columns"""
        with self.assertRaises(ValueError):
            GameBoard(rows=3, columns=-1)

if __name__ == '__main__':
    unittest.main()