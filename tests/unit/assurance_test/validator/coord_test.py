import unittest
from unittest.mock import Mock, create_autospec

from assurance.exception.validation.coord import CoordinateValidationException
from assurance.validators.coord import CoordinateValidator
from chess.common.config import ROW_SIZE, COLUMN_SIZE
from chess.exception.coord import (
    RowBelowBoundsException,
    RowAboveBoundsException,
    ColumnBelowBoundsException,
    ColumnAboveBoundsException
)
from chess.exception.null.column import NullColumnException
from chess.exception.null.coord import NullCoordinateException
from chess.exception.null.row import NullRowException
from chess.geometry.coordinate.coord import Coordinate
from unit.chess_test.geometry.coord.coord_test import CoordinateTest


class CoordinateValidatorTest(unittest.TestCase):


    def test_null_coordinate_raises_exception(self):
        with self.assertRaises(CoordinateValidationException) as ctx:
            CoordinateValidator.validate(None)

        self.assertIsInstance(ctx.exception.__cause__, NullCoordinateException)


    def test_cast_to_coordinate_failure_raises_exception(self):
        with self.assertRaises(CoordinateValidationException) as ctx:
            CoordinateValidator.validate(1)

        self.assertIsInstance(ctx.exception.__cause__, TypeError)


    def test_null_row_raises_exception(self):
        # Create a mock Coordinate with row = None
        mock_coordinate = create_autospec(Coordinate, instance=True)
        mock_coordinate.row = None
        mock_coordinate.column = 0  # valid column

        with self.assertRaises(CoordinateValidationException) as ctx:
            CoordinateValidator.validate(mock_coordinate)

        self.assertIsInstance(ctx.exception.__cause__, NullRowException)

    def test_row_below_bound_raises_exception(self):

        # Create a mock Coordinate with row = None
        mock_coordinate = create_autospec(Coordinate, instance=True)
        mock_coordinate.row = -1
        mock_coordinate.column = 0  # valid column

        with self.assertRaises(CoordinateValidationException) as ctx:
            CoordinateValidator.validate(mock_coordinate)

        self.assertIsInstance(ctx.exception.__cause__, RowBelowBoundsException)

    def test_row_above_or_equals_bound_raises_exception(self):
        # Create a mock Coordinate with row = None
        mock_coordinate = create_autospec(Coordinate, instance=True)
        mock_coordinate.row = ROW_SIZE
        mock_coordinate.column = 0  # valid column

        with self.assertRaises(CoordinateValidationException) as ctx:
            CoordinateValidator.validate(mock_coordinate)

        self.assertIsInstance(ctx.exception.__cause__, RowAboveBoundsException)


    def test_null_column_raises_exception(self):
        # Create a mock Coordinate with row = None
        mock_coordinate = create_autospec(Coordinate, instance=True)
        mock_coordinate.row = 0
        mock_coordinate.column = None

        with self.assertRaises(CoordinateValidationException) as ctx:
            CoordinateValidator.validate(mock_coordinate)

        self.assertIsInstance(ctx.exception.__cause__, NullColumnException)

    def test_column_below_bound_raises_exception(self):
        # Create a mock Coordinate with row = None
        mock_coordinate = create_autospec(Coordinate, instance=True)
        mock_coordinate.row = 0
        mock_coordinate.column = -1

        with self.assertRaises(CoordinateValidationException) as ctx:
            CoordinateValidator.validate(mock_coordinate)

        self.assertIsInstance(ctx.exception.__cause__, ColumnBelowBoundsException)

    def test_column_above_bound_raises_exception(self):
        # Create a mock Coordinate with row = None
        mock_coordinate = create_autospec(Coordinate, instance=True)
        mock_coordinate.row = 0
        mock_coordinate.column = COLUMN_SIZE

        with self.assertRaises(CoordinateValidationException) as ctx:
            CoordinateValidator.validate(mock_coordinate)

        self.assertIsInstance(ctx.exception.__cause__, ColumnAboveBoundsException)


    def test_validation_payload_equals_input_param(self):
        mock_coordinate = CoordinateTest.valid_mock_coordinate(3, 4)
        result = CoordinateValidator.validate(mock_coordinate)
        self.assertEqual(result.payload, mock_coordinate)


if __name__ == '__main__':
    unittest.main()
