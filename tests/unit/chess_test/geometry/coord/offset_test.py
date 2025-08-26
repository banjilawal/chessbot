import unittest

import pytest

from chess.common.config import KNIGHT_WALKING_RANGE, BOARD_DIMENSION
from chess.exception.coordinate.offset_result import OffsetMultiplicationResultException
from chess.exception.coordinate.multiplier import OffsetMultiplicationFactorException
from chess.exception.coordinate.offset_range import OffsetRangeException
from chess.exception.null.column_offset import NullColumnOffsetException
from chess.exception.null.offset_factor import NullOffSetFactor
from chess.exception.null.row_offset import NullRowOffsetException
from chess.geometry.coordinate.offset import Offset


class OffSetTest(unittest.TestCase):

    def test_null_row_offset_raises_error(self):
        with pytest.raises(NullRowOffsetException):
            Offset(row_offset=None, column_offset=0)


    def test_row_offset_below_knight_range_raises_error(self):
        with self.assertRaises(OffsetRangeException):
            Offset(row_offset= -(KNIGHT_WALKING_RANGE+1), column_offset=0)


    def test_row_offset_above_knight_range_raises_error(self):
        with self.assertRaises(OffsetRangeException):
            Offset(row_offset=(KNIGHT_WALKING_RANGE+1), column_offset=0)


    def test_row_offset_in_knigt_walking_range(self):
        # Valid rows should construct a Coordinate without exceptions
        for i in range(-KNIGHT_WALKING_RANGE, KNIGHT_WALKING_RANGE):
            offset = Offset(row_offset=i, column_offset=0)
            self.assertEqual(offset.row_offset, i)


    def test_null_column_offset_raises_error(self):
        with pytest.raises(NullColumnOffsetException):
            Offset(row_offset=0, column_offset=None)


    def test_column_offset_below_knight_range_raises_error(self):
        with self.assertRaises(OffsetRangeException):
            Offset(row_offset=0, column_offset= -(KNIGHT_WALKING_RANGE+1))


    def test_column_offset_above_knight_range_raises_error(self):
        with self.assertRaises(OffsetRangeException):
            Offset(row_offset=0, column_offset=(KNIGHT_WALKING_RANGE+1))


    def test_column_offset_in_knigt_walking_range(self):
        # Valid rows should construct a Coordinate without exceptions
        for i in range(-KNIGHT_WALKING_RANGE, KNIGHT_WALKING_RANGE):
            offset = Offset(row_offset=0, column_offset=i)
            self.assertEqual(offset.column_offset, i)

    def test_null_multiplicaton_scalar_out_of_bounds_raises_exception(self):
        offset = Offset(row_offset=1, column_offset=1)
        with pytest.raises(NullOffSetFactor):
            offset.__mul__(scalar=None)

    def test_multiplication_scalar_out_of_bounds_raises_exception(self):
        offset = Offset(row_offset=1, column_offset=1)
        # Test with a scalar that exceeds BOARD_DIMENSION
        with pytest.raises(OffsetMultiplicationFactorException):
            offset.__mul__(BOARD_DIMENSION + 1)  # This will trigger scalar bounds check

    def test_multiplication_scalar_at_boundary_raises_result_exception(self):
        offset = Offset(row_offset=1, column_offset=1)
        # Test with BOARD_DIMENSION - should pass scalar check but fail result check
        with pytest.raises(OffsetMultiplicationResultException):
            offset.__mul__(BOARD_DIMENSION)  # 1 * 8 = 8, which >= BOARD_DIMENSION

    def test_multiplication_result_out_of_bounds_raises_exception(self):
        offset = Offset(row_offset=2, column_offset=1)
        # This should trigger the result bounds check
        with pytest.raises(OffsetMultiplicationResultException):
            offset.__mul__(4)  # 2 * 4 = 8, which >= BOARD_DIMENSION


if __name__ == '__main__':
    unittest.main()
