import unittest

import pytest

from chess.common.config import KNIGHT_STEP_SIZE

from chess.exception.null.x_dim import XComponentNullException
from chess.exception.null.y_dim import YComponentNullException
from chess.exception.offset.column import YComponentBelowLowerBoundException, YComponentAboveUpperBoundException
from chess.exception.offset.row import XComponentBelowLowerBoundException, XComponentAboveUpperBoundException
from chess.geometry.vector.delta import Vector


class VectorTest(unittest.TestCase):

    def test_null_x_component_raises_exception(self):
        with self.assertRaises(XComponentNullException):
            Vector(x=None, y=0)

    def test_x_component_below_lower_bound_raises_error(self):
        with self.assertRaises(XComponentBelowLowerBoundException):
            Vector(x=-(KNIGHT_STEP_SIZE + 1), y=0)


    def test_x_component_above_upper_bound_raises_error(self):
        with self.assertRaises(XComponentAboveUpperBoundException):
            Vector(x=(KNIGHT_STEP_SIZE + 1), y=0)


    def test_x_component_within_bounds(self):
        # Test all valid delta_row values from -3 to +3 inclusive
        # print()
        for x in range(-KNIGHT_STEP_SIZE, KNIGHT_STEP_SIZE + 1):
            vector = Vector(x=x, y=0)
            # print(f"Testing delta_row: {distance_test.delta_row} expected={delta_row}")
            self.assertEqual(vector.x, x)


    def test_null_y_component_raises_exception(self):
        with self.assertRaises(YComponentNullException):
            Vector(x=0, y=None)

    def test_y_component_below_lower_bound_raises_error(self):
        with self.assertRaises(YComponentBelowLowerBoundException):
            Vector(x=0, y=-(KNIGHT_STEP_SIZE + 1))


    def test_y_component_above_upper_bound_raises_error(self):
        with self.assertRaises(YComponentAboveUpperBoundException):
            Vector(x=0, y=(KNIGHT_STEP_SIZE + 1))


    def test_y_component_within_bounds(self):
        # Test all valid delta_row values from -3 to +3 inclusive
        # print()
        for y in range(-KNIGHT_STEP_SIZE, KNIGHT_STEP_SIZE + 1):
            vector = Vector(x=0, y=y)
            # print(f"Testing delta_row: {distance_test.delta_row} expected={delta_row}")
            self.assertEqual(vector.y, y)


if __name__ == '__main__':
    unittest.main()
