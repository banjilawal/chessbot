import unittest
from unittest.mock import create_autospec

import pytest

from chess.common.config import COLUMN_SIZE, ROW_SIZE
from chess.exception.coord import ColumnBelowBoundsException
from chess.exception.coord import RowBelowBoundsException
from chess.exception.null.column import NullColumnException
from chess.exception.null.row import NullRowException

from chess.geometry.coordinate.coord import Coordinate


class CoordinateTest(unittest.TestCase):

    @staticmethod
    def valid_mock_coordinate(row=0, column=0):
        coord = create_autospec(Coordinate, instance=True)
        coord.row = row
        coord.column = column

        return coord


    def test_null_row_raises_exception(self):
        with self.assertRaises(NullRowException):
            Coordinate(row=None, column=0)


    def test_row_in_bounds(self):
        # Valid rows should construct a Coordinate without exceptions
        for row in range(0, ROW_SIZE):
            coord = Coordinate(row=row, column=0)
            self.assertEqual(coord.row, row)


    def test_row_below_lower_bound_raises_exception(self):
        with self.assertRaises(RowBelowBoundsException):
            Coordinate(row=-1, column=0)


    def test_row_above_upper_bound_raises_exception(self):
        with self.assertRaises(RowBelowBoundsException):
            Coordinate(row=ROW_SIZE, column=0)


    def test_null_column_raises_exception(self):
        with self.assertRaises(NullColumnException):
            Coordinate(row=0, column=None)


    def test_column_in_bounds(self):
        # Tests all columns within bounds construct a Coordinate without exceptions
        for column in range(0, COLUMN_SIZE):
            coord = Coordinate(row=0, column=column)
            self.assertEqual(coord.column, column)


    def test_column_below_lower_bound_raises_exception(self):
        with self.assertRaises(ColumnBelowBoundsException):
            Coordinate(row=0, column=-1)


    def test_column_above_upper_bound_raises_exception(self):
        with self.assertRaises(ColumnBelowBoundsException):
            Coordinate(row=0, column=COLUMN_SIZE)


if __name__ == '__main__':
    unittest.main()
