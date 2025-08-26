import unittest

import pytest

from chess.common.config import KNIGHT_STEP_SIZE, BOARD_DIMENSION

from chess.exception.null.column_offset import NullColumnOffsetException
from chess.exception.null.row_offset import NullRowOffsetException
from chess.exception.offset.column import DeltaColumnBelowSteppingBoundException, DeltaColumnAboveSteppingBoundException
from chess.exception.offset.row import DeltaRowBelowSteppingBoundException, DeltaRowAboveSteppingBoundException
from chess.geometry.coordinate.offset import Offset


class OffSetTest(unittest.TestCase):

    def test_null_delta_row_raises_exception(self):
        with pytest.raises(NullRowOffsetException):
            Offset(delta_row=None, delta_column=0)


    def test_delta_row_below_bounds_raises_error(self):
        with self.assertRaises(DeltaRowBelowSteppingBoundException):
            Offset(delta_row=-(KNIGHT_STEP_SIZE + 1), delta_column=0)


    def test_delta_row_above_bounds_raises_error(self):
        with self.assertRaises(DeltaRowAboveSteppingBoundException):
            Offset(delta_row=(KNIGHT_STEP_SIZE + 1), delta_column=0)


    # def test_row_offset_above_knight_range_raises_error(self):
    #     with self.assertRaises(OffsetRangeException):
    #         Offset(row_offset=(KNIGHT_STEP_SIZE + 1), delta_column=0)


    def test_delta_row_less_or_equal_to_knight_step_size(self):
        # Valid rows should construct a Coordinate without exceptions
        lower_bound = -(KNIGHT_STEP_SIZE + 1)
        upper_bound = KNIGHT_STEP_SIZE + 1
        for delta in range(lower_bound, upper_bound):
            offset = Offset(delta_row=delta, delta_column=0)
            print(f"Testing delta_row: {offset.delta_row} delta={delta}")
            self.assertEqual(offset.delta_row, delta)

    def test_null_delta_column_raises_exception(self):
        with pytest.raises(NullColumnOffsetException):
            Offset(delta_row=0, delta_column=None)

    def test_delta_column_below_bounds_raises_error(self):
        with self.assertRaises(DeltaColumnBelowSteppingBoundException):
            Offset(delta_row=0, delta_column=-(KNIGHT_STEP_SIZE + 1))

    def test_delta_column_above_bounds_raises_error(self):
        with self.assertRaises(DeltaColumnAboveSteppingBoundException):
            Offset(delta_row=0, delta_column=KNIGHT_STEP_SIZE + 1)

    # def test_row_offset_above_knight_range_raises_error(self):
    #     with self.assertRaises(OffsetRangeException):
    #         Offset(row_offset=(KNIGHT_STEP_SIZE + 1), delta_column=0)

    def test_delta_column_less_or_equal_to_knight_step_size(self):
        # Valid rows should construct a Coordinate without exceptions
        lower_bound = -(KNIGHT_STEP_SIZE + 1)
        upper_bound = KNIGHT_STEP_SIZE + 1
        for delta in range(lower_bound, upper_bound):
            offset = Offset(delta_row=0, delta_column=delta)
            print(f"Testing delta_column: {offset.delta_column} delta={delta}")
            self.assertEqual(offset.delta_column, delta)

    #
    # def test_null_multiplicaton_scalar_out_of_bounds_raises_exception(self):
    #     offset = Offset(row_offset=1, delta_column=1)
    #     with pytest.raises(NullOffSetFactor):
    #         offset.__mul__(factor=None)
    #
    # def test_multiplication_scalar_out_of_bounds_raises_exception(self):
    #     offset = Offset(row_offset=1, delta_column=1)
    #     # Test with a scalar that exceeds BOARD_DIMENSION
    #     with pytest.raises(MultiplierOutOfBoundsException):
    #         offset.__mul__(BOARD_DIMENSION + 1)  # This will trigger scalar bounds check
    #
    # def test_multiplication_scalar_at_boundary_raises_result_exception(self):
    #     offset = Offset(row_offset=1, delta_column=1)
    #     # Test with BOARD_DIMENSION - should pass scalar check but fail result check
    #     with pytest.raises(OffsetMultiplicationOverflowException):
    #         offset.__mul__(BOARD_DIMENSION)  # 1 * 8 = 8, which >= BOARD_DIMENSION
    #
    # def test_multiplication_result_out_of_bounds_raises_exception(self):
    #     offset = Offset(row_offset=2, delta_column=1)
    #     # This should trigger the result bounds check
    #     with pytest.raises(OffsetMultiplicationOverflowException):
    #         offset.__mul__(4)  # 2 * 4 = 8, which >= BOARD_DIMENSION


if __name__ == '__main__':
    unittest.main()
