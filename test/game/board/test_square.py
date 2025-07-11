import unittest
from unittest.mock import Mock

from model.cell import Cell
from src.common.constants import Config
from src.exception.exception import InvalidIdError, NegativeRowError, NegativeColumnError
from model.grid_entity import GridEntity


class TestGameBoardSquare(unittest.TestCase):

    def setUp(self):
        self.mock_figure = Mock()
        self.mock_figure._square = None
        self.square = Cell(_id=1, _row=0, _column=0)


    def test_constructing_square_with_valid_id(self):
        """Test cell creation with valid ID"""
        square = Cell(_id=1, _row=0, _column=0)
        self.assertGreaterEqual(square._id, Config.MINIMUM_ID)

    def test_invalid_id_raises_error(self):
        """Test cell creation with invalid ID"""
        with self.assertRaises(InvalidIdError):
            Cell(_id=-1, _row=0, _column=-1)

    def test_constructing_square_with_valid_row(self):
        """Test cell creation with a valid row"""
        square = Cell(_id=1, _row=0, _column=0)
        self.assertGreaterEqual(square._row, 0)

    def test_invalid_row_raises_error(self):
        """Test cell creation with an invalid row"""
        with self.assertRaises(NegativeRowError):
            Cell(_id=1, _row=-1, _column=0)

    # Column tests
    def test_constructing_square_with_valid_column(self):
        """Test cell creation with a valid column"""
        square = Cell(_id=1, _row=0, _column=0)
        self.assertGreaterEqual(square._column, 0)

    def test_invalid_colum_raises_error(self):
        """Test cell creation with an invalid column"""
        with self.assertRaises(NegativeColumnError):
            Cell(_id=1, _row=0, _column=-1)

    def test_square_occupied_by_figure_returns_true(self):
        self.square._occupant = self.mock_figure
        self.assertTrue(self.square.occupied)

    def test_square_not_occupied_by_figure_returns_true(self):
        self.square._occupant = None
        self.assertFalse(self.square.occupied)

    def test_square_is_unoccupied_when_figure_leaves(self):
        figure: GridEntity = GridEntity(id=1, length=2, height=3)
        figure.enter_square(self.square)
        figure.leave_square()
        self.assertIsNone(self.square._occupant)

    def test_figure_leaving_square_looses_ownership(self):
        figure: GridEntity = GridEntity(id=1, length=2, height=3)
        figure.enter_square(self.square)
        figure.leave_square()
        self.assertNotEqual(self.square._occupant, figure)

    def test_square_is_occupied_by_entering_figure(self):
        figure: GridEntity = GridEntity(id=1, length=2, height=3)
        figure.enter_square(self.square)
        self.assertEqual(self.square.occupant, figure)

    def test_figure_entering_square_gains_ownership(self):
        figure: GridEntity = GridEntity(id=1, length=2, height=3)
        figure.enter_square(self.square)
        self.assertEqual(self.square.occupant, figure)

if __name__ == '__main__':
    unittest.main()




