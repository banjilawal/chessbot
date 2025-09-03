import unittest

from chess.common.config import ROW_SIZE, COLUMN_SIZE
from chess.exception.coord import ColumnBelowBoundsException
from chess.exception.coord import RowBelowBoundsException
from chess.exception.null.coord import NullCoordinateException
from chess.exception.null.column import NullColumnException
from chess.exception.null.row import NullRowException

from chess.geometry.coord import Coordinate


class EuclidDistanceTest(unittest.TestCase):

    def test_null_p_coord_raises_exception(self):
        with self.assertRaises(NullCoordinateException):
           Distance(p=None, q=Coordinate(row=0, column=0))


    def test_null_p_row_raises_exception(self):
        with self.assertRaises(NullRowException):
           Distance(p=Coordinate(row=None, column=0), q=Coordinate(row=0, column=0))


    def  test_p_row_below_lower_bounds_raises_exception(self):
        with self.assertRaises(RowBelowBoundsException):
            Distance(p=Coordinate(row=-1, column=0), q=Coordinate(row=0, column=0))


    def  test_p_row_above_upper_bounds_raises_exception(self):
        with self.assertRaises(RowBelowBoundsException):
            Distance(p=Coordinate(row=ROW_SIZE, column=0), q=Coordinate(row=0, column=0))

    def test_p_row_in_bounds(self):
        # Valid rows should construct a Coordinate without exceptions
        for row in range(0, ROW_SIZE):
            cartesian_distance = Distance(
                p=Coordinate(row=row, column=0),
                q=Coordinate(row=0, column=0)
            )
            self.assertEqual(cartesian_distance.p.row, row)


    def test_null_p_column_raises_exception(self):
        with self.assertRaises(NullColumnException):
           Distance(p=Coordinate(row=0, column=None), q=Coordinate(row=0, column=0))


    def test_p_column_below_lower_bounds_raises_exception(self):
        with self.assertRaises(ColumnBelowBoundsException):
            Distance(p=Coordinate(row=0, column=-1), q=Coordinate(row=0, column=0))

    def test_p_column_above_upper_bounds_raises_exception(self):
        with self.assertRaises(ColumnBelowBoundsException):
            Distance(p=Coordinate(row=0, column=COLUMN_SIZE), q=Coordinate(row=0, column=0))


    def test_p_column_in_bounds(self):
        # Valid rows should construct a Coordinate without exceptions
        for col in range(0, COLUMN_SIZE):
            cartesian_distance = Distance(
                p=Coordinate(row=0, column=col),
                q=Coordinate(row=0, column=0)
            )
            self.assertEqual(cartesian_distance.p.column, col)


    def test_null_q_coord_raises_exception(self):
        with self.assertRaises(NullCoordinateException):
            Distance(p=Coordinate(row=0, column=0), q=None)


    def test_null_q_row_raises_exception(self):
        with self.assertRaises(NullRowException):
            Distance(p=Coordinate(row=0, column=0), q=Coordinate(row=None, column=0))


    def test_q_row_below_lower_bounds_raises_exception(self):
        with self.assertRaises(RowBelowBoundsException):
            Distance(p=Coordinate(row=0, column=0), q=Coordinate(row=-1, column=0))


    def test_q_row_above_upper_bounds_raises_exception(self):
        with self.assertRaises(RowBelowBoundsException):
            Distance(p=Coordinate(row=0, column=0), q=Coordinate(row=ROW_SIZE, column=0))


    def test_q_row_in_bounds(self):
        # Valid rows should construct a Coordinate without exceptions
        for row in range(0, ROW_SIZE):
            cartesian_distance = Distance(
                p=Coordinate(row=0, column=0),
                q=Coordinate(row=row, column=0)
            )
            self.assertEqual(cartesian_distance.q.row, row)


    def test_null_q_column_raises_exception(self):
        with self.assertRaises(NullColumnException):
            Distance(p=Coordinate(row=0, column=0), q=Coordinate(row=0, column=None))


    def test_q_column_below_lower_bounds_raises_exception(self):
        with self.assertRaises(ColumnBelowBoundsException):
            Distance(p=Coordinate(row=0, column=0), q=Coordinate(row=0, column=-1))

    def test_q_column_above_upper_bounds_raises_exception(self):
        with self.assertRaises(ColumnBelowBoundsException):
            Distance(p=Coordinate(row=0, column=0), q=Coordinate(row=0, column=COLUMN_SIZE))


    def test_q_column_in_bounds(self):
        for col in range(0, COLUMN_SIZE):
            cartesian_distance = Distance(
                p=Coordinate(row=0, column=0),
                q=Coordinate(row=0, column=col)
            )
            self.assertEqual(cartesian_distance.q.column, col)


if __name__ == '__main__':
    unittest.main()