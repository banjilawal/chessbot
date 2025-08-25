import unittest

import pytest

from chess.common.config import ROW_SIZE, COLUMN_SIZE
from chess.exception.coordinate.column_out_of_bounds import ColumnOutOfBoundsException
from chess.exception.coordinate.row_out_of_bounds import RowOutOfBoundsException
from chess.exception.null.coordinate_null import NullCoordinateException
from chess.exception.null.null_column import NullColumnException
from chess.exception.null.null_row import NullRowException
from chess.geometry.coordinate.distance_magnitude import DistanceMagnitude
from chess.geometry.coordinate.coordinate import Coordinate


class DistanceMagnitudeTest(unittest.TestCase):

    def test_null_p_coord_raises_exception(self):
        with pytest.raises(NullCoordinateException):
           DistanceMagnitude(p=None, q=Coordinate(row=0, column=0))


    def test_null_p_row_raises_exception(self):
        with pytest.raises(NullRowException):
           DistanceMagnitude(p=Coordinate(row=None, column=0), q=Coordinate(row=0, column=0))


    def  test_p_row_below_lower_bounds_raises_exception(self):
        with self.assertRaises(RowOutOfBoundsException):
            DistanceMagnitude(p=Coordinate(row=-1, column=0), q=Coordinate(row=0, column=0))


    def  test_p_row_above_upper_bounds_raises_exception(self):
        with self.assertRaises(RowOutOfBoundsException):
            DistanceMagnitude(p=Coordinate(row=ROW_SIZE, column=0), q=Coordinate(row=0, column=0))

    def test_p_row_in_bounds(self):
        # Valid rows should construct a Coordinate without exceptions
        for row in range(0, ROW_SIZE):
            cartesian_distance = DistanceMagnitude(
                p=Coordinate(row=row, column=0),
                q=Coordinate(row=0, column=0)
            )
            self.assertEqual(cartesian_distance.p.row, row)


    def test_null_p_column_raises_exception(self):
        with pytest.raises(NullColumnException):
           DistanceMagnitude(p=Coordinate(row=0, column=None), q=Coordinate(row=0, column=0))


    def test_p_column_below_lower_bounds_raises_exception(self):
        with self.assertRaises(ColumnOutOfBoundsException):
            DistanceMagnitude(p=Coordinate(row=0, column=-1), q=Coordinate(row=0, column=0))

    def test_p_column_above_upper_bounds_raises_exception(self):
        with self.assertRaises(ColumnOutOfBoundsException):
            DistanceMagnitude(p=Coordinate(row=0, column=COLUMN_SIZE), q=Coordinate(row=0, column=0))


    def test_p_column_in_bounds(self):
        # Valid rows should construct a Coordinate without exceptions
        for col in range(0, COLUMN_SIZE):
            cartesian_distance = DistanceMagnitude(
                p=Coordinate(row=0, column=col),
                q=Coordinate(row=0, column=0)
            )
            self.assertEqual(cartesian_distance.p.column, col)


    def test_null_q_coord_raises_exception(self):
        with pytest.raises(NullCoordinateException):
            DistanceMagnitude(p=Coordinate(row=0, column=0), q=None)


    def test_null_q_row_raises_exception(self):
        with pytest.raises(NullRowException):
            DistanceMagnitude(p=Coordinate(row=0, column=0), q=Coordinate(row=None, column=0))


    def test_q_row_below_lower_bounds_raises_exception(self):
        with self.assertRaises(RowOutOfBoundsException):
            DistanceMagnitude(p=Coordinate(row=0, column=0), q=Coordinate(row=-1, column=0))


    def test_q_row_above_upper_bounds_raises_exception(self):
        with self.assertRaises(RowOutOfBoundsException):
            DistanceMagnitude(p=Coordinate(row=0, column=0), q=Coordinate(row=ROW_SIZE, column=0))


    def test_q_row_in_bounds(self):
        # Valid rows should construct a Coordinate without exceptions
        for row in range(0, ROW_SIZE):
            cartesian_distance = DistanceMagnitude(
                p=Coordinate(row=0, column=0),
                q=Coordinate(row=row, column=0)
            )
            self.assertEqual(cartesian_distance.q.row, row)


    def test_null_q_column_raises_exception(self):
        with pytest.raises(NullColumnException):
            DistanceMagnitude(p=Coordinate(row=0, column=0), q=Coordinate(row=0, column=None))


    def test_q_column_below_lower_bounds_raises_exception(self):
        with self.assertRaises(ColumnOutOfBoundsException):
            DistanceMagnitude(p=Coordinate(row=0, column=0), q=Coordinate(row=0, column=-1))

    def test_q_column_above_upper_bounds_raises_exception(self):
        with self.assertRaises(ColumnOutOfBoundsException):
            DistanceMagnitude(p=Coordinate(row=0, column=0), q=Coordinate(row=0, column=COLUMN_SIZE))


    def test_q_column_in_bounds(self):
        for col in range(0, COLUMN_SIZE):
            cartesian_distance = DistanceMagnitude(
                p=Coordinate(row=0, column=0),
                q=Coordinate(row=0, column=col)
            )
            self.assertEqual(cartesian_distance.q.column, col)


if __name__ == '__main__':
    unittest.main()