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


    def test_delta_row_less_or_equal_to_knight_step_size(self):
        # Test all valid delta_row values from -3 to +3 inclusive
        # print()
        for delta_row in range(-KNIGHT_STEP_SIZE, KNIGHT_STEP_SIZE + 1):
            offset = Offset(delta_row=delta_row, delta_column=0)
            # print(f"Testing delta_row: {offset.delta_row} expected={delta_row}")
            self.assertEqual(offset.delta_row, delta_row)


    def test_null_delta_column_raises_exception(self):
        with pytest.raises(NullColumnOffsetException):
            Offset(delta_row=0, delta_column=None)


    def test_delta_column_below_bounds_raises_error(self):
        with self.assertRaises(DeltaColumnBelowSteppingBoundException):
            Offset(delta_row=0, delta_column=-(KNIGHT_STEP_SIZE + 1))


    def test_delta_column_above_bounds_raises_error(self):
        with self.assertRaises(DeltaColumnAboveSteppingBoundException):
            Offset(delta_row=0, delta_column=KNIGHT_STEP_SIZE + 1)


    def test_delta_column_less_or_equal_to_knight_step_size(self):
        # Test all valid delta_columns values from -3 to +3 inclusive
        # print()
        for delta_column in range(-KNIGHT_STEP_SIZE, KNIGHT_STEP_SIZE + 1):
            offset = Offset(delta_row=0, delta_column=delta_column)
            # print(f"Testing delta_column: {offset.delta_column} expected={delta_column}")
            self.assertEqual(offset.delta_column, delta_column)


if __name__ == '__main__':
    unittest.main()
