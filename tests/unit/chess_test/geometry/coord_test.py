import unittest
from unittest.mock import create_autospec

from chess.system.config import COLUMN_SIZE, ROW_SIZE
from chess.exception.coord_exception import ColumnBelowBoundsException
from chess.exception.coord_exception import RowBelowBoundsException
from chess.coord.coord_exception import NullColumnException
from chess.coord.coord_exception import NullRowException

from chess.coord import Coord


class CoordTest(unittest.TestCase):

    @staticmethod
    def valid_mock_coord(row=0, column=0):
        coord = create_autospec(Coord, instance=True)
        coord.row = row
        coord.column = column

        return coord


    def test_null_row_raises_exception(self):
        with self.assertRaises(NullRowException):
            Coord(row=None, column=0)


    def test_row_in_bounds(self):
        # Valid rows should construct a Coord without exceptions
        for row in range(0, ROW_SIZE):
            coord = Coord(row=row, column=0)
            self.assertEqual(coord.row, row)


    def test_row_below_lower_bound_raises_exception(self):
        with self.assertRaises(RowBelowBoundsException):
            Coord(row=-1, column=0)


    def test_row_above_upper_bound_raises_exception(self):
        with self.assertRaises(RowBelowBoundsException):
            Coord(row=ROW_SIZE, column=0)


    def test_null_column_raises_exception(self):
        with self.assertRaises(NullColumnException):
            Coord(row=0, column=None)


    def test_column_in_bounds(self):
        # Tests all columns within bounds construct a Coord without exceptions
        for column in range(0, COLUMN_SIZE):
            coord = Coord(row=0, column=column)
            self.assertEqual(coord.column, column)


    def test_column_below_lower_bound_raises_exception(self):
        with self.assertRaises(ColumnBelowBoundsException):
            Coord(row=0, column=-1)


    def test_column_above_upper_bound_raises_exception(self):
        with self.assertRaises(ColumnBelowBoundsException):
            Coord(row=0, column=COLUMN_SIZE)


if __name__ == '__main__':
    unittest.main()
