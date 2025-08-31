import unittest
from unittest.mock import patch, Mock

from assurance.exception.validation.id import IdValidationException
from chess.board.square import Square



class SquareUnitTest(unittest.TestCase):

    @patch('assurance.validators.coord.CoordinateValidator.validate')
    @patch('assurance.validators.name.NameValidator.validate')
    @patch('assurance.validators.id.IdValidator.validate')
    def test_square_raises_on_failed_id(self, mock_coord_validate, mock_name_validate, mock_id_validate):

        mock_id_validate.return_value.is_success.return_value = False
        mock_id_validate.return_value.exception = IdValidationException("Invalid ID")

        mock_name_validate.return_value.is_success.return_value = True
        mock_coord_validate.return_value.is_success.return_value = True

        with self.assertRaises(IdValidationException):
            Square(square_id=1, name="A1", coordinate=Mock())


if __name__ == '__main__':
    unittest.main()
