import unittest
from unittest.mock import patch, Mock, create_autospec

from assurance.exception.validation.coord import CoordValidationException
from assurance.exception.validation.id import IdValidationException
from assurance.exception.validation.name import NameValidationException
from chess.board.square import Square
from chess.geometry.coord import Coord
from chess.piece.piece import Piece
from unit.chess_test.geometry.coord_test import CoordTest


class SquareTest(unittest.TestCase):

    @staticmethod
    def valid_mock_square(
        square_id=1,
        name="A1",
        coordinate=CoordTest.valid_mock_coord()
    ):
        square = create_autospec(Square, instance=True)
        square.id=square_id
        square.name=name
        square.coord=coordinate
        return square

    @patch('assurance.validators.coord.CoordValidator.validate')
    @patch('assurance.validators.name.NameValidator.validate')
    @patch('assurance.validators.id.IdValidator.validate')
    def test_square_failed_id_validation_raises_error(
        self,
        mock_coord_validate,
        mock_name_validate,
        mock_id_validate
    ):
        mock_id_validate.return_value.is_success.return_value = False
        mock_id_validate.return_value.exception = IdValidationException("Invalid ID")

        mock_name_validate.return_value.is_success.return_value = True
        mock_coord_validate.return_value.is_success.return_value = True

        with self.assertRaises(IdValidationException):
            Square(square_id=-1, name="A1", coord=Mock())


    @patch('assurance.validators.coord.CoordValidator.validate')
    @patch('assurance.validators.name.NameValidator.validate')
    @patch('assurance.validators.id.IdValidator.validate')
    def test_square_failed_name_validation_raises_error(
        self,
        mock_coord_validate,
        mock_name_validate,
        mock_id_validate
    ):
        mock_id_validate.return_value.is_success.return_value = True

        mock_name_validate.return_value.is_success.return_value = False
        mock_name_validate.return_value.exception = NameValidationException("Invalid name")

        mock_coord_validate.return_value.is_success.return_value = True

        with self.assertRaises(NameValidationException):
            Square(square_id=1, name="", coord=Mock())


    @patch('assurance.validators.coord.CoordValidator.validate')
    @patch('assurance.validators.name.NameValidator.validate')
    @patch('assurance.validators.id.IdValidator.validate')
    def test_square_failed_coordinate_validation_raises_error(
        self,
        mock_coord_validate,
        mock_name_validate,
        mock_id_validate
    ):
        mock_id_validate.return_value.is_success.return_value = True
        mock_name_validate.return_value.is_success.return_value = True

        mock_coord_validate.return_value.is_success.return_value = False
        mock_coord_validate.return_value.exception = CoordValidationException("Invalid coord")

        mock_coordinate = create_autospec(Coord, instance=True)
        mock_coordinate.row = None
        mock_coordinate.column = 0  # valid column

        with self.assertRaises(CoordValidationException):
            Square(square_id=1, name="A-2", coord=None)


    @patch('assurance.validators.coord.CoordValidator.validate')
    @patch('assurance.validators.name.NameValidator.validate')
    @patch('assurance.validators.id.IdValidator.validate')
    def test_square_constructed_if_all_validations_pass(
        self,
        mock_coord_validate,
        mock_name_validate,
        mock_id_validate
    ):
        mock_id_validate.return_value.is_success.return_value = True
        mock_name_validate.return_value.is_success.return_value = True

        mock_coord_validate.return_value.is_success.return_value = True

        mock_coordinate = create_autospec(Coord, instance=True)
        mock_coordinate.row = 0
        mock_coordinate.column = 0

        Square(square_id=1, name="A-2", coord=mock_coordinate)


    def test_set_occupant_gets_wrong_type_raises_error(self):
        mock_coordinate = create_autospec(Coord, instance=True)
        mock_coordinate.row = 0
        mock_coordinate.column = 0

        square = Square(square_id=1, name="A-2", coord=mock_coordinate)
        with self.assertRaises(TypeError):(
            square.occupant)= 5


    def test_set_occupant_passes_on_none(self):
        mock_coordinate = create_autospec(Coord, instance=True)
        mock_coordinate.row = 0
        mock_coordinate.column = 0

        square = Square(square_id=1, name="A-2", coord=mock_coordinate)
        square.occupant = None

        self.assertIsNone(square.occupant)


    def test_set_occupant_passes_on_piece_not_null(self):
        mock_coordinate=CoordTest.valid_mock_coord()
        mock_piece = create_autospec(Piece, instance=True)

        square = Square(square_id=1, name="A-2", coord=mock_coordinate)
        square.occupant = mock_piece

        self.assertEqual(square.occupant, mock_piece)


if __name__ == '__main__':
    unittest.main()
