import unittest

from chess.exception.stack import PopEmptyStackException, PushingNullEntityException, DuplicatePushException
from chess.geometry.coordinate.coord import Coordinate
from chess.token.model.coord import CoordinateStack


class CoordinateStackTest(unittest.TestCase):

    def test_internal_data_structure_not_null(self):
        self.assertIsNotNone(CoordinateStack().items)


    def test_new_coordinate_stack_is_empty(self):
        self.assertTrue(len(CoordinateStack().items) == 0)


    def test_pop_empty_stack_raises_exception(self):
        with self.assertRaises(PopEmptyStackException):
            CoordinateStack().undo_push()


    def test_null_coordinate_push_raises_exception(self):
        with self.assertRaises(PushingNullEntityException):
            CoordinateStack().push_coordinate(None)


    def test_duplicate_coordinate_push_raises_exception(self):
        coord = Coordinate(row=1, column=1)
        coordinate_stack = CoordinateStack()
        coordinate_stack.push_coordinate(coord)

        with self.assertRaises(DuplicatePushException):
            coordinate_stack.push_coordinate(coord)

    def test_pushing_coordinate_updates_current_coordinate(self):
        coord1 = Coordinate(row=1, column=1)
        coord2 = Coordinate(row=2, column=2)

        coordinate_stack = CoordinateStack()
        coordinate_stack.push_coordinate(coord1)
        self.assertEqual(coordinate_stack.current_coordinate, coord1)

        coordinate_stack.push_coordinate(coord2)
        self.assertEqual(coordinate_stack.current_coordinate, coord2)

    def test_undo_push_updates_current_coordinate(self):
        coord1 = Coordinate(row=1, column=1)
        coord2 = Coordinate(row=2, column=2)

        coordinate_stack = CoordinateStack()
        coordinate_stack.push_coordinate(coord1)
        coordinate_stack.push_coordinate(coord2)

        coordinate_stack.undo_push()
        self.assertEqual(coordinate_stack.current_coordinate, coord1)


    def test_pushing_coordinate_increments_size(self):
        coord1 = Coordinate(row=1, column=1)

        coordinate_stack = CoordinateStack()
        original_size = coordinate_stack.size()
        self.assertEqual(coordinate_stack.size(), 0)

        coordinate_stack.push_coordinate(coord1)
        self.assertEqual(coordinate_stack.size(), original_size + 1)


    def test_undo_push_decrements_size(self):

        coordinate_stack = CoordinateStack()
        coordinate_stack.push_coordinate(Coordinate(row=1, column=1))
        size_before_undo = coordinate_stack.size()

        coordinate_stack.undo_push()
        self.assertEqual(coordinate_stack.size(), size_before_undo - 1)


    def test_is_empty_corresponds_to_zero_stack_size(self):
        coordinate_stack = CoordinateStack()

        self.assertTrue(coordinate_stack.is_empty() and coordinate_stack.size() == 0)

    def test_is_empty_false_when_stack_has_items(self):
        coordinate_stack = CoordinateStack()
        coordinate_stack.push_coordinate(Coordinate(row=0, column=0))

        self.assertTrue(not coordinate_stack.is_empty() and coordinate_stack.size() > 0)

    def test_if_stack_Is_empty_then_current_coordinate_is_null(self):
        coordinate_stack = CoordinateStack()
        self.assertTrue(
            coordinate_stack.is_empty() and coordinate_stack.current_coordinate is None
        )


if __name__ == '__main__':
    unittest.main()
