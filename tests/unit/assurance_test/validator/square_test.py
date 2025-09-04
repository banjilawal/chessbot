import unittest
from unittest.mock import create_autospec

from assurance.exception.validation.coord import CoordValidationException
from assurance.exception.validation.id import IdValidationException
from assurance.exception.validation.name import NameValidationException
from assurance.exception.validation.square import SquareValidationException
from assurance.validators.square import SquareValidator
from chess.board.square import Square
from chess.exception.null.square import NullSquareException
from unit.chess_test.board.square_test import SquareTest
from unit.chess_test.geometry.coord_test import CoordTest


class SquareValidatorTest(unittest.TestCase):

    def test_null_square_raises_exception(self):
        with self.assertRaises(SquareValidationException) as ctx:
            SquareValidator.validate(None)

        self.assertIsInstance(ctx.exception.__cause__, NullSquareException)


    def test_cast_to_square_failure_raises_exception(self):
        with self.assertRaises(SquareValidationException) as ctx:
            SquareValidator.validate(1)

        self.assertIsInstance(ctx.exception.__cause__, TypeError)


    def test_square_validator_failed_id_validation_raises_exception(self):
        mock_square = create_autospec(Square, instance=True)
        mock_square.id=-1
        mock_square._name="A-1"
        mock_square._coord=CoordTest.valid_mock_coord()

        with self.assertRaises(SquareValidationException) as ctx:
            SquareValidator.validate(mock_square)

        self.assertIsInstance(ctx.exception.__cause__, IdValidationException)


    def test_square_validator_failed_name_validation_raises_exception(self):
        mock_square = create_autospec(Square, instance=True)
        mock_square.id=1
        mock_square._name="A"
        mock_square._coord=CoordTest.valid_mock_coord()

        with self.assertRaises(SquareValidationException) as ctx:
            SquareValidator.validate(mock_square)

        self.assertIsInstance(ctx.exception.__cause__, NameValidationException)


    def test_square_validator_failed_coordinate_validation_raises_exception(self):
        mock_square = create_autospec(Square, instance=True)
        mock_square.id=1
        mock_square.name="A-1"
        mock_square.coord=None

        with self.assertRaises(SquareValidationException) as ctx:
            SquareValidator.validate(mock_square)

        self.assertIsInstance(ctx.exception.__cause__, CoordValidationException)


    def test_square_validator_payload_equals_valid_square(self):
        square = SquareTest.valid_mock_square()
        validation = SquareValidator.validate(square)
        self.assertEqual(validation.payload, square)


if __name__ == '__main__':
    unittest.main()
