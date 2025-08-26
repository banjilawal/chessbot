import unittest

import pytest

from chess.common.config import BOARD_DIMENSION
from chess.exception.null.scalar import NullScalarException
from chess.exception.offset.mul import ScalarBelowLowerBoundException, ZeroScalarException, \
    ScalarAboveUpperBoundException, RowDeltaOverflowExceptioDn
from chess.geometry.vector.delta import Offset


class OffsetMultiplicationTest(unittest.TestCase):

    def test_null_multiplication_factor_raises_error(self):
        with pytest.raises(NullScalarException):
            Offset(delta_row=1, delta_column=1).__mul__(factor=None)


    def test_negative_multiplication_raises_error(self):
        with pytest.raises(ScalarBelowLowerBoundException):
            Offset(delta_row=1, delta_column=1).__mul__(factor=-1)

    def test_zero_multiplication_raises_error(self):
        with pytest.raises(ZeroScalarException):
            Offset(delta_row=1, delta_column=1).__mul__(factor=-0)

    def test_multiplication_factor_out_of_bounds_raises_error(self):
        with pytest.raises(ScalarAboveUpperBoundException):
            Offset(delta_row=1, delta_column=1).__mul__(factor=BOARD_DIMENSION)

    def test_delta_row_result_out_of_bounds_raises_error(self):
        with pytest.raises(RowDeltaOverflowExceptioDn):
            Offset(delta_row=4, delta_column=1).__mul__(factor=2)

    def test_delta_column_result_out_of_bounds_raises_error(self):
        self.assertEqual(True, False)

    def test_multiplication_factor_within_bounds_succeeds(self):
        self.assertEqual(True, False)

    def test_delta_row_result_within_bounds_succeeds(self):
        self.assertEqual(True, False)

    def test_delta_column_result_within_bounds_succeeds(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
