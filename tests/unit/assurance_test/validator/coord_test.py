import unittest
from unittest.mock import create_autospec

from assurance.exception.validation.coord import CoordValidationException
from assurance.validators.coord import CoordValidator
from chess.common.config import ROW_SIZE, COLUMN_SIZE
from chess.exception.coord_exception import (
    RowBelowBoundsException,
    RowAboveBoundsException,
    ColumnBelowBoundsException,
    ColumnAboveBoundsException
)
from chess.geometry.exception.coord.column_null import NullColumnException
from chess.geometry.exception.coord.coord_null import NullCoordException
from chess.geometry.exception.coord.row_null import NullRowException
from chess.geometry.coord import Coord



class CoordValidatorTest(unittest.TestCase):


    def test_null_coord_raises_exception(self):
        with self.assertRaises(CoordValidationException) as ctx:
            CoordValidator.validate(None)

        self.assertIsInstance(ctx.exception.__cause__, NullCoordException)


    def test_cast_to_coord_failure_raises_exception(self):
        with self.assertRaises(CoordValidationException) as ctx:
            CoordValidator.validate(1)

        self.assertIsInstance(ctx.exception.__cause__, TypeError)


    def test_null_row_raises_exception(self):
        # Create a mock Coord with row = None
        mock_coord = create_autospec(Coord, instance=True)
        mock_coord.row = None
        mock_coord.column = 0  # valid column

        with self.assertRaises(CoordValidationException) as ctx:
            CoordValidator.validate(mock_coord)

        self.assertIsInstance(ctx.exception.__cause__, NullRowException)

    def test_row_below_bound_raises_exception(self):

        # Create a mock Coord with row = None
        mock_coord = create_autospec(Coord, instance=True)
        mock_coord.row = -1
        mock_coord.column = 0  # valid column

        with self.assertRaises(CoordValidationException) as ctx:
            CoordValidator.validate(mock_coord)

        self.assertIsInstance(ctx.exception.__cause__, RowBelowBoundsException)

    def test_row_above_or_equals_bound_raises_exception(self):
        # Create a mock Coord with row = None
        mock_coord = create_autospec(Coord, instance=True)
        mock_coord.row = ROW_SIZE
        mock_coord.column = 0  # valid column

        with self.assertRaises(CoordValidationException) as ctx:
            CoordValidator.validate(mock_coord)

        self.assertIsInstance(ctx.exception.__cause__, RowAboveBoundsException)


    def test_null_column_raises_exception(self):
        # Create a mock Coord with row = None
        mock_coord = create_autospec(Coord, instance=True)
        mock_coord.row = 0
        mock_coord.column = None

        with self.assertRaises(CoordValidationException) as ctx:
            CoordValidator.validate(mock_coord)

        self.assertIsInstance(ctx.exception.__cause__, NullColumnException)

    def test_column_below_bound_raises_exception(self):
        # Create a mock Coord with row = None
        mock_coord = create_autospec(Coord, instance=True)
        mock_coord.row = 0
        mock_coord.column = -1

        with self.assertRaises(CoordValidationException) as ctx:
            CoordValidator.validate(mock_coord)

        self.assertIsInstance(ctx.exception.__cause__, ColumnBelowBoundsException)

    def test_column_above_bound_raises_exception(self):
        # Create a mock Coord with row = None
        mock_coord = create_autospec(Coord, instance=True)
        mock_coord.row = 0
        mock_coord.column = COLUMN_SIZE

        with self.assertRaises(CoordValidationException) as ctx:
            CoordValidator.validate(mock_coord)

        self.assertIsInstance(ctx.exception.__cause__, ColumnAboveBoundsException)


    def test_validation_payload_equals_input_param(self):
        mock_coord = CoordValidataorTest.valid_mock_coord(3, 4)
        result = CoordValidator.validate(mock_coord)
        self.assertEqual(result.payload, mock_coord)


if __name__ == '__main__':
    unittest.main()
