import unittest

import pytest

from chess.common.config import KNIGHT_STEP_SIZE

from chess.exception.null.x_dim import XComponentNullException
from chess.exception.null.y_dim import YComponentNullException
from chess.exception.offset.column import YVectorBelowMinValueException, YVectorAboveMaxValueException
from chess.exception.offset.row import XVectorBelowMinValueException, XVectorAboveMaxValueException
from chess.geometry.vector.delta import Vector


class VectorTest(unittest.TestCase):

    def test_null_x_raises_exception(self):
        with pytest.raises(YComponentNullException):
            Vector(x=None, y=0)


    def test_x_below_min_bound_raises_error(self):
        with self.assertRaises(XVectorBelowMinValueException):
            Vector(x=-(KNIGHT_STEP_SIZE + 1), y=0)


    def test_x_above_max_bound_raises_error(self):
        with self.assertRaises(XVectorAboveMaxValueException):
            Vector(x=(KNIGHT_STEP_SIZE + 1), y=0)


    def test_x_between_min_and_max_bounds(self):
        # Test all valid delta_row values from -3 to +3 inclusive
        # print()
        for x in range(-KNIGHT_STEP_SIZE, KNIGHT_STEP_SIZE + 1):
            vector = Vector(x=x, y=0)
            # print(f"Testing delta_row: {vector.delta_row} expected={delta_row}")
            self.assertEqual(vector.x, x)


    def test_null_y_raises_exception(self):
        with pytest.raises(XComponentNullException):
            Vector(x=0, y=None)


    def test_y_below_min_bound_raises_error(self):
        with self.assertRaises(YVectorBelowMinValueException):
            Vector(x=0, y=-(KNIGHT_STEP_SIZE + 1))


    def test_y_above_max_bound_raises_error(self):
        with self.assertRaises(YVectorAboveMaxValueException):
            Vector(x=0, y=(KNIGHT_STEP_SIZE + 1))


    def test_y_between_min_and_max_bounds(self):
        # Test all valid delta_row values from -3 to +3 inclusive
        # print()
        for y in range(-KNIGHT_STEP_SIZE, KNIGHT_STEP_SIZE + 1):
            vector = Vector(x=0, y=y)
            # print(f"Testing delta_row: {vector.delta_row} expected={delta_row}")
            self.assertEqual(vector.y, y)


if __name__ == '__main__':
    unittest.main()
