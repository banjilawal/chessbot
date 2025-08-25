import unittest

import pytest

from chess.exception.null.coordinate_stack_null import NullCoordinateStackException
from chess.geometry.coordinate.coordinate_stack import CoordinateStack, PopEmptyCoordinateStackException


class CoordinateStackTest(unittest.TestCase):

    def test_new_coordinate_stack_list_is_not_null(self):
        coordinate_stack = CoordinateStack()
        self.assertIsNotNone(coordinate_stack.stack)

    def test_new_coordinate_stack_is_empty(self):
        coordinate_stack = CoordinateStack()
        self.assertTrue(coordinate_stack.is_empty())

    def test_pop_empty_stack_raises_exception(self):
        coordinate_stack = CoordinateStack()
        with pytest.raises(PopEmptyCoordinateStackException):
            coordinate_stack.stack.pop()


    def test_push_null_coordinate_raises_exception(self):
        self.assertEqual(True, False)

    def pushing_duplicate_coordinate_raises_exception(self):
        self.assertEqual(True, False)

    def test_empty_stack_size_is_zero(self):
        self.assertEqual(True, False)

    def test_empty_stack_size_not_less_than_zero(self):
        self.assertEqual(True, False)

    def test_push_coordinate_increases_size(self):
        self.assertEqual(True, False)

    def test_pop_coordinate_decreases_size(self):
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
